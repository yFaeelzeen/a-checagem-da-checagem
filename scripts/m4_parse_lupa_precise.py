import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'agencia_lupa.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Pattern for Lupa labels:
# <div class="block-text">\s*<strong>(VERDADEIRO|FALSO|EXAGERADO|CONTRADITÓRIO|INSUSTENTÁVEL)</strong>\s*</div>
pattern = r'<div class="block-text">\s*<strong>(.*?)</strong>\s*</div>'
matches = list(re.finditer(pattern, html, re.I | re.S))
print(f'Lupa custom-block matches: {len(matches)}')

lupa_checks = []
for idx, m in enumerate(matches):
    verdict = m.group(1).strip()
    pos = m.start()
    
    # Extract preceding text (declaration)
    pre_html = html[max(0, pos-2000):pos]
    # find all <p> in pre_html
    pre_paras = re.findall(r'<p[^>]*>(.*?)</p>', pre_html, re.S)
    declaration = ''
    if pre_paras:
        # Last paragraph before the badge is the quote
        declaration = re.sub(r'<[^>]+>', ' ', pre_paras[-1]).strip()
        
    # Extract following text (justification)
    post_html = html[m.end():min(len(html), m.end()+2500)]
    post_paras = re.findall(r'<p[^>]*>(.*?)</p>', post_html, re.S)
    justification = ''
    if post_paras:
        justification = ' '.join(re.sub(r'<[^>]+>', ' ', p).strip() for p in post_paras[:2])
        
    # Candidate determination
    candidate = 'Indeterminado'
    decl_lower = declaration.lower()
    if 'lula' in decl_lower and 'flávio' not in decl_lower:
        candidate = 'Lula'
    elif 'flávio' in decl_lower or 'bolsonaro' in decl_lower:
        candidate = 'Flávio Bolsonaro'
    else:
        # Check surrounding text
        surrounding = (declaration + ' ' + justification).lower()
        if 'lula' in surrounding and 'flávio' not in surrounding:
            candidate = 'Lula'
        elif 'flávio' in surrounding or 'bolsonaro' in surrounding:
            candidate = 'Flávio Bolsonaro'

    lupa_checks.append({
        'id': f'lupa_{idx+1:02d}',
        'veiculo': 'Agência Lupa',
        'candidato': candidate,
        'declaracao': declaration,
        'veredito_original': verdict,
        'justificativa': justification
    })

print(f'Parsed {len(lupa_checks)} checks from Agência Lupa.')
for c in lupa_checks[:5]:
    print(f"[{c['id']}] Cand: {c['candidato']} | Verd: {c['veredito_original']} | Decl: {c['declaracao'][:80]}...")
