import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'g1_fato_ou_fake.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Look for patterns like:
# O que diz <Candidato>: "..."
# A fala é #FATO / #FAKE / #NÃOÉBEMASSIM
# ou parágrafos com #FATO, #FAKE

matches = re.findall(r'(#FATO|#FAKE|#NÃOÉBEMASSIM|#NÃO É BEM ASSIM)', html, re.I)
print('G1 hashtags found:', len(matches))
print('Unique hashtags:', set(matches))

# Let's see some context around each hashtag
snippets = []
for m in re.finditer(r'(#FATO|#FAKE|#NÃOÉBEMASSIM|#NÃO É BEM ASSIM)', html, re.I):
    start = max(0, m.start() - 250)
    end = min(len(html), m.end() + 500)
    snippet = html[start:end]
    clean_snip = re.sub(r'<[^>]+>', ' ', snippet)
    clean_snip = ' '.join(clean_snip.split())
    snippets.append((m.group(0), clean_snip))

print(f'Total snippets: {len(snippets)}')
for idx, (tag, s) in enumerate(snippets[:10]):
    print(f'--- G1 ITEM {idx+1} [{tag}] ---')
    print(s[:250])
