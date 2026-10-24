import os, sys, json, csv
sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'
in_json = os.path.join(out_dir, 'confronto_todas_382_checagens.json')

with open(in_json, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Export long format CSV (one row per comparison pair)
csv_rows = []
for r in records:
    ind_id = r['id']
    ind_proj = r['indep_projeto']
    ind_orig_id = r['indep_id_orig']
    cand = r['candidato']
    ind_quote = r['indep_declaracao']
    ind_verdict = r['indep_veredito']
    ind_just = r['indep_justificativa']
    status = r['status_pareamento']
    
    portais = r['portais_pareados']
    if not portais:
        csv_rows.append({
            'ID Checagem': ind_id,
            'Candidato': cand,
            'Site Independente (Origem)': ind_proj,
            'ID Independente': ind_orig_id,
            'O que foi falado (Independente)': ind_quote,
            'Classificação (Independente)': ind_verdict,
            'Justificativa (Independente)': ind_just[:300],
            'Status Pareamento': 'Exclusiva dos Independentes',
            'Grande Portal': 'Nenhum portal checou esta fala na amostra',
            'O que foi falado (Portal)': '-',
            'Classificação (Portal)': '-',
            'Justificativa (Portal)': '-'
        })
    else:
        for vname, pdata in portais.items():
            csv_rows.append({
                'ID Checagem': ind_id,
                'Candidato': cand,
                'Site Independente (Origem)': ind_proj,
                'ID Independente': ind_orig_id,
                'O que foi falado (Independente)': ind_quote,
                'Classificação (Independente)': ind_verdict,
                'Justificativa (Independente)': ind_just[:300],
                'Status Pareamento': 'Pareado em Grandes Portais',
                'Grande Portal': vname,
                'O que foi falado (Portal)': pdata['declaracao'],
                'Classificação (Portal)': pdata['veredito'],
                'Justificativa (Portal)': pdata['justificativa'][:300]
            })

out_csv = os.path.join(out_dir, 'confronto_todas_382_checagens.csv')
with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
    fieldnames = [
        'ID Checagem', 'Candidato', 'Site Independente (Origem)', 'ID Independente',
        'O que foi falado (Independente)', 'Classificação (Independente)', 'Justificativa (Independente)',
        'Status Pareamento', 'Grande Portal', 'O que foi falado (Portal)',
        'Classificação (Portal)', 'Justificativa (Portal)'
    ]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(csv_rows)

print(f"Exportado confronto_todas_382_checagens.csv com {len(csv_rows)} linhas de comparação.")
