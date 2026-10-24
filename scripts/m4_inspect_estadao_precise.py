import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'estadao_verifica.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# In Estadão AMP:
# Look for sections with headings, candidate names, and verdict statements
# Often format:
# <h3>Obras paralisadas</h3>
# <p>O que disse Flávio Bolsonaro: "..."</p>
# <p>O que checamos: é verdadeiro/falso...</p>

blocks = re.findall(r'<h[23][^>]*>(.*?)</h[23]>(.*?)(?=<h[23]|$)', html, re.S)
print(f'Estadão h2/h3 blocks: {len(blocks)}')

estadao_items = []
current_cand = 'Desconhecido'

for heading, body in blocks:
    clean_h = re.sub(r'<[^>]+>', ' ', heading).strip()
    if 'Lula' in clean_h and ('PT' in clean_h or len(clean_h) < 15):
        current_cand = 'Lula'
        continue
    elif 'Flávio' in clean_h and ('PL' in clean_h or len(clean_h) < 20):
        current_cand = 'Flávio Bolsonaro'
        continue
        
    # Check if body has verdict
    m_verd = re.search(r'(é|O Estadão Verifica checou que é)\s+(verdadeiro|falso|enganoso|impreciso|exagerado|sem contexto)', body, re.I)
    if m_verd:
        verdict = m_verd.group(2).capitalize()
        # Find quote / what was said
        m_quote = re.search(r'(O que disse[^:]*:|O candidato disse[^:]*:?)(.*?)(?=(Como checamos|O que checamos|<p>é|$))', body, re.S | re.I)
        claim = ''
        if m_quote:
            claim = re.sub(r'<[^>]+>', ' ', m_quote.group(2)).strip()
        else:
            # take first paragraph
            p_first = re.search(r'<p[^>]*>(.*?)</p>', body, re.S)
            if p_first:
                claim = re.sub(r'<[^>]+>', ' ', p_first.group(1)).strip()
                
        # Find explanation
        m_just = re.search(r'(Como checamos[^:]*:|O que checamos[^:]*:)(.*)', body, re.S | re.I)
        just = ''
        if m_just:
            just = re.sub(r'<[^>]+>', ' ', m_just.group(2)).strip()
        else:
            just = re.sub(r'<[^>]+>', ' ', body).strip()
            
        estadao_items.append({
            'id': f'est_{len(estadao_items)+1:02d}',
            'tema': clean_h,
            'candidato': current_cand,
            'veredito': verdict,
            'declaracao': claim,
            'justificativa': just[:500]
        })

print(f'Estadão parsed items: {len(estadao_items)}')
for it in estadao_items[:5]:
    print(f"[{it['id']}] Cand: {it['candidato']} | Tema: {it['tema']} | Verd: {it['veredito']} | Decl: {it['declaracao'][:60]}...")
