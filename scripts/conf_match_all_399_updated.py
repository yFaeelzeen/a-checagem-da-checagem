import os
import sys
import json
import csv
import re

sys.stdout.reconfigure(encoding='utf-8')

REPO = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'
BASE_DIR = os.path.join(REPO, '02_bases_dados_normalizadas')
OUT_DIR = os.path.join(REPO, '05_confronto_independentes_vs_portais')

# Load files
indep_cat_path = os.path.join(BASE_DIR, 'catalogo_independentes_383_checagens.json')
vav_149_path = os.path.join(BASE_DIR, 'verifiqueaverdade_globo_149_checagens.json')
portals_cat_path = os.path.join(BASE_DIR, 'catalogo_portais_219_checagens.json')

with open(indep_cat_path, 'r', encoding='utf-8') as f:
    indep_old = json.load(f)

with open(vav_149_path, 'r', encoding='utf-8') as f:
    vav_149 = json.load(f)

with open(portals_cat_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)

# Rebuild complete independent catalogue for Globo debate:
# Keep Pinóquio.live (175) and Verifique os Fatos (75)
pinoquio = [r for r in indep_old if r['projeto_origem'] == 'Pinóquio.live']
vof = [r for r in indep_old if r['projeto_origem'] == 'Verifique os Fatos']
flagcheck = [r for r in indep_old if r['projeto_origem'] == 'FlagCheck']

# Convert vav_149 records to matching schema
vav_standardized = []
for r in vav_149:
    vav_standardized.append({
        'projeto_origem': 'Verifique a Verdade',
        'id_original': r['id_original'],
        'candidato_original': r['candidato_original'],
        'debate_referencia': r['debate_referencia'],
        'data_debate': r['data_debate'],
        'horario_alegacao': r['horario_alegacao'],
        'tema': r['tema'],
        'alegacao_citada': r['alegacao_citada'],
        'afirmacao_resumida': '',
        'veredito_original': r['veredito_original'],
        'justificativa_verificacao': r['justificativa_verificacao'],
        'correcao': '',
        'fontes': r['fontes_urls'],
        'arquivo_bruto_origem': r['arquivo_bruto_origem'],
        'observacoes': f"Posição: {r['bloco']}, checagem nº {r['ordem_no_bloco']}"
    })

# Total individual Globo independent checks: 175 + 149 + 75 = 399
indep_checks_399 = pinoquio + vav_standardized + vof
print(f"Total checagens individuais independentes (Globo atualizado): {len(indep_checks_399)}")
print(f"  Pinóquio.live: {len(pinoquio)}")
print(f"  Verifique a Verdade (atualizado): {len(vav_standardized)}")
print(f"  Verifique os Fatos: {len(vof)}")

# Save updated catalogue (399 + 1 = 400 registros)
cat_400 = indep_checks_399 + flagcheck
cat_400_json = os.path.join(BASE_DIR, 'catalogo_independentes_400_checagens_globo_atualizado.json')
cat_400_csv = os.path.join(BASE_DIR, 'catalogo_independentes_400_checagens_globo_atualizado.csv')

with open(cat_400_json, 'w', encoding='utf-8') as f:
    json.dump(cat_400, f, ensure_ascii=False, indent=2)

with open(cat_400_csv, 'w', encoding='utf-8-sig', newline='') as f:
    fields = list(cat_400[0].keys())
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for row in cat_400:
        r_copy = dict(row)
        if isinstance(r_copy['fontes'], list):
            r_copy['fontes'] = ' | '.join(r_copy['fontes'])
        w.writerow(r_copy)

print(f"Salvo catalogo_independentes_400_checagens_globo_atualizado em: {cat_400_json}")

# Token normalization for matching
def normalize_text(text):
    if not text:
        return set()
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = [w for w in text.split() if len(w) > 3]
    return set(tokens)

portals_indexed = []
for p in portal_checks:
    p_text = p.get('declaracao', '') + ' ' + p.get('tema', '') + ' ' + p.get('justificativa', '')
    portals_indexed.append({
        'data': p,
        'tokens': normalize_text(p_text),
        'cand': p.get('candidato', '').lower()
    })

# Process all 399 checks
matched_results = []
match_count = 0

