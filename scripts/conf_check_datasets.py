import os, sys, json, csv, re
sys.stdout.reconfigure(encoding='utf-8')

# Paths
m2_cat_path = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925\06_RELATORIOS_CONSOLIDADOS\catalogo_estruturado_checagens_consolidado.json'
m4_ind_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\02_CHECAGENS_INDIVIDUAIS.json'
m4_mat_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.json'

with open(m2_cat_path, 'r', encoding='utf-8') as f:
    indep_records = json.load(f)

with open(m4_ind_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)

with open(m4_mat_path, 'r', encoding='utf-8') as f:
    portal_matrix = json.load(f)

print(f"Independentes carregados: {len(indep_records)}")
print(f"Portais individuais carregados: {len(portal_checks)}")
print(f"Grupos da matriz de portais: {len(portal_matrix)}")

# Print breakdown of independentes
from collections import Counter
print("Distribuição independentes:", Counter(r['projeto_origem'] for r in indep_records))
print("Distribuição portais:", Counter(r['veiculo'] for r in portal_checks))
