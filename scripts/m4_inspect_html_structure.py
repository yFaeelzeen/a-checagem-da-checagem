import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

for fname, name in [
    ('g1_fato_ou_fake.html', 'G1 — Fato ou Fake'),
    ('uol_confere.html', 'UOL Confere'),
    ('estadao_verifica.html', 'Estadão Verifica'),
    ('agencia_lupa.html', 'Agência Lupa')
]:
    with open(os.path.join(raw_dir, fname), 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    print(f'=== {name} ({fname}) ===')
    # Title
    t_match = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
    print('Title:', t_match.group(1).strip() if t_match else 'None')
    
    # Check for headings or bold statements
    h2s = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', html, re.I | re.S)
    print(f'Headings count: {len(h2s)}')
    for h in h2s[:8]:
        clean_h = re.sub(r'<[^>]+>', '', h).strip()
        if clean_h:
            print('  H:', clean_h[:100])
            
    # Check for verdict keywords
    v_falso = len(re.findall(r'\b(falso|fake)\b', html, re.I))
    v_verd = len(re.findall(r'\b(fato|verdadeiro|verdade)\b', html, re.I))
    print(f'Occurrences: falso/fake={v_falso}, fato/verdadeiro={v_verd}')
