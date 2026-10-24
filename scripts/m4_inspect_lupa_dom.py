import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'agencia_lupa.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's see some occurrences of 'verdadeiro' or 'falso'
for m in re.finditer(r'(verdadeiro|falso|exagerado|contraditório|insustentável)', html, re.I):
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 250)
    snippet = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html[start:end]))
    print('LUPA SNIPPET:', snippet)
    print('-'*50)
    if m.start() > 50000:
        break
