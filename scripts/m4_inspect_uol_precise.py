import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

with open(os.path.join(raw_dir, 'uol_confere.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# UOL structure:
# Statements are preceded by bold headers or quotes, then "O que disse:", "Por que é falso/enganoso/verdadeiro:"
# Let's inspect all <p> in article body
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.S)
print(f'Total UOL paras: {len(paras)}')

uol_items = []
current_candidate = 'Desconhecido'

for idx, p in enumerate(paras):
    clean = re.sub(r'<[^>]+>', ' ', p).strip()
    if 'Flávio Bolsonaro' in clean and len(clean) < 30:
        current_candidate = 'Flávio Bolsonaro'
    elif 'Lula' in clean and len(clean) < 30:
        current_candidate = 'Lula'
        
    m = re.match(r'^(FALSO|ENGANOSO|VERDADEIRO|IMPRECISO|SEM CONTEXTO)\.?(.*)', clean, re.I)
    if m:
        verdict = m.group(1).upper()
        just = m.group(2).strip()
        # Look back up to 3 paragraphs for the claim
        claim = ''
        for back in range(1, 4):
            if idx - back >= 0:
                cand_claim = re.sub(r'<[^>]+>', ' ', paras[idx - back]).strip()
                if cand_claim and not any(cand_claim.startswith(v) for v in ['FALSO', 'ENGANOSO', 'VERDADEIRO', 'IMPRECISO']):
                    claim = cand_claim
                    break
        
        # Look forward for explanation if short
        if len(just) < 100 and idx + 1 < len(paras):
            just += ' ' + re.sub(r'<[^>]+>', ' ', paras[idx + 1]).strip()
            
        uol_items.append({
            'id': f'uol_{len(uol_items)+1:02d}',
            'candidato': current_candidate,
            'veredito': verdict,
            'declaracao': claim,
            'justificativa': just
        })

print(f'UOL parsed items: {len(uol_items)}')
for u in uol_items[:5]:
    print(f"[{u['id']}] Cand: {u['candidato']} | Verd: {u['veredito']} | Decl: {u['declaracao'][:70]}...")
