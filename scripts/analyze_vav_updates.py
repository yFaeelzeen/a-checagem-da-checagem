import os
import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

REPO = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'
GLOBO_LIVE_PATH = os.path.join(REPO, '01_coleta_preservacao_bruta', 'verifiqueaverdade_com_br', 'debates', 'globo-2026-10-23.html')
GLOBO_OLD_PATH = os.path.join(REPO, '01_coleta_preservacao_bruta', 'verifiqueaverdade_com_br', 'debates', 'globo-2026-10-23_snapshot_inicial_132.html')
METO_PATH = os.path.join(REPO, '01_coleta_preservacao_bruta', 'verifiqueaverdade_com_br', 'metodologia', 'index.html')
PORTAIS_CATALOG = os.path.join(REPO, '02_bases_dados_normalizadas', 'catalogo_portais_219_checagens.json')

def main():
    print("=== ANÁLISE DAS 17 NOVAS CHECAGENS E METODOLOGIA DO VERIFIQUE A VERDADE ===")
    
    # 1. Methodology extraction
    if os.path.exists(METO_PATH):
        with open(METO_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            meto_soup = BeautifulSoup(f.read(), 'html.parser')
        main_content = meto_soup.find('main') or meto_soup.find('article') or meto_soup.body
        meto_text = main_content.get_text(separator='\n', strip=True) if main_content else ''
        print("\n--- Metodologia Oficial Extraída ---")
        print(meto_text[:1200])
        print("...\n")
        
        # Save clean markdown version of methodology
        meto_md_path = os.path.join(REPO, '03_auditoria_estrutural_e_fontes', 'metodologia_oficial_verifique_a_verdade.md')
        with open(meto_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# Metodologia Oficial — Verifique a Verdade\n\n*Extraído via REA em 24/10/2026 de https://verifiqueaverdade.com.br/metodologia/*\n\n```text\n{meto_text}\n```\n")
        print(f"Salva metodologia em markdown: {meto_md_path}")
        
    # 2. Inspect 17 new checks in Globo debate
    with open(GLOBO_LIVE_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        soup_live = BeautifulSoup(f.read(), 'html.parser')
    with open(GLOBO_OLD_PATH, 'r', encoding='utf-8', errors='ignore') as f:
        soup_old = BeautifulSoup(f.read(), 'html.parser')
        
    cards_live = {c.get('id'): c for c in soup_live.find_all('article', class_=re.compile(r'claim'))}
    cards_old = {c.get('id'): c for c in soup_old.find_all('article', class_=re.compile(r'claim'))}
    
    new_ids = sorted(set(cards_live.keys()) - set(cards_old.keys()))
    print(f"\nTotal novas checagens identificadas: {len(new_ids)}")
    
    new_records = []
    for nid in new_ids:
        art = cards_live[nid]
        speaker = art.find('span', class_='claim-speaker').get_text(strip=True) if art.find('span', class_='claim-speaker') else ''
        topic = art.find('span', class_='claim-topic').get_text(strip=True) if art.find('span', class_='claim-topic') else ''
        time_btn = art.find('button', class_=re.compile(r'claim-time'))
        t_text = time_btn.get_text(strip=True).replace('▶', '').strip() if time_btn else ''
        verdict = art.find('span', class_=re.compile(r'verdict')).get_text(strip=True) if art.find('span', class_=re.compile(r'verdict')) else ''
        v_clean = re.sub(r'^[✓✗≈≠?!\s]+', '', verdict).strip()
        claim = art.find('p', class_='claim-text').get_text(strip=True) if art.find('p', class_='claim-text') else ''
        reason = art.find('p', class_='claim-reasoning').get_text(strip=True) if art.find('p', class_='claim-reasoning') else ''
        sources = [a.get('href') for a in art.find_all('a') if a.get('href')]
        
        rec = {
            'id': nid,
            'candidato': speaker,
            'horario': t_text,
            'tema': topic,
            'veredito': v_clean,
            'alegacao': claim,
            'justificativa': reason,
            'fontes': sources
        }
        new_records.append(rec)
        print(f"\n[{nid}] ({speaker} - {v_clean}) | {t_text} | {topic}")
        print(f"  Fala: {claim}")
        print(f"  Justificativa: {reason[:160]}...")
        print(f"  Fontes: {sources}")

    # Check match with portals
    with open(PORTAIS_CATALOG, 'r', encoding='utf-8') as f:
        portais = json.load(f)
        
    print("\n--- Confronto das 17 Novas Checagens com os Grandes Portais ---")
    matches = []
    for nr in new_records:
        kws = [w.lower() for w in re.findall(r'\b[a-zA-Záéíóúâêîôûãõç]{4,}\b', nr['alegacao']) if w.lower() not in ['para', 'com', 'mais', 'como', 'sobre', 'disse', 'pelo', 'pela', 'quando', 'onde']]
        matched_portals = []
        for p in portais:
            p_text = (p.get('declaracao_auditada', '') + ' ' + p.get('contexto_ou_resumo', '')).lower()
            score = sum(1 for kw in kws if kw in p_text)
            if score >= 3 or (len(kws) <= 3 and score >= 2):
                matched_portals.append({
                    'veiculo': p['veiculo'],
                    'candidato': p['candidato'],
                    'classificacao': p['classificacao_original'],
                    'declaracao': p['declaracao_auditada'],
                    'score': score
                })
        print(f"[{nr['id']}] {nr['candidato']} ({nr['veredito']}): {nr['alegacao'][:60]}... -> {len(matched_portals)} matches nos portais")
        for mp in matched_portals[:3]:
            print(f"   -> {mp['veiculo']} ({mp['classificacao']}): {mp['declaracao'][:80]}...")
            
    # Save inspection report
    out_json = os.path.join(REPO, '03_auditoria_estrutural_e_fontes', 'verifique_a_verdade_17_novas_checagens.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(new_records, f, ensure_ascii=False, indent=2)
    print(f"\nSalvo arquivo das 17 novas checagens em: {out_json}")

if __name__ == '__main__':
    main()
