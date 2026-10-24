import os, sys, json, csv
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'
out_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'

with open(os.path.join(raw_dir, 'manifesto_fontes_autorizadas.json'), 'r', encoding='utf-8') as f:
    manifest = json.load(f)

with open(os.path.join(out_dir, '02_CHECAGENS_INDIVIDUAIS.json'), 'r', encoding='utf-8') as f:
    checks = json.load(f)

# Count checks per vehicle and candidate
counts = {}
for c in checks:
    v = c['veiculo']
    cand = c['candidato']
    if v not in counts:
        counts[v] = {'total': 0, 'Lula': 0, 'Flávio Bolsonaro': 0}
    counts[v]['total'] += 1
    if cand == 'Lula':
        counts[v]['Lula'] += 1
    else:
        counts[v]['Flávio Bolsonaro'] += 1

inventory_records = []
for k, m in manifest.items():
    vname = m['veiculo']
    cinfo = counts.get(vname, {'total': 0, 'Lula': 0, 'Flávio Bolsonaro': 0})
    inventory_records.append({
        'id_veiculo': k,
        'veiculo': vname,
        'url_autorizada': m['url_autorizada'],
        'status_http': m['status_acesso'],
        'metodo_recuperacao': m['metodo_recuperacao'],
        'tamanho_bytes': m['tamanho_bytes'],
        'sha256': m['sha256'],
        'data_coleta': m['timestamp_coleta'],
        'total_checagens_recuperadas': cinfo['total'],
        'checagens_lula': cinfo['Lula'],
        'checagens_flavio': cinfo['Flávio Bolsonaro'],
        'arquivo_local_bruto': m['arquivo_local'],
        'situacao_acesso': 'Acesso bem-sucedido (HTML preservado)'
    })

# Write CSV
inv_csv = os.path.join(out_dir, '01_INVENTARIO_QUATRO_PUBLICACOES.csv')
with open(inv_csv, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow([
        'ID Veículo', 'Veículo', 'URL Autorizada', 'Status HTTP', 'Método de Recuperação',
        'Tamanho Bytes', 'SHA-256', 'Data Coleta', 'Total Checagens',
        'Checagens Lula', 'Checagens Flávio', 'Arquivo Local Bruto', 'Situação Acesso'
    ])
    for r in inventory_records:
        w.writerow([
            r['id_veiculo'], r['veiculo'], r['url_autorizada'], r['status_http'], r['metodo_recuperacao'],
            r['tamanho_bytes'], r['sha256'], r['data_coleta'], r['total_checagens_recuperadas'],
            r['checagens_lula'], r['checagens_flavio'], r['arquivo_local_bruto'], r['situacao_acesso']
        ])

# Write JSON
inv_json = os.path.join(out_dir, '01_INVENTARIO_QUATRO_PUBLICACOES.json')
with open(inv_json, 'w', encoding='utf-8') as f:
    json.dump(inventory_records, f, indent=2, ensure_ascii=False)

print('Successfully exported 01_INVENTARIO_QUATRO_PUBLICACOES.csv and .json')
