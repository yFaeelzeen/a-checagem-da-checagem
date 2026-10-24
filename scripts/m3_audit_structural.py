import os, sys, json, csv, hashlib
sys.stdout.reconfigure(encoding='utf-8')

m2_root = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
cat_csv = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.csv')
cat_json = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json')
inv_json = os.path.join(m2_root, '05_INVENTARIO_GERAL', 'inventario_consolidado_geral.json')

# 1. Inspect CSV lines
with open(cat_csv, 'r', encoding='utf-8-sig') as f:
    csv_lines = f.readlines()
print(f'CSV total lines (including header): {len(csv_lines)}')

reader = csv.DictReader(csv_lines)
csv_rows = list(reader)
print(f'CSV total data records: {len(csv_rows)}')

# 2. Inspect JSON records
with open(cat_json, 'r', encoding='utf-8') as f:
    json_rows = json.load(f)
print(f'JSON total data records: {len(json_rows)}')

# 3. Counts by project
proj_counts_csv = {}
for r in csv_rows:
    p = r['Projeto de Origem']
    proj_counts_csv[p] = proj_counts_csv.get(p, 0) + 1
print('CSV counts by project:', proj_counts_csv)

proj_counts_json = {}
for r in json_rows:
    p = r['projeto_origem']
    proj_counts_json[p] = proj_counts_json.get(p, 0) + 1
print('JSON counts by project:', proj_counts_json)

# 4. Check for duplicate IDs per project
ids_by_proj = {}
duplicates = []
for idx, r in enumerate(csv_rows):
    p = r['Projeto de Origem']
    pid = r['ID Original']
    if p not in ids_by_proj:
        ids_by_proj[p] = {}
    if pid in ids_by_proj[p]:
        duplicates.append({'project': p, 'id': pid, 'first_row': ids_by_proj[p][pid], 'dup_row': idx+2})
    else:
        ids_by_proj[p][pid] = idx + 2
print('ID duplicates found:', len(duplicates))

# 5. Missing / empty critical fields
empty_fields = []
for idx, r in enumerate(csv_rows):
    row_num = idx + 2
    for field, val in r.items():
        if not val or not val.strip():
            # some fields are optional, e.g., 'Correção', 'Afirmação Resumida'
            empty_fields.append({'row': row_num, 'project': r['Projeto de Origem'], 'id': r['ID Original'], 'field': field})

print('Total empty field instances:', len(empty_fields))
empty_by_field = {}
for ef in empty_fields:
    empty_by_field[ef['field']] = empty_by_field.get(ef['field'], 0) + 1
print('Empty counts by field:', empty_by_field)

# 6. Check files in 00_ORIGINAIS_VERIFIQUE_OS_FATOS
vof_dir = os.path.join(m2_root, '00_ORIGINAIS_VERIFIQUE_OS_FATOS')
vof_files = []
for root, dirs, files in os.walk(vof_dir):
    for fn in files:
        vof_files.append(os.path.relpath(os.path.join(root, fn), vof_dir))
print(f'Total actual files in 00_ORIGINAIS_VERIFIQUE_OS_FATOS: {len(vof_files)}')
