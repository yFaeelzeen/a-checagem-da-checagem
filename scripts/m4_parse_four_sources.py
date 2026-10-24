import os, sys, re, json, csv
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

# ==========================================
# 1. PARSER G1 — FATO OU FAKE
# ==========================================
with open(os.path.join(raw_dir, 'g1_fato_ou_fake.html'), 'r', encoding='utf-8', errors='ignore') as f:
    g1_html = f.read()

# In G1 AMP:
# Articles are under candidate sections (FLÁVIO BOLSONARO / LULA)
# Quotes are typically in <blockquote> or <p>"..."</p>
# Verdicts are '#FATO', '#FAKE', '#NÃOÉBEMASSIM'

# Let's extract blocks by looking for #FATO / #FAKE / #NÃOÉBEMASSIM
g1_checks = []
# split by paragraphs
g1_paras = re.findall(r'<p[^>]*>(.*?)</p>', g1_html, re.S)
current_candidate = 'Desconhecido'

for i, p in enumerate(g1_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'FLÁVIO BOLSONARO' in clean_p.upper():
        current_candidate = 'Flávio Bolsonaro'
    elif 'LULA (PT)' in clean_p.upper() or ('LULA' in clean_p.upper() and len(clean_p) < 20):
        current_candidate = 'Lula'
        
    m = re.search(r'(A declaração é\s*|#)(#?FATO|#?FAKE|#?NÃOÉBEMASSIM|#?NÃO É BEM ASSIM)', clean_p, re.I)
    if m:
        verdict = m.group(2).replace('#', '').strip().upper()
        # The quote is usually in the preceding paragraph or in quotation marks
        prev_p = re.sub(r'<[^>]+>', ' ', g1_paras[i-1]).strip() if i > 0 else ''
        # Justification is the rest of this paragraph + following paragraph
        just = clean_p[m.end():].strip()
        if just.startswith('.'): just = just[1:].strip()
        if just.lower().startswith('veja por quê:'): just = just[13:].strip()
        if len(just) < 50 and i + 1 < len(g1_paras):
            just += ' ' + re.sub(r'<[^>]+>', ' ', g1_paras[i+1]).strip()
            
        g1_checks.append({
            'veiculo': 'G1 — Fato ou Fake',
            'candidato': current_candidate,
            'declaracao': prev_p,
            'veredito_original': f'#{verdict}',
            'justificativa': just,
            'paragrafo_bruto': clean_p
        })

print(f'G1 parsed checks: {len(g1_checks)}')

# ==========================================
# 2. PARSER UOL CONFERE
# ==========================================
with open(os.path.join(raw_dir, 'uol_confere.html'), 'r', encoding='utf-8', errors='ignore') as f:
    uol_html = f.read()

uol_paras = re.findall(r'<p[^>]*>(.*?)</p>', uol_html, re.S)
uol_checks = []
current_cand_uol = 'Desconhecido'

for i, p in enumerate(uol_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'Flávio Bolsonaro' in clean_p and len(clean_p) < 30:
        current_cand_uol = 'Flávio Bolsonaro'
    elif 'Lula' in clean_p and len(clean_p) < 30:
        current_cand_uol = 'Lula'
        
    # UOL uses bold tags like <b>FALSO.</b> or text starting with FALSO / ENGANOSO / VERDADEIRO
    m = re.match(r'^(FALSO|ENGANOSO|VERDADEIRO|IMPRECISO|SEM CONTEXTO)\.?(.*)', clean_p, re.I)
    if m:
        verdict = m.group(1).upper()
        just = m.group(2).strip()
        prev_p = re.sub(r'<[^>]+>', ' ', uol_paras[i-1]).strip() if i > 0 else ''
        if len(just) < 50 and i + 1 < len(uol_paras):
            just += ' ' + re.sub(r'<[^>]+>', ' ', uol_paras[i+1]).strip()
        uol_checks.append({
            'veiculo': 'UOL Confere',
            'candidato': current_cand_uol,
            'declaracao': prev_p,
            'veredito_original': verdict,
            'justificativa': just,
            'paragrafo_bruto': clean_p
        })

print(f'UOL parsed checks: {len(uol_checks)}')

# ==========================================
# 3. PARSER ESTADÃO VERIFICA
# ==========================================
with open(os.path.join(raw_dir, 'estadao_verifica.html'), 'r', encoding='utf-8', errors='ignore') as f:
    est_html = f.read()

est_paras = re.findall(r'<p[^>]*>(.*?)</p>', est_html, re.S)
est_checks = []
current_cand_est = 'Desconhecido'

for i, p in enumerate(est_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'Flávio' in clean_p and len(clean_p) < 30:
        current_cand_est = 'Flávio Bolsonaro'
    elif 'Lula' in clean_p and len(clean_p) < 30:
        current_cand_est = 'Lula'
        
    # Estadão often writes: "O que disse o candidato: ... Como checamos: é verdadeiro / é falso / é enganoso"
    m = re.search(r'\bé\s+(verdadeiro|falso|enganoso|impreciso|exagerado)\b', clean_p, re.I)
    if m:
        verdict = m.group(1).capitalize()
        # Find statement
        prev_p = re.sub(r'<[^>]+>', ' ', est_paras[i-1]).strip() if i > 0 else ''
        est_checks.append({
            'veiculo': 'Estadão Verifica',
            'candidato': current_cand_est,
            'declaracao': prev_p,
            'veredito_original': verdict,
            'justificativa': clean_p,
            'paragrafo_bruto': clean_p
        })

print(f'Estadão parsed checks: {len(est_checks)}')

# ==========================================
# 4. PARSER AGÊNCIA LUPA
# ==========================================
with open(os.path.join(raw_dir, 'agencia_lupa.html'), 'r', encoding='utf-8', errors='ignore') as f:
    lupa_html = f.read()

lupa_paras = re.findall(r'<p[^>]*>(.*?)</p>', lupa_html, re.S)
lupa_checks = []
current_cand_lupa = 'Desconhecido'

for i, p in enumerate(lupa_paras):
    clean_p = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'Flávio Bolsonaro' in clean_p and len(clean_p) < 30:
        current_cand_lupa = 'Flávio Bolsonaro'
    elif 'Lula' in clean_p and len(clean_p) < 30:
        current_cand_lupa = 'Lula'
        
    # Lupa format:
    # "Citação do candidato"
    # Lupa label: VERDADEIRO / FALSO / EXAGERADO / CONTRADITÓRIO
    m = re.match(r'^(VERDADEIRO|FALSO|EXAGERADO|CONTRADITÓRIO|AINDA É CEDO PARA DIZER)$', clean_p, re.I)
    if m:
        verdict = m.group(1).upper()
        prev_p = re.sub(r'<[^>]+>', ' ', lupa_paras[i-1]).strip() if i > 0 else ''
        next_p = re.sub(r'<[^>]+>', ' ', lupa_paras[i+1]).strip() if i + 1 < len(lupa_paras) else ''
        lupa_checks.append({
            'veiculo': 'Agência Lupa',
            'candidato': current_cand_lupa,
            'declaracao': prev_p,
            'veredito_original': verdict,
            'justificativa': next_p,
            'paragrafo_bruto': clean_p
        })

print(f'Lupa parsed checks: {len(lupa_checks)}')

# Save debug JSON of parsed items
all_parsed = {
    'g1': g1_checks,
    'uol': uol_checks,
    'estadao': est_checks,
    'lupa': lupa_checks
}
with open(r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources\all_parsed_checks.json', 'w', encoding='utf-8') as f:
    json.dump(all_parsed, f, indent=2, ensure_ascii=False)
