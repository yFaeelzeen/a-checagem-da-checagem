# A Checagem da Checagem — Dossiê de Auditoria e Confronto Factual (Eleições 2026)

Repositório analítico de preservação digital, auditoria estrutural e confronto comparativo das checagens de fatos publicadas sobre o debate presidencial da TV Globo do 2º turno das Eleições 2026 entre **Luiz Inácio Lula da Silva** e **Flávio Bolsonaro** (realizado em 23/10/2026).

O projeto reúne, normaliza e confronta dois ecossistemas:
1. **Checadores Independentes:** *Verifique a Verdade* (extração integral com 256 checagens em 2 debates e metodologia), *Pinóquio.live* (175 checagens), *Verifique os Fatos* (75 checagens), painel estatístico do *FlagCheck* e telemetria do *Checagem ao Vivo*.
2. **Grandes Portais Jornalísticos:** *G1 (Fato ou Fake)*, *UOL Confere*, *Estadão Verifica* e *Agência Lupa* (219 checagens individuais).

O projeto conta com uma **Aplicação Web Interativa**, um **Console de Auditoria Metodológica** e uma **API REST Nativa** pronta para execução local e deploy em nuvem (Vercel e GitHub).

---

## 📸 Demonstração Visual da Interface

### 1. Painel Principal & Placar Consolidado dos Candidatos
Aviso de transparência de IA no topo, botão de acesso direto ao repositório GitHub, identificação cromática partidária (Flávio em azul e Lula em vermelho) e placar geral apurado pelo critério da maioria das checagens.

![Painel Principal e Placar Consolidado](docs/screenshots/01_visao_geral_e_placar.png)

### 2. Busca por Palavra-Chave, Filtros e Baralho Paginado
Busca rápida com normalização semântica, filtros combinados de candidato e veredito, paginação compacta de 8 cards por página e gaveta retrátil de fontes oficiais.

![Catálogo Completo e Filtros de Declarações](docs/screenshots/02_catalogo_e_filtros.png)

### 3. Metodologia Integral & Console Interativo da API REST
Dossiê exaustivo de metodologia forense, investigação dos mecanismos de viés editorial sob o benefício da dúvida e playground interativo para disparo de requisições em tempo real à API REST.

![Metodologia e Console Interativo da API](docs/screenshots/03_metodologia_e_api.png)

---

## 🚀 Funcionalidades da Interface Web

- **Catálogo Completo de Declarações (412 registros):** Cobertura de todas as falas apuradas no debate com paginação balanceada (8 cards por página).
- **Busca por Palavra-Chave:** Campo de busca em tempo real com normalização semântica (ex.: digite `milícia`, `obras`, `nordeste`, `vacina`).
- **Filtros por Candidato e Veredito:**
  - Fotos oficiais de candidatura com identificação cromática partidária (**Flávio Bolsonaro** em azul, **Lula** em vermelho).
  - Filtro por veredito normalizado (*Verdadeiro*, *Falso*, *Enganoso/Controverso*).
- **Auditoria Condicional de Viés Editorial:**
  - Aplicada **exclusivamente quando há divergência substantiva** de classificação entre veículos independentes e a grande imprensa.
  - Questionamento metodológico direto ao usuário sobre o enquadramento adotado pelo checador independente.
  - Regra do benefício da dúvida com comprovação documental das fontes.
- **Gaveta Retrátil de Fontes Oficiais:**
  - Seção de fontes e evidências separada do corpo do texto em gaveta interativa com links externos identificados por domínio e órgão público.
- **Console Interativo de API REST (`metodologia.html`):**
  - Playground para testar e inspecionar em tempo real os retornos da API REST com botão de copiar JSON e comando cURL.

---

## 📁 Estrutura do Repositório

