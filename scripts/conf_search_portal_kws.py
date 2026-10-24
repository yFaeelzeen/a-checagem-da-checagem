import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

m4_ind_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\02_CHECAGENS_INDIVIDUAIS.json'
with open(m4_ind_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)

for kw in ['6x1', 'escala', 'feminicídio', 'mulheres', 'araras', 'serra']:
    matches = [p for p in portal_checks if kw in (p['declaracao'] + ' ' + p['tema'] + ' ' + p['justificativa']).lower()]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:3]:
        print(f"   [{m['veiculo']}] {m['candidato']} | Decl: {m['declaracao'][:60]} | Verd: {m['veredito_original']}")
