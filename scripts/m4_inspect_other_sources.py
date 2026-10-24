import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

for fname, name in [
    ('uol_confere.html', 'UOL Confere'),
    ('estadao_verifica.html', 'Estadão Verifica'),
    ('agencia_lupa.html', 'Agência Lupa')
]:
    with open(os.path.join(raw_dir, fname), 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    print(f'=== Scanning {name} ===')
    # Clean tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.S)
    
    # Check for quotes and checks
    lines = [l.strip() for l in re.sub(r'<[^>]+>', '\n', text).splitlines() if l.strip()]
    print(f'Total text lines: {len(lines)}')
    
    # Look for candidate sections
    flavio_mentions = [i for i, l in enumerate(lines) if 'flávio' in l.lower() or 'bolsonaro' in l.lower()]
    lula_mentions = [i for i, l in enumerate(lines) if 'lula' in l.lower()]
    print(f'Lines mentioning Flavio/Bolsonaro: {len(flavio_mentions)}, Lula: {len(lula_mentions)}')
    
    # Look for verdicts in lines
    verdicts_found = []
    for l in lines:
        if any(w in l.lower() for w in ['verdadeiro', 'falso', 'fato', 'fake', 'impreciso', 'sem contexto', 'enganoso', 'não é bem assim', 'exagerado', 'contraditório']):
            if len(l) < 50:
                verdicts_found.append(l)
    print(f'Short lines with verdict words ({len(verdicts_found)}):', verdicts_found[:15])
