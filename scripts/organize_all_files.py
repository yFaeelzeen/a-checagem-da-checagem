import os, sys, shutil, hashlib, json
sys.stdout.reconfigure(encoding='utf-8')

repo_dir = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'
dossie_m2 = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
dossie_m3 = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
dossie_m4 = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'
dossie_confronto = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'

def copy_file(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

def copy_tree(src, dst):
    if os.path.exists(src):
        for root, dirs, files in os.walk(src):
            for f in files:
                src_file = os.path.join(root, f)
                rel_path = os.path.relpath(src_file, src)
                dst_file = os.path.join(dst, rel_path)
                copy_file(src_file, dst_file)

print("1. Copiando Preservações Brutas (01_coleta_preservacao_bruta)...")
# Verifique os Fatos
copy_tree(os.path.join(dossie_m2, '00_ORIGINAIS_VERIFIQUE_OS_FATOS', 'raw_site'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'verifiqueosfatos_com'))
copy_tree(os.path.join(dossie_m2, '00_ORIGINAIS_VERIFIQUE_OS_FATOS', 'git_objects'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'verifiqueosfatos_com', 'git_objects'))

# Pinóquio.live
copy_tree(os.path.join(dossie_m2, '02_PINOQUIO_LIVE', 'raw_site'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'pinoquio_live'))

# Verifique a Verdade
copy_tree(os.path.join(dossie_m2, '04_VERIFIQUE_A_VERDADE', 'raw_site'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'verifiqueaverdade_com_br'))

# FlagCheck
copy_tree(os.path.join(dossie_m2, '01_FLAGCHECK', 'raw_site'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'flagcheck_com_br'))

# Checagem ao Vivo
copy_tree(os.path.join(dossie_m2, '03_CHECAGEM_AO_VIVO', 'raw_site'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'checagemaovivo_org'))

# Portais de Imprensa
copy_tree(os.path.join(dossie_m4, 'raw_sources'),
          os.path.join(repo_dir, '01_coleta_preservacao_bruta', 'portais_imprensa'))

print("2. Copiando Bases de Dados Normalizadas (02_bases_dados_normalizadas)...")
# Catálogo consolidado dos independentes
copy_file(os.path.join(dossie_m2, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.csv'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'catalogo_independentes_383_checagens.csv'))
copy_file(os.path.join(dossie_m2, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'catalogo_independentes_383_checagens.json'))

# Catálogo individual dos grandes portais
copy_file(os.path.join(dossie_m4, '02_CHECAGENS_INDIVIDUAIS.csv'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'catalogo_portais_219_checagens.csv'))
copy_file(os.path.join(dossie_m4, '02_CHECAGENS_INDIVIDUAIS.json'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'catalogo_portais_219_checagens.json'))

# Checagens individuais exportadas específicas
copy_file(os.path.join(dossie_m2, '00_ORIGINAIS_VERIFIQUE_OS_FATOS', 'data_exported', 'checagens_completas.csv'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'verifiqueosfatos_75_checagens.csv'))
copy_file(os.path.join(dossie_m2, '02_PINOQUIO_LIVE', 'data_exported', 'checagens_globo_2026.csv'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'pinoquio_live_175_checagens.csv'))
copy_file(os.path.join(dossie_m2, '04_VERIFIQUE_A_VERDADE', 'data_exported', 'artigos_checagem_globo.csv'),
          os.path.join(repo_dir, '02_bases_dados_normalizadas', 'verifiqueaverdade_132_checagens.csv'))

print("3. Copiando Auditoria Estrutural e Fontes (03_auditoria_estrutural_e_fontes)...")
m3_files = [
    ('01_AUDITORIA_ESTRUTURAL.md', '01_auditoria_estrutural.md'),
    ('01_AUDITORIA_ESTRUTURAL.json', '01_auditoria_estrutural.json'),
    ('01_DUPLICATAS_E_CAMPOS_AUSENTES.csv', '01_duplicatas_e_campos_ausentes.csv'),
    ('03_AUDITORIA_DAS_FONTES.md', '03_auditoria_das_fontes.md'),
    ('03_INVENTARIO_DE_FONTES.csv', '03_inventario_de_fontes.csv'),
    ('04_CONSISTENCIA_METODOLOGICA.md', '04_consistencia_metodologica.md'),
    ('04_DISTRIBUICAO_DE_VEREDITOS.csv', '04_distribuicao_de_vereditos.csv'),
    ('05_INDICE_DE_EVIDENCIAS.csv', '05_indice_de_evidencias.csv')
]
for src_name, dst_name in m3_files:
    copy_file(os.path.join(dossie_m3, src_name), os.path.join(repo_dir, '03_auditoria_estrutural_e_fontes', dst_name))

print("4. Copiando Auditoria dos Portais (04_auditoria_portais_imprensa)...")
m4_files = [
    ('00_LEIA_ME_METODOLOGIA.md', 'metodologia_portais.md'),
    ('01_INVENTARIO_QUATRO_PUBLICACOES.csv', '01_inventario_quatro_publicacoes.csv'),
    ('01_INVENTARIO_QUATRO_PUBLICACOES.json', '01_inventario_quatro_publicacoes.json'),
    ('04_DIVERGENCIAS_E_CONCORDANCIAS.md', '04_divergencias_e_concordancias_portais.md'),
    ('05_CONSISTENCIA_EDITORIAL_LULA_FLAVIO.md', '05_consistencia_editorial_portais.md'),
    ('06_LACUNAS_E_LIMITACOES.md', '06_lacunas_e_limitacoes_portais.md')
]
for src_name, dst_name in m4_files:
    copy_file(os.path.join(dossie_m4, src_name), os.path.join(repo_dir, '04_auditoria_portais_imprensa', dst_name))

print("5. Copiando Confrontos Independentes vs Portais (05_confronto_independentes_vs_portais)...")
conf_files = [
    ('CONFRONTO_EXAUSTIVO_382_DECLARACOES.md', 'confronto_exaustivo_382_declaracoes.md'),
    ('confronto_todas_382_checagens.csv', 'confronto_todas_382_checagens.csv'),
    ('confronto_todas_382_checagens.json', 'confronto_todas_382_checagens.json'),
    ('matriz_confronto_independentes_vs_portais.csv', 'matriz_confronto_20_casos_chave.csv'),
    ('matriz_confronto_independentes_vs_portais.json', 'matriz_confronto_20_casos_chave.json')
]
for src_name, dst_name in conf_files:
    copy_file(os.path.join(dossie_confronto, src_name), os.path.join(repo_dir, '05_confronto_independentes_vs_portais', dst_name))

# Matriz da Missão 3 de 15 casos
copy_file(os.path.join(dossie_m3, '02_MATRIZ_COMPARATIVA.csv'),
          os.path.join(repo_dir, '05_confronto_independentes_vs_portais', 'matriz_comparativa_independentes_15_casos.csv'))

print("6. Copiando Relatórios Executivos Finais (06_relatorios_executivos_finais)...")
copy_file(os.path.join(dossie_confronto, 'RELATORIO_AUDITORIA_INDEPENDENTES_VS_PORTAIS.md'),
          os.path.join(repo_dir, '06_relatorios_executivos_finais', 'relatorio_confronto_independentes_vs_portais.md'))
copy_file(os.path.join(dossie_m4, '07_RELATORIO_EXECUTIVO_FINAL.md'),
          os.path.join(repo_dir, '06_relatorios_executivos_finais', 'relatorio_executivo_portais_imprensa.md'))
copy_file(os.path.join(dossie_m3, 'RELATORIO_FINAL_AUDITORIA_INDEPENDENTE.md'),
          os.path.join(repo_dir, '06_relatorios_executivos_finais', 'relatorio_executivo_checadores_independentes.md'))

print("7. Copiando Scripts de Análise e Processamento (scripts)...")
# Collect scripts from all mission folders
scripts_to_copy = [
    (os.path.join(dossie_m3, 'scripts'), 'm3_'),
    (os.path.join(dossie_m4, 'scripts'), 'm4_'),
    (os.path.join(dossie_confronto, 'scripts'), 'conf_')
]
for sdir, prefix in scripts_to_copy:
    if os.path.exists(sdir):
        for f in os.listdir(sdir):
            if f.endswith('.py'):
                copy_file(os.path.join(sdir, f), os.path.join(repo_dir, 'scripts', f"{prefix}{f}"))

print("Organização de cópia concluída com sucesso!")