for idx, ind in enumerate(indep_checks_399):
    ind_id = f"IND-{idx+1:03d}"
    ind_proj = ind['projeto_origem']
    ind_orig_id = ind['id_original']
    ind_cand = ind['candidato_original']
    ind_quote = ind['alegacao_citada']
    ind_verdict = ind['veredito_original']
    ind_expl = ind['justificativa_verificacao']
    
    ind_search_text = ind_quote + ' ' + ind.get('afirmacao_resumida', '')
    ind_tokens = normalize_text(ind_search_text)
    
    cand_key = 'lula' if 'lula' in ind_cand.lower() else ('flávio' if ('flávio' in ind_cand.lower() or 'flavio' in ind_cand.lower()) else '')
    
    matched_portals = []
    for p_idx, p in enumerate(portals_indexed):
        p_cand = p['cand']
        if cand_key and p_cand and (cand_key not in p_cand and p_cand not in cand_key):
            continue
            
        common = ind_tokens.intersection(p['tokens'])
        stop_words = {'para', 'como', 'mais', 'sobre', 'disse', 'pelo', 'pela', 'quando', 'onde', 'este', 'esta', 'esse', 'essa', 'governo', 'brasil'}
        meaningful_common = common - stop_words
        
        score = len(meaningful_common)
        if score >= 3 or (len(ind_tokens) <= 5 and score >= 2):
            matched_portals.append({
                'portal_id': p['data'].get('audit_id', f"PORTAL-{p_idx+1:03d}"),
                'veiculo': p['data']['veiculo'],
                'candidato': p['data']['candidato'],
                'declaracao_portal': p['data']['declaracao'],
                'classificacao_portal': p['data']['veredito_original'],
                'justificativa_portal': p['data']['justificativa'],
                'score_similaridade': score,
                'termos_comuns': sorted(list(meaningful_common))
            })
            
    matched_portals.sort(key=lambda x: x['score_similaridade'], reverse=True)
    
    if matched_portals:
        match_count += 1
        has_match = True
    else:
        has_match = False
        
    matched_results.append({
        'id_confronto': ind_id,
        'projeto_independente': ind_proj,
        'id_original_independente': ind_orig_id,
        'candidato': ind_cand,
        'declaracao_independente': ind_quote,
        'veredito_independente': ind_verdict,
        'justificativa_independente': ind_expl,
        'possui_correspondente_portal': has_match,
        'total_correspondencias_portais': len(matched_portals),
        'portais_correspondentes': matched_portals
    })

print(f"Total declarações mapeadas com sucesso: {match_count} de {len(indep_checks_399)} ({match_count/len(indep_checks_399)*100:.1f}%)")

# Save JSON and CSV
out_json = os.path.join(OUT_DIR, 'confronto_todas_399_checagens.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(matched_results, f, ensure_ascii=False, indent=2)

out_csv = os.path.join(OUT_DIR, 'confronto_todas_399_checagens.csv')
with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow([
        'ID Confronto', 'Projeto Independente', 'ID Original', 'Candidato',
        'Declaração Independente', 'Veredito Independente', 'Justificativa Independente',
        'Possui Correspondente', 'Total Correspondentes', 'Veículo Portal',
        'Classificação Portal', 'Declaração Portal', 'Justificativa Portal', 'Termos Comuns'
    ])
    for mr in matched_results:
        if mr['portais_correspondentes']:
            for p in mr['portais_correspondentes']:
                w.writerow([
                    mr['id_confronto'], mr['projeto_independente'], mr['id_original_independente'],
                    mr['candidato'], mr['declaracao_independente'], mr['veredito_independente'],
                    mr['justificativa_independente'], 'SIM', mr['total_correspondencias_portais'],
                    p['veiculo'], p['classificacao_portal'], p['declaracao_portal'],
                    p['justificativa_portal'], ', '.join(p['termos_comuns'])
                ])
        else:
            w.writerow([
                mr['id_confronto'], mr['projeto_independente'], mr['id_original_independente'],
                mr['candidato'], mr['declaracao_independente'], mr['veredito_independente'],
                mr['justificativa_independente'], 'NÃO', 0,
                'Nenhum portal direto', 'Sem checagem direta', 'N/A', 'N/A', ''
            ])

print(f"Salvo confronto_todas_399_checagens em: {out_json} e {out_csv}")