```text
a-checagem-da-checagem/
├── index.html             # Painel principal com catálogo, busca, filtros e cards
├── metodologia.html       # Dossiê metodológico integral e console interativo da API
├── app.js                 # Lógica reativa: busca, filtros, paginação e gaveta de fontes
├── styles.css             # Identidade visual inspirada em gazeta jornalística
├── declarations_data.js   # Catálogo completo de 412 declarações em JS estático
├── declarations.json      # Catálogo normalizado em JSON (2.6 MB)
├── api_data.json          # Metadados, escopo, pipeline e perfil das agências
├── lula.webp              # Foto oficial TSE
├── flavio.webp            # Foto oficial TSE
│
├── api/                   # Vercel Serverless Functions (Node.js)
│   ├── _utils.js          # Utilitários de carregamento de dados e cabeçalhos CORS
│   ├── index.js           # GET /api — Catálogo e sumário da API
│   ├── declarations.js    # GET /api/declarations?search=&candidate=&verdict=
│   ├── methodology.js     # GET /api/methodology — Pipeline e escopo da investigação
│   ├── bias-analysis.js   # GET /api/bias-analysis — Mecanismos forenses de viés
│   ├── cases.js           # GET /api/cases — Catálogo de casos
│   ├── stats.js           # GET /api/stats — Estatísticas agregadas e matriz cruzada
│   └── all.js             # GET /api/all — Exportação completa em JSON unificado
│
├── coleta/                # Arquivos brutos preservados dos sites (HTML, JS, CSS, JSON)
│   ├── checagemaovivo/    # Landing page e telemetria pós-debate
│   ├── flagcheck/         # Painéis estatísticos e metadados Schema.org
│   ├── pinoquio/          # Dump do event.json (175 checagens) e SPA
│   ├── portais/           # HTMLs brutos preservados (G1, UOL, Estadão, Lupa)
│   ├── verifiqueaverdade/ # Espelhamento integral: 274 ativos, 2 debates, metodologia e cards OG
│   └── verifiqueosfatos/  # Repositório Git SPA e posts.json originais
│
├── dados/                 # Planilhas e bancos de dados normalizados (CSV e JSON)
│   ├── independentes_globo.csv / .json    # 399 checagens individuais da Globo (+ 1 painel)
│   ├── portais_globo.csv / .json          # 219 checagens individuais dos 4 grandes portais
│   ├── verifiqueaverdade_globo.csv / .json # 149 checagens do debate Globo (com revisão pós-debate)
│   ├── verifiqueaverdade_band.csv / .json  # 107 checagens recuperadas do debate Band (18/10)
│   ├── verifiqueaverdade_total.csv / .json # Todas as 256 checagens do Verifique a Verdade
│   ├── pinoquio_globo.csv                 # 175 checagens estruturadas do Pinóquio.live
│   └── verifiqueosfatos_globo.csv         # 75 checagens estruturadas do Verifique os Fatos
│
├── auditoria/             # Análises de integridade, metodologia e fontes oficiais
│   ├── auditoria_estrutural.md / .json    # Integridade de campos, dados e arquivos
│   ├── duplicatas_e_lacunas.csv           # Mapeamento de campos nulos e duplicatas
│   ├── fontes_inventario.csv              # 1.006 URLs de fontes mapeadas nos checadores
│   ├── fontes_analise.md                  # Teste de conformidade de 60 links de órgãos oficiais
│   ├── distribuicao_vereditos.csv         # Placar e distribuição por candidato e veículo
│   ├── indice_evidencias.csv              # Matriz de sustentação factual
│   ├── metodologia_independentes.md       # Auditoria metodológica dos independentes
│   ├── metodologia_verifiqueaverdade.md   # Metodologia oficial do Verifique a Verdade
│   ├── novas_checagens_verifiqueaverdade.json # Auditoria das 17 novas falas da revisão Globo
│   ├── portais_inventario.csv / .json     # Catálogo das 4 publicações jornalísticas
│   ├── portais_metodologia.md             # Critérios de checagem dos 4 grandes portais
│   ├── portais_divergencias.md            # Confronto interno entre G1, UOL, Estadão e Lupa
│   ├── portais_consistencia.md            # Avaliação de simetria editorial e rigor
│   └── portais_lacunas.md                 # Limitações técnicas e declarações não cobertas
│
├── confronto/             # Cruzamento exaustivo (Independentes vs Grandes Portais)
│   ├── confronto_declaracoes.md           # Pareamento exaustivo de todas as 399 checagens
│   ├── confronto_dados.csv / .json        # Matriz relacional completa (886 pares de correspondência)
│   ├── confronto_20_casos.csv / .json     # 20 controvérsias centrais confrontadas em detalhe
│   └── confronto_15_casos_independentes.csv # Matriz comparativa entre os independentes
│
├── relatorios/            # Relatórios executivos explicativos em Markdown
│   ├── relatorio_confronto.md             # Síntese do confronto Independentes vs Grandes Portais
│   ├── relatorio_independentes.md         # Diagnóstico dos checadores independentes
│   ├── relatorio_portais.md               # Diagnóstico dos grandes portais de imprensa
│   └── relatorio_verifiqueaverdade.md     # Relatório da preservação integral do site
│
├── docs/screenshots/      # Capturas de tela demonstrativas em alta resolução
├── scripts/               # Pipelines reprodutíveis em Python
├── vercel.json            # Configuração de deploy, rotas e serverless na Vercel
├── package.json           # Manifesto do projeto e scripts de execução
├── README.md              # Documentação principal
└── SHA256_HASHES.txt      # Verificação criptográfica de integridade de todos os 475 arquivos
```

