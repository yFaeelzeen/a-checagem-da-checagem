# Dossiê de Auditoria Comparativa — Quatro Fontes Jornalísticas Autorizadas (Missão 4)

Este diretório contém a auditoria sistemática, individual e comparativa das checagens do debate presidencial da TV Globo (23/10/2026) entre Lula e Flávio Bolsonaro, realizada sob a restrição mandatória de **lista fechada** de quatro publicações jornalísticas autorizadas.

## 1. Fontes Externas Autorizadas
1. **UOL Confere:** `https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm`
2. **G1 — Fato ou Fake:** `https://g1.globo.com/google/amp/fato-ou-fake/eleicoes/noticia/2026/10/23/veja-o-que-e-fato-ou-fake-nas-falas-de-flavio-bolsonaro-e-lula-no-debate-da-globo-no-2o-turno-das-eleicoes-2026.ghtml`
3. **Estadão Verifica:** `https://www.estadao.com.br/amp/estadao-verifica/debate-tv-globo-checagem-tempo-real-ao-vivo/`
4. **Agência Lupa:** `https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/`

## 2. Estrutura de Arquivos da Pasta
- `00_LEIA_ME_METODOLOGIA.md`: Guia de leitura e princípios metodológicos.
- `01_INVENTARIO_QUATRO_PUBLICACOES.csv` e `.json`: Metadados técnicos, URLs, status HTTP, hashes SHA-256 e totais de checagens por veículo.
- `02_CHECAGENS_INDIVIDUAIS.csv` e `.json`: Catálogo exaustivo com 219 checagens individuais identificadas e transcritas.
- `03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.csv` e `.json`: Matriz relacional agrupando alegações comparáveis entre os quatro veículos.
- `04_DIVERGENCIAS_E_CONCORDANCIAS.md`: Análise profunda das divergências metodológicas, factuais e semânticas.
- `05_CONSISTENCIA_EDITORIAL_LULA_FLAVIO.md`: Auditoria de simetria de critérios e cobertura entre os candidatos.
- `06_LACUNAS_E_LIMITACOES.md`: Documentação de limites da coleta e tratamento de FlagCheck e Checagem ao Vivo.
- `07_RELATORIO_EXECUTIVO_FINAL.md`: Síntese executiva com respostas diretas a todas as perguntas do mandato.
- `08_LOG_DE_EXECUCAO.md`: Registro cronológico de todos os passos computacionais executados.
- `09_SHA256_ARTEFATOS.txt`: Hashes criptográficos de todos os arquivos gerados.
- `raw_sources/`: Cópia preservada dos HTMLs originais das quatro reportagens.
- `scripts/`: Código Python determinístico executado para a produção de cada arquivo.
