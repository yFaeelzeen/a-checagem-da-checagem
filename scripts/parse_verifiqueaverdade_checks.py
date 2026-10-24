import os
import sys
import re
import json
import csv
import shutil
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\01_coleta_preservacao_bruta\verifiqueaverdade_com_br'
OUT_DIR = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\02_bases_dados_normalizadas'

def sync_html_shortcuts():
    # Make sure both .html and /index.html exist for ease of access
    debates_dir = os.path.join(DEST_DIR, 'debates')
    g_dir_html = os.path.join(debates_dir, 'globo-2026-10-23', 'index.html')
    g_file_html = os.path.join(debates_dir, 'globo-2026-10-23.html')
    b_dir_html = os.path.join(debates_dir, 'band-2026-10-18', 'index.html')
    b_file_html = os.path.join(debates_dir, 'band-2026-10-18.html')
    
    if os.path.exists(g_dir_html):
        shutil.copy2(g_dir_html, g_file_html)
    if os.path.exists(b_dir_html):
        shutil.copy2(b_dir_html, b_file_html)
    print("Sincronizados atalhos de arquivo HTML (.html e /index.html)")

def parse_debate_html(file_path, debate_title, debate_date):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
        
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article', class_=re.compile(r'claim'))
    
    records = []
    for art in articles:
        card_id = art.get('id', '')
        if not card_id:
            continue
            
        # Meta: speaker, topic, time
        speaker_el = art.find('span', class_='claim-speaker')
        speaker = speaker_el.get_text(strip=True) if speaker_el else ''
        
        topic_el = art.find('span', class_='claim-topic')
        topic = topic_el.get_text(strip=True) if topic_el else ''
        
        time_btn = art.find('button', class_=re.compile(r'claim-time'))
        if time_btn:
            time_text = time_btn.get_text(strip=True).replace('▶', '').strip()
        else:
            time_text = ''
            
        # Verdict
        verdict_el = art.find('span', class_=re.compile(r'verdict'))
        if verdict_el:
            v_text = re.sub(r'^[✓✗≈≠?!\s]+', '', verdict_el.get_text(strip=True)).strip()
        else:
            v_text = ''
            
        # Claim
        claim_el = art.find('p', class_='claim-text')
        claim_text = claim_el.get_text(strip=True) if claim_el else ''
        
        # Reasoning
        reason_el = art.find('p', class_='claim-reasoning')
        reason_text = reason_el.get_text(strip=True) if reason_el else ''
        
        # Sources
        sources_el = art.find('p', class_='claim-sources')
        source_urls = []
        source_texts = []
        if sources_el:
            for a in sources_el.find_all('a'):
                href = a.get('href', '')
                txt = a.get_text(strip=True)
                if href:
                    source_urls.append(href)
                if txt:
                    source_texts.append(txt)
            raw_source_p = sources_el.get_text(strip=True).replace('Fontes:', '').strip()
        else:
            raw_source_p = ''
            
        m_block = re.match(r'b(\d+)-(\d+)', card_id)
        bloco_num = m_block.group(1) if m_block else ''
        ordem_bloco = m_block.group(2) if m_block else ''
        
        records.append({
            'projeto_origem': 'Verifique a Verdade',
            'debate_referencia': debate_title,
            'data_debate': debate_date,
            'id_original': card_id,
            'bloco': f"Bloco {bloco_num}",
            'ordem_no_bloco': ordem_bloco,
            'horario_alegacao': time_text,
            'candidato_original': speaker,
            'tema': topic,
            'veredito_original': v_text,
            'alegacao_citada': claim_text,
            'justificativa_verificacao': reason_text,
            'fontes_texto': raw_source_p,
            'fontes_urls': source_urls,
            'arquivo_bruto_origem': os.path.relpath(file_path, r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem').replace('\\', '/')
        })
        
    return records

def main():
    print("=== EXTRACT & PARSE ALL VERIFIQUE A VERDADE CHECKS ===")
    sync_html_shortcuts()
    
    globo_live_path = os.path.join(DEST_DIR, 'debates', 'globo-2026-10-23', 'index.html')
    band_path = os.path.join(DEST_DIR, 'debates', 'band-2026-10-18', 'index.html')
    
    globo_checks = parse_debate_html(globo_live_path, 'Debate Presidencial TV Globo (2º Turno)', '2026-10-23')
    print(f"Total Globo checks parsed from live: {len(globo_checks)}")
    
    band_checks = parse_debate_html(band_path, 'Debate Presidencial Band (2º Turno)', '2026-10-18')
    print(f"Total Band checks parsed from live: {len(band_checks)}")
    
    fields = [
        'projeto_origem', 'debate_referencia', 'data_debate', 'id_original', 'bloco', 'ordem_no_bloco',
        'horario_alegacao', 'candidato_original', 'tema', 'veredito_original', 'alegacao_citada',
        'justificativa_verificacao', 'fontes_texto', 'fontes_urls', 'arquivo_bruto_origem'
    ]
    
    # Export Globo 149
    out_globo_csv = os.path.join(OUT_DIR, 'verifiqueaverdade_globo_149_checagens.csv')
    out_globo_json = os.path.join(OUT_DIR, 'verifiqueaverdade_globo_149_checagens.json')
    if globo_checks:
        with open(out_globo_csv, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in globo_checks:
                row = dict(r)
                row['fontes_urls'] = ' | '.join(row['fontes_urls'])
                w.writerow(row)
        with open(out_globo_json, 'w', encoding='utf-8') as f:
            json.dump(globo_checks, f, ensure_ascii=False, indent=2)
        print(f"Salvo Globo 149 em: {out_globo_csv}")
        
    # Export Band 107
    out_band_csv = os.path.join(OUT_DIR, 'verifiqueaverdade_band_107_checagens.csv')
    out_band_json = os.path.join(OUT_DIR, 'verifiqueaverdade_band_107_checagens.json')
    if band_checks:
        with open(out_band_csv, 'w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in band_checks:
                row = dict(r)
                row['fontes_urls'] = ' | '.join(row['fontes_urls'])
                w.writerow(row)
        with open(out_band_json, 'w', encoding='utf-8') as f:
            json.dump(band_checks, f, ensure_ascii=False, indent=2)
        print(f"Salvo Band 107 em: {out_band_csv}")
        
    # Total combined for Verifique a Verdade
    total_vav = globo_checks + band_checks
    out_total_csv = os.path.join(OUT_DIR, 'verifiqueaverdade_total_256_checagens.csv')
    out_total_json = os.path.join(OUT_DIR, 'verifiqueaverdade_total_256_checagens.json')
    with open(out_total_csv, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in total_vav:
            row = dict(r)
            row['fontes_urls'] = ' | '.join(row['fontes_urls'])
            w.writerow(row)
    with open(out_total_json, 'w', encoding='utf-8') as f:
        json.dump(total_vav, f, ensure_ascii=False, indent=2)
    print(f"Salvo Total VAV ({len(total_vav)} checagens) em: {out_total_csv}")

if __name__ == '__main__':
    main()
