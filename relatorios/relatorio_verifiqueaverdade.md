# Relatório Executivo de Extração e Preservação Integral — Verifique a Verdade

> **Site Oficial:** `https://verifiqueaverdade.com.br/`  
> **Data da Coleta com REA:** 24/10/2026 | **Método:** Coleta Passiva de Superfície e Engenharia Reversa Web  
> **Total de Recursos Preservados:** 274 ativos web (HTMLs, Chunks JS Turbopack, Folhas CSS, Assets SVG e Cards OpenGraph)  
> **Status de Integridade:** 100% dos recursos obtidos sem bloqueio (HTTP 200) e catalogados com SHA-256 em manifesto determinístico.

---

## 1. 🌐 Escopo da Extração Completa

Diferentemente da coleta inicial preliminar — que havia focado estritamente na URL da transmissão do debate da Globo —, a presente operação do REA realizou o mapeamento exaustivo de todo o domínio público `verifiqueaverdade.com.br`, recuperando:

1. **Página Inicial (`/`):** Dashboard público com índices consolidados, painéis comparativos e navegação geral (40.930 bytes).
2. **Debate TV Globo Atualizado (`/debates/globo-2026-10-23/`):** A versão mais recente e expandida do debate de 23/10/2026, com **149 checagens individuais** (1.346.686 bytes), integrando 17 checagens concluídas na revisão pós-transmissão que não constavam no snapshot matinal de 132 checagens.
3. **Debate Band Recuperado (`/debates/band-2026-10-18/`):** Preservação completa do primeiro debate presidencial do 2º turno, contendo **107 checagens individuais** (930.032 bytes).
4. **Página Oficial de Metodologia (`/metodologia/`):** Documento metodológico formal de critérios e diretrizes editoriais do projeto (26.444 bytes).
5. **Ativos Estáticos e Bundles:** 10 chunks JavaScript Next.js/Turbopack, CSS de layout responsivo, ícones de marca SVG e **256 cards visuais OpenGraph** (`/og/checagem/...`) criados dinamicamente para cada checagem individual.

---

## 2. 📜 Metodologia Editorial do Verifique a Verdade