---

## 🌐 Como Fazer o Deploy no Vercel

O projeto foi configurado com `vercel.json` na raiz e endpoints serverless em `/api`. Para publicar:

### Opção 1: Pelo Painel Web da Vercel (Recomendada)
1. Faça push do repositório para a sua conta no GitHub (veja a seção [Como Subir no GitHub](#-como-subir-no-github)).
2. Acesse [vercel.com](https://vercel.com) e clique em **"Add New..." > "Project"**.
3. Selecione o repositório `a-checagem-da-checagem` importado do GitHub.
4. Mantenha as configurações padrão (Framework Preset: **Other** / Root Directory: `./`).
5. Clique em **"Deploy"**.
6. A Vercel provisionará tanto a interface estática (`/`, `/metodologia.html`) quanto as rotas de API (`/api/declarations`, etc.) automaticamente.

### Opção 2: Pela CLI da Vercel
```bash
# 1. Instalar a CLI da Vercel globalmente (se ainda não tiver)
npm install -g vercel

# 2. Na raiz do projeto, execute o deploy
vercel --prod
```

---

## 🐙 Como Subir no GitHub

Para publicar o projeto em um novo repositório no seu GitHub:

```bash
# 1. Abra o terminal na raiz da pasta do projeto:
cd C:\Users\RAFAE\Downloads\a-checagem-da-checagem

# 2. Crie um novo repositório vazio no GitHub (ex: a-checagem-da-checagem)
#    Não marque a opção de criar README ou .gitignore no GitHub (já temos aqui).

# 3. Vincule a branch remota e envie o código:
git remote add origin https://github.com/SEU_USUARIO/a-checagem-da-checagem.git
git branch -M main
git push -u origin main
```

---

## 💻 Como Executar Localmente

### Opção A: Servidor Local (Node.js ou Python)
Sem dependências externas:

```bash
# Via npm/npx
npx serve .

# Ou via Python local
python scripts/local_server.py
```
Acesse no navegador:
- Interface Principal: **http://localhost:8080** (ou porta indicada pelo `serve`)
- Metodologia e API: **http://localhost:8080/metodologia.html**
- Endpoint da API: **http://localhost:8080/api**

---

## 📡 Endpoints da API REST

A API responde com `Content-Type: application/json; charset=utf-8` e cabeçalhos CORS liberados (`Access-Control-Allow-Origin: *`):

| Endpoint | Método | Descrição | Parâmetros Opcionais |
| :--- | :---: | :--- | :--- |
| `/api` | `GET` | Metadados do projeto, sumário e links disponíveis | — |
| `/api/declarations` | `GET` | Catálogo das 412 declarações com filtros | `search`, `candidate` (`lula`, `flavio`), `verdict` (`true`, `false`, `misleading`) |
| `/api/methodology` | `GET` | Metodologia forense, escopo e pipeline | — |
| `/api/bias-analysis` | `GET` | Mecanismos de viés e perfis dos checadores | — |
| `/api/cases` | `GET` | Catálogo estruturado de casos | — |
| `/api/stats` | `GET` | Estatísticas de universo, veículos e matriz cruzada | — |
| `/api/all` | `GET` | Base de dados integral unificada em JSON | — |

---

## 📊 Principais Conclusões da Pesquisa

### 1. Volume de Dados Auditado
- **399 checagens individuais** dos projetos independentes no debate da TV Globo (*Pinóquio.live*: 175; *Verifique a Verdade*: 149; *Verifique os Fatos*: 75).
- **107 checagens individuais** adicionais recuperadas do debate da Band pelo *Verifique a Verdade*, consolidando **256 checagens** no portal.
- **219 checagens individuais** dos quatro grandes veículos de imprensa (*Estadão Verifica*, *G1 — Fato ou Fake*, *Agência Lupa*, *UOL Confere*).
- **312 checagens (78,2%)** das 399 checagens independentes da Globo encontram correspondência direta nas apurações da imprensa tradicional.

### 2. Descobertas do *Verifique a Verdade*
- **Revisão Pós-Debate (+17 checagens):** O site continuou atualizando suas checagens após o debate da Globo, publicando 17 novas análises (de `b1-51` a `b4-27`), incluindo dados do Banco Central sobre taxa de juros real, reduflação de produtos da cesta de consumo, promessas de criação da Casa da Mulher Brasileira e depoimentos da CPMI Vorcaro.
- **Transparência de Fontes:** 100% das checagens do *Verifique a Verdade* e do *Pinóquio.live* contêm links diretos para documentos primários (leis, acórdãos e relatórios oficiais).
- **Metodologia Formal:** Exige comprovação objetiva para declarações factuais e não atribui selos de veredito a opiniões, juízos de valor ou perguntas de mediadores.

### 3. Convergência Factual (+80% de Acordo nos Fatos Primários)
- Ambos os ecossistemas convergem plenamente na apuração dos dados oficiais do Estado brasileiro (relatórios do TCU sobre obras paralisadas, estatísticas do Banco Central sobre dívida pública, IPCA do IBGE e dados do TSE).
- Rejeição unânime de boatos sem lastro (aquisição de ilha do MST por jogador de futebol, aprovação do fim da escala 6x1, piso permanente de R$ 600 sob governo anterior).

### 4. As Razões Reais das Divergências de Veredito
- **Atribuição Causal (11.500 obras paralisadas do TCU):** *Verifique a Verdade*, *G1* e *Estadão* consideraram a fala de Flávio `Verdadeiro / Fato` pela exatidão do número do TCU; *Pinóquio.live*, *Verifique os Fatos*, *UOL* e *Lupa* classificaram como `Falso / Enganoso / Falta Contexto` por penalizarem a atribuição da autoria ao governo federal (maioria municipal).
- **Tipificação Jurídica Formal vs Vínculos Materiais (Inquérito de milícia contra Flávio):** *Verifique a Verdade*, *UOL*, *Estadão* e *Lupa* classificaram como `Verdadeiro` pelo rigor formal penal (inexistência de inquérito sob o tipo penal de milícia armada); *Pinóquio.live* e *G1* classificaram como `Insustentável / Não é bem assim` apontando investigações conexas de nomeações no gabinete.
- **Tolerância a Erro Contra Si Mesmo:** No caso de Lula alegando ter herdado 6 mil obras (quando eram 8.603 no TCU), *G1* e *UOL* aplicaram `Fake / Falso` pela imprecisão numérica, enquanto *Verifique a Verdade* considerou `Verdadeiro` e *Lupa* considerou `Subestimado` por ser erro que jogava contra o próprio orador.

---

## ⚖️ Licenciamento Aberto

- **Código-fonte:** Distribuído sob a licença **MIT** (veja [LICENSE](file:///LICENSE)).
- **Dados, relatórios e textos:** Distribuídos sob **Creative Commons Atribuição 4.0 Internacional (CC-BY-4.0)**.
