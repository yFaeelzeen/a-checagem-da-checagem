import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

REPO = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'

def main():
    print("=== SIMPLIFICAÇÃO E RENOMEAÇÃO DE PASTAS E ARQUIVOS ===")
    
    # 1. Folders mapping
    # 01_coleta_preservacao_bruta -> coleta
    old_coleta = os.path.join(REPO, '01_coleta_preservacao_bruta')
    new_coleta = os.path.join(REPO, 'coleta')
    if os.path.exists(old_coleta) and not os.path.exists(new_coleta):
        os.rename(old_coleta, new_coleta)
        print("Renomeada pasta: 01_coleta_preservacao_bruta -> coleta")
        
    # Simplify subfolders inside coleta
    coleta_subs = {
        'checagemaovivo_org': 'checagemaovivo',
        'flagcheck_com_br': 'flagcheck',
        'pinoquio_live': 'pinoquio',
        'portais_imprensa': 'portais',
        'verifiqueaverdade_com_br': 'verifiqueaverdade',
        'verifiqueosfatos_com': 'verifiqueosfatos'
    }
    for old_sub, new_sub in coleta_subs.items():
        op = os.path.join(new_coleta, old_sub)
        np = os.path.join(new_coleta, new_sub)
        if os.path.exists(op) and not os.path.exists(np):
            os.rename(op, np)
            print(f"  coleta/{old_sub} -> coleta/{new_sub}")

    # 2. 02_bases_dados_normalizadas -> dados
    old_dados = os.path.join(REPO, '02_bases_dados_normalizadas')
    new_dados = os.path.join(REPO, 'dados')
    if os.path.exists(old_dados) and not os.path.exists(new_dados):
        os.rename(old_dados, new_dados)
        print("Renomeada pasta: 02_bases_dados_normalizadas -> dados")
        
    # Rename files in dados
    dados_files = {
        'catalogo_independentes_400_checagens_globo_atualizado.csv': 'independentes_globo.csv',
        'catalogo_independentes_400_checagens_globo_atualizado.json': 'independentes_globo.json',
        'catalogo_independentes_383_checagens.csv': 'independentes_globo_v1.csv',
        'catalogo_independentes_383_checagens.json': 'independentes_globo_v1.json',
        'catalogo_portais_219_checagens.csv': 'portais_globo.csv',
        'catalogo_portais_219_checagens.json': 'portais_globo.json',
        'pinoquio_live_175_checagens.csv': 'pinoquio_globo.csv',
        'verifiqueosfatos_75_checagens.csv': 'verifiqueosfatos_globo.csv',
        'verifiqueaverdade_132_checagens.csv': 'verifiqueaverdade_globo_v1.csv',
        'verifiqueaverdade_globo_149_checagens.csv': 'verifiqueaverdade_globo.csv',
        'verifiqueaverdade_globo_149_checagens.json': 'verifiqueaverdade_globo.json',
        'verifiqueaverdade_band_107_checagens.csv': 'verifiqueaverdade_band.csv',
        'verifiqueaverdade_band_107_checagens.json': 'verifiqueaverdade_band.json',
        'verifiqueaverdade_total_256_checagens.csv': 'verifiqueaverdade_total.csv',
        'verifiqueaverdade_total_256_checagens.json': 'verifiqueaverdade_total.json'
    }
    for of, nf in dados_files.items():
        op = os.path.join(new_dados, of)
        np = os.path.join(new_dados, nf)
        if os.path.exists(op):
            if os.path.exists(np) and op != np:
                os.remove(np)
            os.rename(op, np)
            print(f"  dados/{of} -> dados/{nf}")

    # 3. Combine 03_auditoria_estrutural_e_fontes and 04_auditoria_portais_imprensa -> auditoria
    new_audit = os.path.join(REPO, 'auditoria')
    os.makedirs(new_audit, exist_ok=True)
    
    old_a1 = os.path.join(REPO, '03_auditoria_estrutural_e_fontes')
    old_a2 = os.path.join(REPO, '04_auditoria_portais_imprensa')
    
    audit_files_map = {
        '01_auditoria_estrutural.md': 'auditoria_estrutural.md',
        '01_auditoria_estrutural.json': 'auditoria_estrutural.json',
        '01_duplicatas_e_campos_ausentes.csv': 'duplicatas_e_lacunas.csv',
        '03_auditoria_das_fontes.md': 'fontes_analise.md',
        '03_inventario_de_fontes.csv': 'fontes_inventario.csv',
        '04_consistencia_metodologica.md': 'metodologia_independentes.md',
        '04_distribuicao_de_vereditos.csv': 'distribuicao_vereditos.csv',
        '05_indice_de_evidencias.csv': 'indice_evidencias.csv',
        'metodologia_oficial_verifique_a_verdade.md': 'metodologia_verifiqueaverdade.md',
        'verifique_a_verdade_17_novas_checagens.json': 'novas_checagens_verifiqueaverdade.json'
    }
    if os.path.exists(old_a1):
        for of, nf in audit_files_map.items():
            op = os.path.join(old_a1, of)
            np = os.path.join(new_audit, nf)
            if os.path.exists(op):
                if os.path.exists(np) and op != np:
                    os.remove(np)
                shutil.move(op, np)
                print(f"  auditoria/{nf} (vindo de 03/{of})")
        # Remove old dir if empty
        try:
            os.rmdir(old_a1)
            print("Removida pasta antiga: 03_auditoria_estrutural_e_fontes")
        except:
            pass

    portais_audit_map = {
        '01_inventario_quatro_publicacoes.csv': 'portais_inventario.csv',
        '01_inventario_quatro_publicacoes.json': 'portais_inventario.json',
        '04_divergencias_e_concordancias_portais.md': 'portais_divergencias.md',
        '05_consistencia_editorial_portais.md': 'portais_consistencia.md',
        '06_lacunas_e_limitacoes_portais.md': 'portais_lacunas.md',
        'metodologia_portais.md': 'portais_metodologia.md'
    }
    if os.path.exists(old_a2):
        for of, nf in portais_audit_map.items():
            op = os.path.join(old_a2, of)
            np = os.path.join(new_audit, nf)
            if os.path.exists(op):
                if os.path.exists(np) and op != np:
                    os.remove(np)
                shutil.move(op, np)
                print(f"  auditoria/{nf} (vindo de 04/{of})")
        try:
            os.rmdir(old_a2)
            print("Removida pasta antiga: 04_auditoria_portais_imprensa")
        except:
            pass

    # 4. 05_confronto_independentes_vs_portais -> confronto
    old_conf = os.path.join(REPO, '05_confronto_independentes_vs_portais')
    new_conf = os.path.join(REPO, 'confronto')
    if os.path.exists(old_conf) and not os.path.exists(new_conf):
        os.rename(old_conf, new_conf)
        print("Renomeada pasta: 05_confronto_independentes_vs_portais -> confronto")
        
    confronto_files = {
        'confronto_exaustivo_399_declaracoes.md': 'confronto_declaracoes.md',
        'confronto_todas_399_checagens.csv': 'confronto_dados.csv',
        'confronto_todas_399_checagens.json': 'confronto_dados.json',
        'matriz_confronto_20_casos_chave.csv': 'confronto_20_casos.csv',
        'matriz_confronto_20_casos_chave.json': 'confronto_20_casos.json',
        'matriz_comparativa_independentes_15_casos.csv': 'confronto_15_casos_independentes.csv',
        'confronto_exaustivo_382_declaracoes.md': 'confronto_declaracoes_v1.md',
        'confronto_todas_382_checagens.csv': 'confronto_dados_v1.csv',
        'confronto_todas_382_checagens.json': 'confronto_dados_v1.json'
    }
    for of, nf in confronto_files.items():
        op = os.path.join(new_conf, of)
        np = os.path.join(new_conf, nf)
        if os.path.exists(op):
            if os.path.exists(np) and op != np:
                os.remove(np)
            os.rename(op, np)
            print(f"  confronto/{of} -> confronto/{nf}")

    # 5. 06_relatorios_executivos_finais -> relatorios
    old_rel = os.path.join(REPO, '06_relatorios_executivos_finais')
    new_rel = os.path.join(REPO, 'relatorios')
    if os.path.exists(old_rel) and not os.path.exists(new_rel):
        os.rename(old_rel, new_rel)
        print("Renomeada pasta: 06_relatorios_executivos_finais -> relatorios")
        
    rel_files = {
        'relatorio_confronto_independentes_vs_portais.md': 'relatorio_confronto.md',
        'relatorio_executivo_checadores_independentes.md': 'relatorio_independentes.md',
        'relatorio_executivo_portais_imprensa.md': 'relatorio_portais.md',
        'relatorio_extracao_completa_verifiqueaverdade.md': 'relatorio_verifiqueaverdade.md'
    }
    for of, nf in rel_files.items():
        op = os.path.join(new_rel, of)
        np = os.path.join(new_rel, nf)
        if os.path.exists(op):
            if os.path.exists(np) and op != np:
                os.remove(np)
            os.rename(op, np)
            print(f"  relatorios/{of} -> relatorios/{nf}")

    # 6. Rename root hash file to SHA256_HASHES.txt
    old_hash = os.path.join(REPO, 'SHA256_ARTEFATOS_REPOSITORIO.txt')
    new_hash = os.path.join(REPO, 'SHA256_HASHES.txt')
    if os.path.exists(old_hash):
        if os.path.exists(new_hash):
            os.remove(new_hash)
        os.rename(old_hash, new_hash)
        print("Renomeado: SHA256_ARTEFATOS_REPOSITORIO.txt -> SHA256_HASHES.txt")

if __name__ == '__main__':
    main()
