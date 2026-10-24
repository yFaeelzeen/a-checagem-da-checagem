import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'agencia_lupa.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect tags around EXAGERADO
idx = html.find('EXAGERADO')
if idx != -1:
    print('Raw surrounding HTML:\n', html[idx-200:idx+400])
