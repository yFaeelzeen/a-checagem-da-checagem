import os, sys, json, csv, re
sys.stdout.reconfigure(encoding='utf-8')

# Load files
m2_cat_path = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925\06_RELATORIOS_CONSOLIDADOS\catalogo_estruturado_checagens_consolidado.json'
m4_ind_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\02_CHECAGENS_INDIVIDUAIS.json'
out_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'

with open(m2_cat_path, 'r', encoding='utf-8') as f:
    indep_all = json.load(f)

# Exclude the 1 aggregate FlagCheck panel record to get exactly the 382 individual checks
indep_checks = [r for r in indep_all if r['projeto_origem'] != 'FlagCheck']
print(f"Total individual independent checks: {len(indep_checks)}")

with open(m4_ind_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)
print(f"Total individual portal checks: {len(portal_checks)}")

# Normalize text for matching
def normalize_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = [w for w in text.split() if len(w) > 3]
    return set(tokens)

# Map portals into list with token sets
portals_indexed = []
for p in portal_checks:
    p_text = p.get('declaracao', '') + ' ' + p.get('tema', '') + ' ' + p.get('justificativa', '')
    portals_indexed.append({
        'data': p,
        'tokens': normalize_text(p_text),
        'cand': p.get('candidato', '').lower()
    })

# Process all 382 checks
matched_results = []
match_count = 0

for idx, ind in enumerate(indep_checks):
    ind_id = f"IND-{idx+1:03d}"
    ind_proj = ind['projeto_origem']
    ind_orig_id = ind['id_original']
    ind_cand = ind['candidato_original']
    ind_quote = ind['alegacao_citada']
    ind_verdict = ind['veredito_original']
    ind_expl = ind['justificativa_verificacao']
    
    # Tokens from quote + claim
    ind_search_text = ind_quote + ' ' + ind.get('afirmacao_resumida', '')
    ind_tokens = normalize_text(ind_search_text)
    
    # Try to match with portals
    # A candidate match must either match candidate name or be compatible
    matched_portals = []
    
    cand_key = 'lula' if 'lula' in ind_cand.lower() else ('flávio' if ('flávio' in ind_cand.lower() or 'flavio' in ind_cand.lower()) else '')
    
    for p in portals_indexed:
        # candidate check
        if cand_key and p['cand'] and cand_key not in p['cand'] and p['cand'] != 'desconhecido':
            continue
        
        # calculate overlap of tokens
        overlap = ind_tokens.intersection(p['tokens'])
        # require at least 3 significant tokens in common or significant Jaccard
        if len(ind_tokens) > 0:
            score = len(overlap) / len(ind_tokens)
            # If significant intersection
            if len(overlap) >= 3 and (score >= 0.25 or len(overlap) >= 4):
                matched_portals.append({
                    'veiculo': p['data']['veiculo'],
                    'declaracao': p['data']['declaracao'],
                    'veredito': p['data']['veredito_original'],
                    'justificativa': p['data']['justificativa'],
                    'overlap_tokens': list(overlap),
                    'score': round(score, 2)
                })
    
    # Deduplicate portals by vehicle (keep highest score)
    best_by_vehicle = {}
    for mp in matched_portals:
        v = mp['veiculo']
        if v not in best_by_vehicle or mp['score'] > best_by_vehicle[v]['score']:
            best_by_vehicle[v] = mp
            
    has_match = len(best_by_vehicle) > 0
    if has_match:
        match_count += 1
        
    matched_results.append({
        'id': ind_id,
        'indep_projeto': ind_proj,
        'indep_id_orig': ind_orig_id,
        'candidato': ind_cand,
        'indep_declaracao': ind_quote,
        'indep_veredito': ind_verdict,
        'indep_justificativa': ind_expl,
        'status_pareamento': 'Pareado em Portais' if has_match else 'Exclusiva dos Independentes',
        'qtd_portais_pareados': len(best_by_vehicle),
        'portais_pareados': best_by_vehicle
    })

print(f"Processamento concluído: das 382 checagens, {match_count} encontraram correspondência temático-factual direta em 1 ou mais grandes portais.")

# Save master JSON
with open(os.path.join(out_dir, 'confronto_todas_382_checagens.json'), 'w', encoding='utf-8') as f:
    json.dump(matched_results, f, indent=2, ensure_ascii=False)

print("Arquivo confronto_todas_382_checagens.json salvo com sucesso.")
