import os, sys, json, csv
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
cat_json = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925\06_RELATORIOS_CONSOLIDADOS\catalogo_estruturado_checagens_consolidado.json'

with open(cat_json, 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by project and candidate
stats = {}
for it in items:
    proj = it['projeto_origem']
    cand = it['candidato_original']
    verd = it['veredito_original']
    
    if proj not in stats:
        stats[proj] = {}
    if cand not in stats[proj]:
        stats[proj][cand] = {}
    stats[proj][cand][verd] = stats[proj][cand].get(verd, 0) + 1

# Generate CSV rows
csv_rows = []
for proj, cands in stats.items():
    for cand, verdicts in cands.items():
        total_cand = sum(verdicts.values())
        for verd, cnt in sorted(verdicts.items()):
            pct = (cnt / total_cand) * 100
            csv_rows.append({
                'Projeto': proj,
                'Candidato': cand,
                'Veredito Original': verd,
                'Quantidade': cnt,
                'Total Candidato no Projeto': total_cand,
                'Percentual': f'{pct:.2f}%'
            })

out_csv = os.path.join(target_dir, '04_DISTRIBUICAO_DE_VEREDITOS.csv')
with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Projeto', 'Candidato', 'Veredito Original', 'Quantidade', 'Total Candidato no Projeto', 'Percentual'])
    for r in csv_rows:
        w.writerow([r['Projeto'], r['Candidato'], r['Veredito Original'], r['Quantidade'], r['Total Candidato no Projeto'], r['Percentual']])

print(f'Wrote 04_DISTRIBUICAO_DE_VEREDITOS.csv with {len(csv_rows)} distribution records.')
for proj, cands in stats.items():
    print(f'=== {proj} ===')
    for cand, v in cands.items():
        print(f'  {cand} (Total {sum(v.values())}): {v}')
