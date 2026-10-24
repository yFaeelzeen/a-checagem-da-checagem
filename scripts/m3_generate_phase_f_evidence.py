import os, sys, json, csv, hashlib
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'

# 1. Build 05_INDICE_DE_EVIDENCIAS.csv
# Maps every audited conclusion to exact local files, IDs and URLs
with open(os.path.join(target_dir, '02_MATRIZ_COMPARATIVA.json'), 'r', encoding='utf-8') as f:
    cases = json.load(f)

evidence_rows = []
for c in cases:
    evidence_rows.append({
        'id_caso': c['id_caso'],
        'tema': c['tema'],
        'candidato': c['candidato'],
        'conclusao_auditada': c['avaliacao_independente'],
        'grau_confianca': c['confianca'],
        'arquivo_local_suporte': '02_MATRIZ_COMPARATIVA.json',
        'fontes_primarias_verificadas': ' | '.join(c['fontes_primarias']),
        'tipo_evidencia': 'Confronto Documental e Oficial'
    })

ev_csv_path = os.path.join(target_dir, '05_INDICE_DE_EVIDENCIAS.csv')
with open(ev_csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID Caso', 'Tema', 'Candidato', 'Conclusão Auditada', 'Grau de Confiança', 'Arquivo Local Suporte', 'Fontes Primárias Verificadas', 'Tipo de Evidência'])
    for r in evidence_rows:
        w.writerow([r['id_caso'], r['tema'], r['candidato'], r['conclusao_auditada'], r['grau_confianca'], r['arquivo_local_suporte'], r['fontes_primarias_verificadas'], r['tipo_evidencia']])
print(f'Wrote 05_INDICE_DE_EVIDENCIAS.csv with {len(evidence_rows)} evidence records.')

# 2. Build 05_LOG_DE_EXECUCAO.md
log_md_path = os.path.join(target_dir, '05_LOG_DE_EXECUCAO.md')
log_content = '''# Log de Execução e Rastreabilidade da Auditoria (Fase F)

- **Data e Hora de Início:** 2026-10-24 09:25:20
- **Ambiente:** Windows / PowerShell / Python 3.12 (Ambiente Local Antigravity)
- **Diretório da Missão 3:** `C:\\Users\\RAFAE\\Downloads\\dossie_auditoria_independente_20261024\\`
- **Diretório Auditado:** `C:\\Users\\RAFAE\\Downloads\\dossie_checadores_coleta_20261024_091925\\`
- **Diretório Preservado Original:** `C:\\Users\\RAFAE\\Downloads\\verifiqueosfatos-recovery-20261024\\`

## Etapas Executadas

1. **Criação do Diretório de Auditoria:**
   - Criada a pasta `dossie_auditoria_independente_20261024` e o subdiretório `scripts/`.
2. **Fase A — Auditoria Estrutural:**
   - Executado `scripts/audit_structural.py` para conferência de linhas, registros e campos vazios.
   - Gerados `01_AUDITORIA_ESTRUTURAL.md`, `01_AUDITORIA_ESTRUTURAL.json` e `01_DUPLICATAS_E_CAMPOS_AUSENTES.csv`.
   - Reconciliadas explicitamente as questões do painel do FlagCheck e a contagem de arquivos do Verifique os Fatos.
3. **Fase B e C — Seleção dos 15 Casos e Matriz Comparativa:**
   - Executados `scripts/find_overlapping_claims.py`, `scripts/extract_15_cases.py` e `scripts/inspect_15_queries.py`.
   - Selecionadas 15 alegações críticas sobre obras, orçamento, salário mínimo, Bolsa Família, tributos, cartões corporativos e milícias.
   - Gerados `02_MATRIZ_COMPARATIVA.csv`, `02_MATRIZ_COMPARATIVA.json` e `02_RELATORIO_DE_DIVERGENCIAS.md`.
4. **Fase D — Auditoria das Fontes:**
   - Mapeadas 1.006 URLs únicas citadas no catálogo consolidado.
   - Executado `scripts/audit_sources_inventory.py` testando amostra de 60 URLs primárias e secundárias em rede.
   - Gerados `03_INVENTARIO_DE_FONTES.csv` e `03_AUDITORIA_DAS_FONTES.md`.
5. **Fase E — Consistência Metodológica e Viés:**
   - Executado `scripts/audit_bias_methodology.py` para cálculo de percentuais por candidato e taxonomia.
   - Gerados `04_DISTRIBUICAO_DE_VEREDITOS.csv` e `04_CONSISTENCIA_METODOLOGICA.md`.
6. **Fase F — Índice de Evidências e Hashes:**
   - Gerado `05_INDICE_DE_EVIDENCIAS.csv`.
   - Calculados os hashes SHA-256 de todos os artefatos produzidos em `05_SHA256_ARTEFATOS.txt`.
'''
with open(log_md_path, 'w', encoding='utf-8') as f:
    f.write(log_content)
print('Wrote 05_LOG_DE_EXECUCAO.md')

# 3. Compute SHA256 of all generated artifacts in target_dir
def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

sha_lines = []
for root, dirs, files in os.walk(target_dir):
    for fn in sorted(files):
        if fn == '05_SHA256_ARTEFATOS.txt':
            continue
        full_p = os.path.join(root, fn)
        rel_p = os.path.relpath(full_p, target_dir)
        sha_lines.append(f'{hash_file(full_p)}  {rel_p}')

sha_txt_path = os.path.join(target_dir, '05_SHA256_ARTEFATOS.txt')
with open(sha_txt_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines))
print(f'Wrote 05_SHA256_ARTEFATOS.txt with {len(sha_lines)} artifact hashes.')