A extração e análise da página oficial [`metodologia/index.html`](file:///C:/Users/RAFAE/Downloads/a-checagem-da-checagem/01_coleta_preservacao_bruta/verifiqueaverdade_com_br/metodologia/index.html) revelou os padrões operacionais do projeto:

- **Critério de Elegibilidade:** Apenas declarações factuais passíveis de comprovação objetiva recebem veredito (números, leis, votações parlamentares, acórdãos e dados contábeis). Juízos de valor, opiniões ou caracterizações políticas (ex.: *"traição"*, *"desespero eleitoral"*) não são pontuados.
- **Regra Estrita de Fontes Primárias:** Todas as checagens exigem links oficiais diretos (Planalto, Câmara, Senado, TCU, IBGE, Banco Central, Tesouro Nacional, STF/STJ/TSE). Reportagens de imprensa só são admitidas em casos excepcionais onde inexiste registro governamental, devendo ser explicitamente rotuladas como `imprensa`.
- **Exclusão de Dados da Mediação:** Afirmações e perguntas feitas por jornalistas e mediadores não pontuam contra os candidatos no placar geral; quando conferidas, figuram apenas como nota de rodapé informativa.
- **Escala Graduada de Vereditos:** Utiliza 6 classificações: `Verdadeiro`, `Falso`, `Impreciso`, `Contraditório`, `Insustentável` e `Não verificável`.

---

## 3. 🔍 Debate TV Globo (23/10/2026) — Análise das 149 Checagens e Atualização

A base do debate da Globo foi atualizada de 132 para **149 checagens**. A distribuição total das checagens do debate ficou consolidada da seguinte forma:

| Candidato | Total de Falas Checadas | % do Corpus |
| :--- | :--- | :--- |
| **Flávio** | 85 | 57.0% |
| **Lula** | 64 | 43.0% |

**Distribuição de Vereditos no Debate Globo (149 checagens):**

- **Verdadeiro:** 73 (49.0%)
- **Impreciso:** 42 (28.2%)
- **✕Falso:** 23 (15.4%)
- **Não verificável:** 11 (7.4%)

### As 17 Checagens Adicionadas na Revisão Pós-Transmissão

A comparação automatizada entre o snapshot inicial (`globo-2026-10-23_snapshot_inicial_132.html`) e o arquivo final preservado identificou as seguintes 17 verificações concluídas após o encerramento do debate:

| ID | Candidato | Horário | Veredito | Resumo da Alegação |
| :--- | :--- | :--- | :--- | :--- |
| `b1-51` | **Flávio** | 0:19:15 | `Verdadeiro` | O Brasil tem "uma das maiores taxas de juros do mundo"... |
| `b1-52` | **Flávio** | 0:19:24 | `Impreciso` | Por causa dos juros, a dúzia de ovos "virou dez", o sabão em pó d... |
| `b1-53` | **Lula** | 0:39:43 | `Impreciso` | Quando assumiu, o Nordeste era a região "mais pobre", "mais analf... |
| `b1-54` | **Lula** | 0:42:33 | `Não verificável` | "Nós fizemos 14 novos hospitais" no Nordeste... |
| `b2-36` | **Lula** | 1:06:33 | `Impreciso` | Herdou a taxa de juro "com 13%", e ela "está 13,75%" com o Banco ... |
| `b2-37` | **Lula** | 1:09:15 | `Impreciso` | Bolsonaro "optou" por deixar morrer 716 mil pessoas na Covid em v... |
| `b2-38` | **Lula** | 1:12:24 | `✕Falso` | O escolhido de Flávio para a Saúde "disse que vai privatizar o SU... |
| `b2-39` | **Flávio** | 1:14:19 | `Não verificável` | "Cada vez é menor o percentual que o governo federal coloca" na s... |
| `b2-40` | **Lula** | 0:56:01 | `Impreciso` | "Milhões de trabalhadores se acidentam" por irresponsabilidade pa... |
| `b3-28` | **Flávio** | 1:22:37 | `Não verificável` | A Caixa tem "mais de 11 milhões de contratos imobiliários", com "... |
| `b3-29` | **Lula** | 1:25:30 | `Verdadeiro` | O Brasil tem "17,5 milhões" de MEIs... |
| `b4-22` | **Flávio** | 1:46:51 | `✕Falso` | "Eu vou criar a Casa da Mulher Brasileira", onde a mulher agredid... |
| `b4-23` | **Flávio** | 1:53:07 | `Impreciso` | O fim da marcação das balas veio de uma emenda de deputado na Câm... |
| `b4-24` | **Flávio** | 1:55:44 | `Verdadeiro` | Lula recebeu R$ 30 milhões "por fora", que, "segundo o áudio", fo... |
| `b4-25` | **Flávio** | 2:02:30 | `Verdadeiro` | Lula "prometeu que não ia indicar seus amigos pro Supremo e indic... |
| `b4-26` | **Flávio** | 2:03:46 | `Não verificável` | "Quem tá sustentando Lulinha é a Roberta" Luchsinger... |
| `b4-27` | **Flávio** | 2:03:49 | `Verdadeiro` | Lula chamou Roberta Luchsinger de "pilantra" várias vezes e disse... |

**Destaques Fatuais das Novas Checagens:**
1. **Economia (Selic e Juros Reais):** Em `b1-51`, Flávio alega que o Brasil tem uma das maiores taxas de juro do mundo. O projeto classificou como `Verdadeiro` citando dados da API do Banco Central (SGS 432) e ranking Infinity/Moneyou apontando juro real de 8,1% ao ano.
2. **Reduflação:** Em `b1-52`, Flávio cita a redução de produtos de consumo (sabão em pó de 1kg para 800g, caixa de chocolate, etc.). Classificado como `Impreciso` pois o fenômeno existe e é monitorado pelo Procon, mas a alegação superdimensiona percentuais e generaliza a cesta.
3. **Financiamento de Filme e Delação Vorcaro:** Em `b4-24`, Flávio cita áudio de Daniel Vorcaro sobre suposto repasse de R$ 30 mi ao Instituto Lula. Classificado como `Verdadeiro` com base na existência material do áudio confirmado pela defesa do banqueiro em 12/10, registrando contudo que PF e PGR não acolheram a alegação em termo formal de delação premiada.
4. **Políticas Públicas e Casa da Mulher Brasileira:** Em `b4-22`, Flávio afirma *"Eu vou criar a Casa da Mulher Brasileira"*. Classificado como `Falso` pois o programa foi formalmente instituído pelo Decreto nº 8.086 de 2013 e já possui dezenas de unidades em funcionamento.

---

## 4. 📺 Debate Band (18/10/2026) — 107 Checagens Recuperadas

A preservação do arquivo [`debates/band-2026-10-18.html`](file:///C:/Users/RAFAE/Downloads/a-checagem-da-checagem/01_coleta_preservacao_bruta/verifiqueaverdade_com_br/debates/band-2026-10-18.html) permitiu incorporar à auditoria a íntegra das checagens do debate anterior na Band:

- **Volume:** 107 checagens individuais estruturadas.
- **Candidatos:** Lula com 56 falas checadas (52.3%), Flávio Bolsonaro com 51 falas checadas (47.7%).
- **Distribuição de Vereditos:**
  - `Verdadeiro`: 47 (43.9%)
  - `Impreciso`: 29 (27.1%)
  - `✕Falso`: 22 (20.6%)
  - `Não verificável`: 9 (8.4%)

---

## 5. 📊 Resumo Consolidado do Projeto Verifique a Verdade

| Categoria | Quantidade |
| :--- | :--- |
| **Ativos Web Preservados no Repositório** | 274 arquivos |
| **Checagens Debate Globo (23/10/2026)** | 149 checagens |
| **Checagens Debate Band (18/10/2026)** | 107 checagens |
| **Total de Checagens no Site** | **256 checagens** |
| **Taxa de Transparência de Fontes** | 100% com links para fontes primárias |
| **Manifesto Criptográfico** | [`inventario_extracao_completa.json`](file:///C:/Users/RAFAE/Downloads/a-checagem-da-checagem/01_coleta_preservacao_bruta/verifiqueaverdade_com_br/inventario_extracao_completa.json) |
