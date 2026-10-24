import os, sys, re, json, csv
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'
out_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'

all_individual_checks = []

# ==========================================
# 1. PARSE G1 — FATO OU FAKE
# ==========================================
with open(os.path.join(raw_dir, 'g1_fato_ou_fake.html'), 'r', encoding='utf-8', errors='ignore') as f:
    g1_html = f.read()

g1_paras = re.findall(r'<p[^>]*>(.*?)</p>', g1_html, re.S)
current_cand = 'Flávio Bolsonaro' # Starts with Flavio

for i, p in enumerate(g1_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'FLÁVIO BOLSONARO (PL)' in clean_p.upper():
        current_cand = 'Flávio Bolsonaro'
    elif 'LULA (PT)' in clean_p.upper():
        current_cand = 'Lula'
        
    m = re.search(r'(A declaração é\s*|#)(#?FATO|#?FAKE|#?NÃOÉBEMASSIM|#?NÃO É BEM ASSIM)', clean_p, re.I)
    if m:
        v_raw = m.group(2).replace('#', '').strip().upper()
        if v_raw == 'NÃOÉBEMASSIM': v_raw = 'NÃO É BEM ASSIM'
        
        # quote is previous paragraph
        quote = re.sub(r'<[^>]+>', ' ', g1_paras[i-1]).strip() if i > 0 else ''
        if quote.startswith('“') or quote.startswith('"'):
            pass
        elif i > 1:
            quote = re.sub(r'<[^>]+>', ' ', g1_paras[i-2]).strip() + ' ' + quote
            
        just = clean_p[m.end():].strip()
        if just.startswith('.'): just = just[1:].strip()
        if just.lower().startswith('veja por quê:'): just = just[13:].strip()
        if len(just) < 80 and i + 1 < len(g1_paras):
            just += ' ' + re.sub(r'<[^>]+>', ' ', g1_paras[i+1]).strip()
            
        all_individual_checks.append({
            'audit_id': f'G1_{len(all_individual_checks)+1:03d}',
            'veiculo': 'G1 — Fato ou Fake',
            'candidato': current_cand,
            'declaracao': quote,
            'tema': 'Debate Globo 2º Turno',
            'veredito_original': f'#{v_raw}',
            'justificativa': just,
            'url_fonte': 'https://g1.globo.com/google/amp/fato-ou-fake/eleicoes/noticia/2026/10/23/veja-o-que-e-fato-ou-fake-nas-falas-de-flavio-bolsonaro-e-lula-no-debate-da-globo-no-2o-turno-das-eleicoes-2026.ghtml',
            'completude': 'Completo',
            'trecho_evidencia': clean_p[:300]
        })

# ==========================================
# 2. PARSE UOL CONFERE
# ==========================================
with open(os.path.join(raw_dir, 'uol_confere.html'), 'r', encoding='utf-8', errors='ignore') as f:
    uol_html = f.read()

uol_paras = re.findall(r'<p[^>]*>(.*?)</p>', uol_html, re.S)
current_cand = 'Flávio Bolsonaro'

for i, p in enumerate(uol_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'Flávio Bolsonaro' in clean_p and len(clean_p) < 30:
        current_cand = 'Flávio Bolsonaro'
    elif 'Lula' in clean_p and len(clean_p) < 30:
        current_cand = 'Lula'
        
    m = re.match(r'^(FALSO|ENGANOSO|VERDADEIRO|IMPRECISO|SEM CONTEXTO)\.?(.*)', clean_p, re.I)
    if m:
        verdict = m.group(1).upper()
        just = m.group(2).strip()
        quote = ''
        for back in range(1, 4):
            if i - back >= 0:
                cq = re.sub(r'<[^>]+>', ' ', uol_paras[i - back]).strip()
                if cq and not any(cq.startswith(v) for v in ['FALSO', 'ENGANOSO', 'VERDADEIRO', 'IMPRECISO']):
                    quote = cq
                    break
        if len(just) < 80 and i + 1 < len(uol_paras):
            just += ' ' + re.sub(r'<[^>]+>', ' ', uol_paras[i + 1]).strip()
            
        all_individual_checks.append({
            'audit_id': f'UOL_{len(all_individual_checks)+1:03d}',
            'veiculo': 'UOL Confere',
            'candidato': current_cand,
            'declaracao': quote,
            'tema': 'Debate Globo 2º Turno',
            'veredito_original': verdict,
            'justificativa': just,
            'url_fonte': 'https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm',
            'completude': 'Completo',
            'trecho_evidencia': clean_p[:300]
        })

# ==========================================
# 3. PARSE ESTADÃO VERIFICA
# ==========================================
with open(os.path.join(raw_dir, 'estadao_verifica.html'), 'r', encoding='utf-8', errors='ignore') as f:
    est_html = f.read()

blocks = re.findall(r'<h[23][^>]*>(.*?)</h[23]>(.*?)(?=<h[23]|$)', est_html, re.S)
current_cand = 'Lula'

for heading, body in blocks:
    clean_h = re.sub(r'<[^>]+>', ' ', heading).strip()
    if 'Lula' in clean_h and ('PT' in clean_h or len(clean_h) < 15):
        current_cand = 'Lula'
        continue
    elif 'Flávio' in clean_h and ('PL' in clean_h or len(clean_h) < 20):
        current_cand = 'Flávio Bolsonaro'
        continue
        
    m_verd = re.search(r'(é|O Estadão Verifica checou que é)\s+(verdadeiro|falso|enganoso|impreciso|exagerado|sem contexto)', body, re.I)
    if m_verd:
        verdict = m_verd.group(2).capitalize()
        m_quote = re.search(r'(O que disse[^:]*:|O candidato disse[^:]*:?)(.*?)(?=(Como checamos|O que checamos|<p>é|$))', body, re.S | re.I)
        claim = re.sub(r'<[^>]+>', ' ', m_quote.group(2)).strip() if m_quote else clean_h
        m_just = re.search(r'(Como checamos[^:]*:|O que checamos[^:]*:)(.*)', body, re.S | re.I)
        just = re.sub(r'<[^>]+>', ' ', m_just.group(2)).strip() if m_just else re.sub(r'<[^>]+>', ' ', body).strip()
        
        all_individual_checks.append({
            'audit_id': f'EST_{len(all_individual_checks)+1:03d}',
            'veiculo': 'Estadão Verifica',
            'candidato': current_cand,
            'declaracao': claim,
            'tema': clean_h,
            'veredito_original': verdict,
            'justificativa': just[:600],
            'url_fonte': 'https://www.estadao.com.br/amp/estadao-verifica/debate-tv-globo-checagem-tempo-real-ao-vivo/',
            'completude': 'Completo',
            'trecho_evidencia': (claim + ' ' + just)[:300]
        })

# ==========================================
# 4. PARSE AGÊNCIA LUPA
# ==========================================
with open(os.path.join(raw_dir, 'agencia_lupa.html'), 'r', encoding='utf-8', errors='ignore') as f:
    lupa_html = f.read()

pattern = r'<div class="block-text">\s*<strong>(.*?)</strong>\s*</div>'
matches = list(re.finditer(pattern, lupa_html, re.I | re.S))

for idx, m in enumerate(matches):
    verdict = m.group(1).strip()
    pos = m.start()
    pre_html = lupa_html[max(0, pos-2000):pos]
    pre_paras = re.findall(r'<p[^>]*>(.*?)</p>', pre_html, re.S)
    quote = re.sub(r'<[^>]+>', ' ', pre_paras[-1]).strip() if pre_paras else ''
    
    post_html = lupa_html[m.end():min(len(lupa_html), m.end()+2500)]
    post_paras = re.findall(r'<p[^>]*>(.*?)</p>', post_html, re.S)
    just = ' '.join(re.sub(r'<[^>]+>', ' ', p).strip() for p in post_paras[:2]) if post_paras else ''
    
    cand = 'Flávio Bolsonaro'
    combined_txt = (quote + ' ' + just).lower()
    if 'lula' in combined_txt and 'flávio' not in combined_txt:
        cand = 'Lula'
    elif 'flávio' in combined_txt or 'bolsonaro' in combined_txt:
        cand = 'Flávio Bolsonaro'
        
    all_individual_checks.append({
        'audit_id': f'LUPA_{len(all_individual_checks)+1:03d}',
        'veiculo': 'Agência Lupa',
        'candidato': cand,
        'declaracao': quote,
        'tema': 'Debate Globo 2º Turno',
        'veredito_original': verdict,
        'justificativa': just,
        'url_fonte': 'https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/',
        'completude': 'Completo',
        'trecho_evidencia': (quote + ' ' + just)[:300]
    })

print(f'Total individual checks parsed across 4 outlets: {len(all_individual_checks)}')

# Save 02_CHECAGENS_INDIVIDUAIS.json
out_json = os.path.join(out_dir, '02_CHECAGENS_INDIVIDUAIS.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(all_individual_checks, f, indent=2, ensure_ascii=False)

# Save 02_CHECAGENS_INDIVIDUAIS.csv
out_csv = os.path.join(out_dir, '02_CHECAGENS_INDIVIDUAIS.csv')
with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID Auditoria', 'Veículo', 'Candidato', 'Declaração', 'Tema', 'Veredito Original', 'Justificativa', 'URL Fonte', 'Completude', 'Trecho Evidência'])
    for c in all_individual_checks:
        w.writerow([
            c['audit_id'], c['veiculo'], c['candidato'], c['declaracao'],
            c['tema'], c['veredito_original'], c['justificativa'],
            c['url_fonte'], c['completude'], c['trecho_evidencia']
        ])

print('Successfully exported 02_CHECAGENS_INDIVIDUAIS.json and .csv')
