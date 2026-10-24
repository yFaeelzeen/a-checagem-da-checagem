import os, sys, shutil, hashlib, json, time
sys.stdout.reconfigure(encoding='utf-8')

repo_dir = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'

subdirs = [
    '01_coleta_preservacao_bruta',
    '01_coleta_preservacao_bruta/verifiqueosfatos_com',
    '01_coleta_preservacao_bruta/pinoquio_live',
    '01_coleta_preservacao_bruta/verifiqueaverdade_com_br',
    '01_coleta_preservacao_bruta/flagcheck_com_br',
    '01_coleta_preservacao_bruta/checagemaovivo_org',
    '01_coleta_preservacao_bruta/portais_imprensa',
    '02_bases_dados_normalizadas',
    '03_auditoria_estrutural_e_fontes',
    '04_auditoria_portais_imprensa',
    '05_confronto_independentes_vs_portais',
    '06_relatorios_executivos_finais',
    'scripts'
]

for sd in subdirs:
    os.makedirs(os.path.join(repo_dir, sd), exist_ok=True)

print("Estrutura de diretórios criada com sucesso:")
for sd in subdirs:
    print(f"  + {sd}")
