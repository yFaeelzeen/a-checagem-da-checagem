# Script definitivo para restaurar o design da gazeta com dados literais e sem cache
from pathlib import Path
import time

INTERFACE_DIR = Path(r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface")
ts = int(time.time())

# 1. ATUALIZAR index.html COM CACHE BUSTER
index_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A Checagem da Checagem — Dossiê de Auditoria Factual 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400..900;1,7..72,400..700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v={ts}">
</head>
<body class="newsprint-theme">

  <!-- Cabeçalho da Gazeta de Auditoria -->
  <header class="gazette-header">
    <div class="gazette-top-strip">
      <div class="gazette-container strip-flex">
        <span class="edition-tag">DOSSIÊ INDEPENDENTE Nº 01/2026</span>
        <span class="edition-center">COMPARAÇÃO DIRETA • DEBATE PRESIDENCIAL TV GLOBO (23/10/2026)</span>
        <span class="edition-status">BASE: 399 CHECAGENS vs 219 PORTAIS</span>
      </div>
    </div>

    <div class="gazette-container masthead">
      <div class="masthead-main">
        <div class="masthead-brand">
          <div class="masthead-titles">
            <h1 class="newspaper-title">A CHECAGEM DA CHECAGEM</h1>
            <p class="newspaper-deck">
              Quando sete jornais e agências assistem à mesma fala no debate, por que chegam a conclusões opostas?
            </p>
          </div>
        </div>

        <div class="masthead-actions">
          <button class="theme-toggle-btn" id="theme-toggle" aria-label="Alternar modo de leitura papel / tinta noturna">
            <span class="theme-btn-text">MODO DE LEITURA</span>
          </button>
        </div>
      </div>

      <!-- Resumo de Entrada: Linguagem Clara e Literal -->
      <div class="gazette-editorial-lead">
        <p>
          Confrontamos <strong>399 checagens de sites independentes</strong> (<em>Verifique a Verdade</em>, <em>Pinóquio.live</em>, <em>Verifique os Fatos</em>) com as apurações dos <strong>quatro maiores portais de notícias</strong> (<em>G1</em>, <em>UOL</em>, <em>Estadão</em> e <em>Agência Lupa</em>). Veja abaixo os casos explicados de forma literal e direta: o que foi dito, o fato real nos documentos e por que os vereditos se dividiram.
        </p>
      </div>
    </div>
  </header>

  <!-- Conteúdo Principal -->
  <main class="gazette-container docket-layout">

    <!-- Seletor de Casos -->
    <section class="docket-selector" aria-label="Casos em julgamento">
      <div class="selector-header">
        <span class="selector-title">CASOS EM DESTAQUE (CLIQUE PARA VER A COMPARAÇÃO)</span>
        <span class="selector-hint">5 casos com explicações literais e placar das agências</span>
      </div>
      <div class="case-tabs-strip" id="case-tabs" role="tablist">
        <!-- Injetado via JS -->
      </div>
    </section>

    <!-- O Dossiê do Caso Selecionado -->
    <section class="case-dossier" id="active-case-dossier">
      <!-- Injetado dinamicamente via JS -->
    </section>

    <!-- Explicação das Divergências: Linguagem Direta -->
    <section class="editorial-framework">
      <div class="framework-header">
        <h2 class="framework-title">Como checadores chegam a resultados opostos para a mesma frase?</h2>
      </div>
      <div class="framework-columns">
        <div class="framework-card">
          <span class="card-num">01</span>
          <h3 class="card-headline">O número existe no papel, mas a culpa foi distorcida</h3>
          <p class="card-body">
            O candidato cita um número real de órgão oficial (como o TCU), mas culpa o adversário ou o governo federal. Quem dá <strong>Verdadeiro</strong> olha só se o documento existe; quem dá <strong>Falso</strong> condena o fato de jogar a culpa no alvo errado.
          </p>
        </div>
        <div class="framework-card">
          <span class="card-num">02</span>
          <h3 class="card-headline">A letra fria da lei contra o que a polícia investigou</h3>
          <p class="card-body">
            Na Justiça formal, se não existe processo aberto com o nome daquele crime específico, a frase é estritamente <strong>Verdadeira</strong>. Mas se a polícia investigou mensagens, repasses ou nomeações de suspeitos pelo gabinete, outros veículos carimbam como <strong>Enganoso</strong> ou <strong>Falta Contexto</strong>.
          </p>
        </div>
        <div class="framework-card">
          <span class="card-num">03</span>
          <h3 class="card-headline">Errar uma estatística contra si mesmo</h3>
          <p class="card-body">
            O candidato erra uma estatística, mas fala um número menor do que a realidade (prejudicando a própria denúncia). Quem aplica a matemática fria carimba <strong>Fake</strong>; quem avalia a intenção releva o erro porque o orador não tentou tirar vantagem.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- Rodapé -->
  <footer class="gazette-footer">
    <div class="gazette-container footer-flex">
      <div class="footer-left">
        <strong>A Checagem da Checagem</strong> — Auditoria Factual Comparada
        <div class="footer-meta">Debate Presidencial TV Globo • 23 de Outubro de 2026 • 2º Turno</div>
      </div>
      <div class="footer-right">
        Repositório local de auditoria: <code>a-checagem-da-checagem/confronto/confronto_declaracoes.md</code>
      </div>
    </div>
  </footer>

  <script src="app.js?v={ts}"></script>
</body>
</html>
'''
INTERFACE_DIR.joinpath("index.html").write_text(index_html, encoding="utf-8")

# 2. ATUALIZAR app.js RESTAURANDO O LAYOUT DA GAZETA
app_js = r'''// Casos Auditados do Dossiê "A Checagem da Checagem" — Versão com Design Broadsheet Restaurado
const DOSSIER_CASES = [
  {
    id: "CASO 01",
    tagId: "TCU • OBRAS",
    speaker: "Flávio Bolsonaro",
    speakerShort: "Flávio",
    blockTime: "Bloco 1 • 0:07:17",
    headline: "As 11.500 obras paradas do TCU",
    quote: "O TCU acaba de soltar relatório com mais de 11.500 obras paralisadas no atual governo.",
    verdictBadge: "DIVERGÊNCIA DE CULPA",
    stampClass: "divergence",

    theFact: "O relatório do TCU existe de verdade e registra 11.469 obras paradas no país. Porém, a grande maioria esmagadora são obras de municípios (prefeituras) iniciadas há muitos anos em gestões passadas, e não obras federais paralisadas pelo governo atual.",

    whyDiverge: "Quem deu VERDADEIRO focou no papel oficial (o número 11.469 existe no TCU). Quem deu FALSO focou na culpa política (dizer que as obras pararam 'no atual governo' é enganoso, pois a maioria é antiga e municipal).",

    scoreboard: [
      { count: 3, label: "VERDADEIRO / FATO", type: "true" },
      { count: 3, label: "FALSO", type: "fake" },
      { count: 1, label: "ENGANOSO / CONTEXTO", type: "warn" }
    ],

    pressChecks: [
      {
        outlet: "G1 — Fato ou Fake",
        verdict: "#FATO",
        stampClass: "stamp-true",
        text: "Verdadeiro porque o relatório do TCU realmente existe e aponta 11.469 obras paralisadas em território nacional."
      },
      {
        outlet: "Estadão Verifica",
        verdict: "Verdadeiro",
        stampClass: "stamp-true",
        text: "Verdadeiro porque o número bate com a contagem técnica oficial mais recente aprovada pelo TCU."
      },
      {
        outlet: "UOL Confere",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso porque as obras federais diretas são cerca de 4.200, e culpar o governo atual ignora que a imensa maioria é de prefeituras."
      },
      {
        outlet: "Agência Lupa",
        verdict: "Falta Contexto",
        stampClass: "stamp-warn",
        text: "Falta contexto porque o número é autêntico, mas quase todas as obras foram paralisadas em governos passados."
      }
    ],

    independentChecks: [
      {
        outlet: "Verifique a Verdade",
        verdict: "Verdadeiro",
        stampClass: "stamp-true",
        text: "O documento do TCU contabilizou exatamente 11.469 obras paralisadas em levantamento de 2025. O dado documental confere."
      },
      {
        outlet: "Pinóquio.live",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso porque culpar o governo atual é enganoso: quase todas são contratos com prefeituras firmados há mais de 8 anos."
      },
      {
        outlet: "Verifique os Fatos",
        verdict: "Enganoso",
        stampClass: "stamp-warn",
        text: "Enganoso porque citar o número sem explicar que a responsabilidade é de prefeituras distorce a realidade para o eleitor."
      }
    ],

    primarySources: [
      "Relatório de Auditoria do TCU (11.469 obras paradas)",
      "Painel Integrado de Obras Federais (Destrava)"
    ]
  },

  {
    id: "CASO 02",
    tagId: "POLÍCIA • MILÍCIA",
    speaker: "Flávio Bolsonaro",
    speakerShort: "Flávio",
    blockTime: "Bloco 1 • 0:13:42",
    headline: "Investigação por milícia armada",
    quote: "Desde que o Brasil foi descoberto lá em 1500, eu nunca fui investigado por causa de envolvimento com milícia, Lula. Isso é coisa da sua cabeça.",
    verdictBadge: "LEI FORMAL vs. SUSPEITAS NO GABINETE",
    stampClass: "divergence",

    theFact: "Na Justiça criminal formal, nunca houve inquérito indiciando Flávio pelo crime de milícia armada (artigo 288-A do Código Penal). Por outro lado, investigações da Polícia Federal documentaram repasses de emendas e contratações de parentes de milicianos pelo seu gabinete.",

    whyDiverge: "Quem deu VERDADEIRO seguiu a lei ao pé da letra (não existe processo criminal com esse crime). Quem deu FALTA CONTEXTO ou INSUSTENTÁVEL considerou que dizer que 'nunca foi investigado' esconde os relatórios da Polícia Federal sobre ligações do seu gabinete com milicianos.",

    scoreboard: [
      { count: 2, label: "VERDADEIRO", type: "true" },
      { count: 0, label: "FALSO", type: "fake" },
      { count: 3, label: "FALTA CONTEXTO", type: "warn" }
    ],

    pressChecks: [
      {
        outlet: "Estadão Verifica",
        verdict: "Verdadeiro",
        stampClass: "stamp-true",
        text: "Verdadeiro no critério formal da lei: os processos contra ele investigaram 'rachadinhas' (desvio de salários), e não o crime de milícia."
      },
      {
        outlet: "G1 — Fato ou Fake",
        verdict: "Não é Bem Assim",
        stampClass: "stamp-warn",
        text: "Não é bem assim porque, embora o crime formal não seja milícia, relatórios da PF documentam a proximidade de seu gabinete com suspeitos."
      },
      {
        outlet: "Agência Lupa",
        verdict: "Falta Contexto",
        stampClass: "stamp-warn",
        text: "Falta contexto porque a Polícia Federal apurou pedidos de verbas intermediados por milicianos, mesmo o inquérito focando no desvio de verbas."
      }
    ],

    independentChecks: [
      {
        outlet: "Verifique a Verdade",
        verdict: "Verdadeiro",
        stampClass: "stamp-true",
        text: "Verdadeiro pela lei: não há e nunca houve inquérito criminal formal sob o tipo penal de milícia armada (artigo 288-A do Código Penal)."
      },
      {
        outlet: "Pinóquio.live",
        verdict: "Insustentável",
        stampClass: "stamp-warn",
        text: "Insustentável porque Flávio empregou a mãe e a esposa de Adriano da Nóbrega na Alerj e atendeu a pedidos investigados pela Polícia Federal."
      }
    ],

    primarySources: [
      "Inquéritos do STF (4.874 e 4.879)",
      "Relatórios de Operação da Polícia Federal",
      "Código Penal Brasileiro (Art. 288-A)"
    ]
  },

  {
    id: "CASO 03",
    tagId: "TCU • HERANÇA",
    speaker: "Lula",
    speakerShort: "Lula",
    blockTime: "Bloco 2 • 0:48:19",
    headline: "As 6 mil obras paradas herdadas",
    quote: "Quando eu assumi o governo, tinha quase 6 mil obras paradas nesse país.",
    verdictBadge: "ERRO DE NÚMERO vs. PREJUÍZO PRÓPRIO",
    stampClass: "divergence",

    theFact: "Em abril de 2023, o TCU registrava 8.603 obras paradas no país. Ou seja: o problema herdado era ainda pior do que Lula falou (eram 8,6 mil obras, e não 6 mil).",

    whyDiverge: "Quem deu FALSO puniu o erro matemático direto (6 mil é bem diferente de 8,6 mil). Quem deu VERDADEIRO ou SUBESTIMADO levou em conta que Lula errou para baixo, diminuindo um número negativo herdado que servia para defender seu próprio governo.",

    scoreboard: [
      { count: 1, label: "VERDADEIRO", type: "true" },
      { count: 3, label: "FALSO / FAKE", type: "fake" },
      { count: 1, label: "SUBESTIMADO", type: "warn" }
    ],

    pressChecks: [
      {
        outlet: "G1 — Fato ou Fake",
        verdict: "#FAKE",
        stampClass: "stamp-fake",
        text: "Fake pelo rigor dos números: a diferença de mais de 2.600 obras está fora de qualquer margem de arredondamento aceitável."
      },
      {
        outlet: "UOL Confere",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso porque os registros oficiais do TCU e da CGU na época indicavam 8.603 obras paradas, e não 6 mil."
      },
      {
        outlet: "Agência Lupa",
        verdict: "Subestimado",
        stampClass: "stamp-warn",
        text: "Subestimado: o número dito pelo candidato foi menor do que o saldo real documentado pelo tribunal de contas."
      }
    ],

    independentChecks: [
      {
        outlet: "Verifique a Verdade",
        verdict: "Verdadeiro",
        stampClass: "stamp-true",
        text: "Verdadeiro no sentido prático: eram 8.603 obras. Lula diminuiu o problema herdado em vez de aumentar para tirar vantagem."
      },
      {
        outlet: "Pinóquio.live",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso pelo rigor dos números: a diferença de 2.600 obras não permite validar a frase como verdadeira."
      }
    ],

    primarySources: [
      "Diagnóstico de Obras Paralisadas do TCU (Abril/2023)",
      "Painel de Obras do Ministério da Gestão (MGI)"
    ]
  },

  {
    id: "CASO 04",
    tagId: "INTERNET • BOATO",
    speaker: "Flávio Bolsonaro",
    speakerShort: "Flávio",
    blockTime: "Bloco 3 • 1:19:05",
    headline: "Boato sobre compra de ilha e o MST",
    quote: "Acusação sobre compra de ilha por jogador da seleção brasileira e suposta ligação patrimonial com o MST.",
    verdictBadge: "MENTIRA COMPLETA (UNANIMIDADE)",
    stampClass: "consensus",

    theFact: "Essa história é 100% inventada. Nunca existiu nenhuma compra de ilha por jogador da seleção brasileira em parceria com o MST. Trata-se de uma montagem antiga de internet que já havia sido desmentida antes.",

    whyDiverge: "Aqui não houve nenhuma discordância: todas as 7 agências consultaram cartórios de imóveis e órgãos do patrimônio e carimbaram FALSO por unanimidade.",

    scoreboard: [
      { count: 0, label: "VERDADEIRO", type: "true" },
      { count: 7, label: "FALSO / FAKE", type: "fake" },
      { count: 0, label: "OUTROS", type: "warn" }
    ],

    pressChecks: [
      {
        outlet: "G1 — Fato ou Fake",
        verdict: "#FAKE",
        stampClass: "stamp-fake",
        text: "Fake total: certidões dos órgãos e cartórios locais confirmam que não há nenhum registro dessa compra."
      },
      {
        outlet: "UOL Confere",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: é uma montagem falsa de redes sociais que já havia sido desmentida em apurações anteriores."
      },
      {
        outlet: "Estadão Verifica",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: boato reciclado sem suporte em nenhum documento ou registro público."
      },
      {
        outlet: "Agência Lupa",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: ausência total de lastro na realidade para essa alegação."
      }
    ],

    independentChecks: [
      {
        outlet: "Verifique os Fatos",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: buscas em cartórios de imóveis e patrimônio comprovam que a história não existe."
      },
      {
        outlet: "Pinóquio.live",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: montagem de internet fabricada sem nenhuma relação com patrimônio real."
      },
      {
        outlet: "Verifique a Verdade",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: não existe nenhuma transação financeira ou cartorial ligando o atleta citado ao movimento."
      }
    ],

    primarySources: [
      "Cartórios de Registro de Imóveis Litorâneos",
      "Secretaria do Patrimônio da União (SPU)"
    ]
  },

  {
    id: "CASO 05",
    tagId: "LEI • BENEFÍCIO",
    speaker: "Flávio Bolsonaro",
    speakerShort: "Flávio",
    blockTime: "Bloco 4 • 1:44:30",
    headline: "Piso permanente de R$ 600 do Auxílio",
    quote: "Nós aprovamos o piso permanente de 600 reais do Auxílio Brasil.",
    verdictBadge: "VALOR PERMANENTE NA LEI ERA R$ 400",
    stampClass: "consensus",

    theFact: "A lei permanente aprovada fixou o benefício em R$ 400. O bônus adicional de R$ 200 só valia até dezembro daquele ano eleitoral. Para o benefício continuar em R$ 600 no ano seguinte, foi necessária a aprovação de uma nova PEC após a eleição.",

    whyDiverge: "Praticamente todas as agências concordaram que a fala não é verdadeira: na letra da lei e no orçamento deixado para o ano seguinte, o valor permanente garantido era de apenas R$ 400.",

    scoreboard: [
      { count: 0, label: "VERDADEIRO", type: "true" },
      { count: 2, label: "FALSO", type: "fake" },
      { count: 3, label: "ENGANOSO / IMPRECISO", type: "warn" }
    ],

    pressChecks: [
      {
        outlet: "G1 — Fato ou Fake",
        verdict: "Não é Bem Assim",
        stampClass: "stamp-warn",
        text: "Não era permanente: os R$ 600 só valiam e tinham dinheiro garantido até dezembro do ano eleitoral."
      },
      {
        outlet: "Estadão Verifica",
        verdict: "Enganoso",
        stampClass: "stamp-warn",
        text: "Enganoso: a continuidade dos R$ 600 para o ano seguinte dependeu de outra votação aprovada após a eleição."
      },
      {
        outlet: "UOL Confere",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: a proposta de orçamento deixada pelo governo para o ano seguinte previa apenas R$ 405 de benefício médio."
      }
    ],

    independentChecks: [
      {
        outlet: "Verifique a Verdade",
        verdict: "Impreciso",
        stampClass: "stamp-warn",
        text: "Impreciso: a lei fixou o piso permanente em R$ 400. O acréscimo de R$ 200 tinha prazo certo para acabar em dezembro."
      },
      {
        outlet: "Pinóquio.live",
        verdict: "Falso",
        stampClass: "stamp-fake",
        text: "Falso: o projeto de orçamento federal enviado ao Congresso não previa pagar R$ 600 no ano seguinte."
      }
    ],

    primarySources: [
      "Lei Federal 14.342/2022 (Piso permanente de R$ 400)",
      "Emenda Constitucional 123/2022 (Bônus temporário de R$ 200)",
      "Projeto da Lei Orçamentária Federal (PLOA 2023)"
    ]
  }
];

let currentCaseIndex = 0;

function renderCaseTabs() {
  const container = document.getElementById("case-tabs");
  if (!container) return;
  container.innerHTML = "";

  DOSSIER_CASES.forEach((c, idx) => {
    const tab = document.createElement("button");
    tab.className = `tab-case-btn ${idx === currentCaseIndex ? "active" : ""}`;
    tab.setAttribute("role", "tab");
    tab.setAttribute("aria-selected", idx === currentCaseIndex ? "true" : "false");

    tab.innerHTML = `
      <div class="tab-meta-row">
        <span class="tab-case-id">${c.id}</span>
        <span class="tab-speaker-pill">${c.speakerShort}</span>
      </div>
      <div class="tab-case-headline">${c.headline}</div>
    `;

    tab.addEventListener("click", () => {
      if (currentCaseIndex !== idx) {
        currentCaseIndex = idx;
        renderCaseTabs();
        renderDossierCase(DOSSIER_CASES[currentCaseIndex]);
      }
    });

    container.appendChild(tab);
  });
}

function renderDossierCase(c) {
  const dossier = document.getElementById("active-case-dossier");
  if (!dossier) return;

  // Renderiza coluna dos Grandes Portais
  const pressHtml = c.pressChecks.map(item => `
    <div class="factcheck-article-item">
      <div class="article-item-top">
        <span class="outlet-name">${item.outlet}</span>
        <span class="editorial-stamp ${item.stampClass}">${item.verdict}</span>
      </div>
      <p class="article-excerpt">${item.text}</p>
    </div>
  `).join("");

  // Renderiza coluna dos Independentes
  const indepHtml = c.independentChecks.map(item => `
    <div class="factcheck-article-item">
      <div class="article-item-top">
        <span class="outlet-name">${item.outlet}</span>
        <span class="editorial-stamp ${item.stampClass}">${item.verdict}</span>
      </div>
      <p class="article-excerpt">${item.text}</p>
    </div>
  `).join("");

  // Renderiza pills do Placar
  const scoreboardHtml = c.scoreboard.filter(s => s.count > 0).map(s => `
    <span class="score-pill score-${s.type}">
      <strong>${s.count}</strong> ${s.label}
    </span>
  `).join("");

  // Renderiza tags de fontes oficiais
  const docsHtml = c.primarySources.map(s => `<span class="doc-tag">${s}</span>`).join("");

  dossier.innerHTML = `
    <!-- Topo do Dossiê com Título e Carimbo -->
    <div class="dossier-headline-block">
      <div>
        <span class="dossier-id-badge">${c.id} • ${c.tagId}</span>
        <h2 class="dossier-speaker-title">${c.speaker}</h2>
        <div class="dossier-context-line">${c.blockTime} • ${c.headline}</div>
      </div>
      <div>
        <span class="stamp-seal-badge ${c.stampClass}">[ ${c.verdictBadge} ]</span>
      </div>
    </div>

    <!-- 1. A Fala no Debate (Dignidade Editorial) -->
    <div class="transcript-statement-box">
      <div class="statement-eyebrow">A DECLARAÇÃO NO DEBATE:</div>
      <blockquote class="statement-quote">"${c.quote}"</blockquote>
    </div>

    <!-- 2. O Fato Real e o Placar Geral em Destaque -->
    <div class="fact-summary-banner">
      <div class="fact-summary-main">
        <span class="fact-badge">O FATO REAL</span>
        <p class="fact-text">${c.theFact}</p>
      </div>
      <div class="fact-scoreboard-box">
        <span class="scoreboard-title">PLACAR DAS 7 AGÊNCIAS</span>
        <div class="scoreboard-pills-list">
          ${scoreboardHtml}
        </div>
      </div>
    </div>

    <!-- 3. O Duelo em Duas Colunas da Gazeta -->
    <div class="comparison-duel-layout">
      <div class="duel-column">
        <div class="duel-column-header">
          <h3 class="column-entity-title">A Grande Imprensa</h3>
          <span class="column-meta-count">${c.pressChecks.length} veículos auditados</span>
        </div>
        <div class="column-articles-list">
          ${pressHtml}
        </div>
      </div>

      <div class="duel-column">
        <div class="duel-column-header">
          <h3 class="column-entity-title">Checadores Independentes</h3>
          <span class="column-meta-count">${c.independentChecks.length} veículos auditados</span>
        </div>
        <div class="column-articles-list">
          ${indepHtml}
        </div>
      </div>
    </div>

    <!-- 4. Caixa de Destaque: Por Que Discordam? -->
    <div class="auditor-memo-box">
      <div class="memo-header">
        <span>POR QUE AS AGÊNCIAS DISCORDAM NO VEREDITO?</span>
      </div>
      <p class="memo-text">${c.whyDiverge}</p>
    </div>

    <!-- 5. Documentos Oficiais -->
    <div class="dossier-evidence-strip">
      <span class="evidence-title">DOCUMENTOS OFICIAIS CONSULTADOS:</span>
      <div class="evidence-tag-list">
        ${docsHtml}
      </div>
    </div>
  `;
}

function setupThemeToggle() {
  const btn = document.getElementById("theme-toggle");
  if (btn) {
    btn.addEventListener("click", () => {
      document.body.classList.toggle("night-mode");
      const isNight = document.body.classList.contains("night-mode");
      btn.querySelector(".theme-btn-text").textContent = isNight ? "MODO PAPEL JORNAL" : "MODO TINTA NOTURNA";
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  renderCaseTabs();
  renderDossierCase(DOSSIER_CASES[0]);
  setupThemeToggle();
});
'''
INTERFACE_DIR.joinpath("app.js").write_text(app_js, encoding="utf-8")

# 3. ATUALIZAR styles.css COM ESTILOS COMPLETOS DO BROADSHEET + FACT BANNER
styles_css = r'''/* ==========================================================================
   A Checagem da Checagem — Gazeta de Auditoria Factual (Direção Editorial)
   Inspirado no design de publicações impressas de jornalismo investigativo.
   ========================================================================== */

:root {
  /* Tema Papel Jornal (Light Newsprint - Padrão) */
  --bg-paper: #f8f6f0;
  --bg-paper-alt: #f1ede2;
  --bg-highlight: #fff9db;
  --text-ink: #111216;
  --text-ink-secondary: #4a4d55;
  --text-ink-muted: #737782;
  --border-rule: #111216;
  --border-hairline: rgba(17, 18, 22, 0.16);
  
  /* Cores de Carimbos Editoriais */
  --stamp-red: #c92a2a;
  --stamp-red-bg: #ffe3e3;
  --stamp-green: #2b8a3e;
  --stamp-green-bg: #ebfbee;
  --stamp-amber: #d97706;
  --stamp-amber-bg: #fffbeb;

  /* Fontes */
  --font-serif: "Literata", "Charter", Georgia, "Times New Roman", serif;
  --font-sans: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;

  /* Geometria */
  --border-radius: 4px;
}

/* Modo Tinta Noturna (Dark Archival) */
body.night-mode {
  --bg-paper: #121316;
  --bg-paper-alt: #1a1c21;
  --bg-highlight: #252219;
  --text-ink: #f2ede4;
  --text-ink-secondary: #b5b0a5;
  --text-ink-muted: #807b70;
  --border-rule: #f2ede4;
  --border-hairline: rgba(242, 237, 228, 0.18);
  
  --stamp-red: #ff8787;
  --stamp-red-bg: rgba(201, 42, 42, 0.25);
  --stamp-green: #69db7c;
  --stamp-green-bg: rgba(43, 138, 62, 0.25);
  --stamp-amber: #fcc419;
  --stamp-amber-bg: rgba(217, 119, 6, 0.25);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-paper);
  color: var(--text-ink);
  font-family: var(--font-sans);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.gazette-container {
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 24px;
}

/* ==========================================================================
   CABEÇALHO DA GAZETA (MASTHEAD)
   ========================================================================== */

.gazette-header {
  border-bottom: 2px solid var(--border-rule);
  background-color: var(--bg-paper);
}

.gazette-top-strip {
  border-bottom: 1px solid var(--border-hairline);
  padding: 8px 0;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--text-ink-muted);
}

.strip-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}

.edition-tag {
  background-color: var(--border-rule);
  color: var(--bg-paper);
  padding: 2px 8px;
  border-radius: 2px;
}

.masthead {
  padding: 32px 24px 28px;
}

.masthead-main {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
  border-bottom: 3px double var(--border-rule);
  padding-bottom: 24px;
  margin-bottom: 20px;
}

.masthead-brand {
  flex: 1;
}

.newspaper-title {
  font-family: var(--font-serif);
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.05;
  color: var(--text-ink);
  margin-bottom: 8px;
  text-transform: uppercase;
}

.newspaper-deck {
  font-family: var(--font-serif);
  font-size: clamp(1.05rem, 1.8vw, 1.35rem);
  font-style: italic;
  color: var(--text-ink-secondary);
  line-height: 1.4;
  max-width: 820px;
}

.theme-toggle-btn {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-rule);
  color: var(--text-ink);
  padding: 10px 18px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  cursor: pointer;
  border-radius: var(--border-radius);
  min-height: 44px;
  min-width: 44px;
  transition: all 0.15s ease;
}

.theme-toggle-btn:hover {
  background-color: var(--border-rule);
  color: var(--bg-paper);
}

.theme-toggle-btn:focus-visible {
  outline: 2px solid var(--stamp-red);
  outline-offset: 2px;
}

.gazette-editorial-lead {
  max-width: 980px;
  font-size: 1.05rem;
  line-height: 1.65;
  color: var(--text-ink-secondary);
}

/* ==========================================================================
   LAYOUT PRINCIPAL
   ========================================================================== */

.docket-layout {
  padding: 36px 24px 60px;
}

/* ==========================================================================
   SELETOR DE CASOS (GUIAS DE PROCESSO / ABAS)
   ========================================================================== */

.docket-selector {
  margin-bottom: 28px;
}

.selector-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-hairline);
  margin-bottom: 12px;
}

.selector-title {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--text-ink-muted);
}

.selector-hint {
  font-size: 0.8rem;
  color: var(--text-ink-muted);
}

.case-tabs-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 8px;
}

.tab-case-btn {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  border-radius: var(--border-radius);
  padding: 12px 14px;
  text-align: left;
  cursor: pointer;
  min-height: 44px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: all 0.15s ease;
}

.tab-case-btn:hover {
  border-color: var(--border-rule);
  background-color: var(--bg-paper);
}

.tab-case-btn:active {
  transform: scale(0.99);
}

.tab-case-btn:focus-visible {
  outline: 2px solid var(--stamp-red);
  outline-offset: 2px;
}

.tab-case-btn.active {
  background-color: var(--border-rule);
  color: var(--bg-paper);
  border-color: var(--border-rule);
}

.tab-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.tab-case-id {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 700;
  opacity: 0.8;
}

.tab-speaker-pill {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
}

.tab-case-headline {
  font-family: var(--font-serif);
  font-size: 0.92rem;
  font-weight: 700;
  line-height: 1.3;
}

/* ==========================================================================
   O DOSSIÊ DO CASO ATIVO (THE CASE DOSSIER)
   ========================================================================== */

.case-dossier {
  background-color: var(--bg-paper);
  border: 2px solid var(--border-rule);
  border-radius: var(--border-radius);
  padding: 32px;
  box-shadow: 4px 4px 0px var(--border-rule);
  margin-bottom: 48px;
}

/* Cabeçalho do Dossiê */
.dossier-headline-block {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  border-bottom: 1px solid var(--border-rule);
  padding-bottom: 18px;
  margin-bottom: 24px;
}

.dossier-id-badge {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  background-color: var(--border-rule);
  color: var(--bg-paper);
  padding: 3px 8px;
  border-radius: 2px;
  display: inline-block;
  margin-bottom: 6px;
}

.dossier-speaker-title {
  font-family: var(--font-serif);
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--text-ink);
  letter-spacing: -0.02em;
}

.dossier-context-line {
  font-size: 0.88rem;
  color: var(--text-ink-secondary);
}

/* Carimbo Gráfico de Veredito do Dossiê */
.stamp-seal-badge {
  font-family: var(--font-mono);
  font-size: 0.88rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 8px 16px;
  border: 2px solid currentColor;
  border-radius: 2px;
  display: inline-flex;
  align-items: center;
  transform: rotate(-1deg);
}

.stamp-seal-badge.divergence {
  color: var(--stamp-red);
  background-color: var(--stamp-red-bg);
}

.stamp-seal-badge.consensus {
  color: var(--stamp-green);
  background-color: var(--stamp-green-bg);
}

/* Bloco da Frase Proferida (Dignidade de Gazeta) */
.transcript-statement-box {
  background-color: var(--bg-paper-alt);
  border-left: 4px solid var(--border-rule);
  padding: 18px 24px;
  margin-bottom: 20px;
  border-radius: var(--border-radius);
}

.statement-eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--text-ink-muted);
  margin-bottom: 6px;
  text-transform: uppercase;
}

.statement-quote {
  font-family: var(--font-serif);
  font-size: clamp(1.15rem, 2vw, 1.45rem);
  font-weight: 700;
  font-style: italic;
  line-height: 1.45;
  color: var(--text-ink);
}

/* ==========================================================================
   BANNER DE FATO REAL E PLACAR DAS AGÊNCIAS
   ========================================================================== */

.fact-summary-banner {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  border-left: 5px solid var(--stamp-green);
  border-radius: var(--border-radius);
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 18px;
}

.fact-summary-main {
  flex: 1 1 450px;
}

.fact-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--stamp-green);
  display: block;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.fact-text {
  font-size: 0.98rem;
  line-height: 1.55;
  color: var(--text-ink);
  font-weight: 500;
}

.fact-scoreboard-box {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 0 0 auto;
}

.scoreboard-title {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--text-ink-muted);
  text-transform: uppercase;
}

.scoreboard-pills-list {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
}

.score-pill {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 2px;
  border: 1.5px solid currentColor;
  letter-spacing: 0.04em;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

.score-pill strong {
  font-size: 0.92rem;
  font-weight: 800;
}

.score-pill.score-true {
  color: var(--stamp-green);
  background-color: var(--stamp-green-bg);
}

.score-pill.score-fake {
  color: var(--stamp-red);
  background-color: var(--stamp-red-bg);
}

.score-pill.score-warn {
  color: var(--stamp-amber);
  background-color: var(--stamp-amber-bg);
}

/* ==========================================================================
   CONFRONTO EM DUAS COLUNAS DE IMPRENSA
   ========================================================================== */

.comparison-duel-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  border-top: 1px solid var(--border-hairline);
  padding-top: 24px;
  margin-bottom: 24px;
}

@media (max-width: 860px) {
  .comparison-duel-layout {
    grid-template-columns: 1fr;
  }
}

.duel-column {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.duel-column-header {
  border-bottom: 2px solid var(--border-rule);
  padding-bottom: 8px;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.column-entity-title {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-ink);
  letter-spacing: -0.01em;
}

.column-meta-count {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-ink-muted);
}

.factcheck-article-item {
  border-bottom: 1px solid var(--border-hairline);
  padding-bottom: 14px;
}

.factcheck-article-item:last-child {
  border-bottom: none;
}

.article-item-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 6px;
}

.outlet-name {
  font-weight: 700;
  font-size: 0.92rem;
  color: var(--text-ink);
}

/* Carimbo Individual de Cada Checador */
.editorial-stamp {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  font-weight: 800;
  padding: 2px 8px;
  border: 1.5px solid currentColor;
  border-radius: 2px;
  letter-spacing: 0.04em;
  white-space: nowrap;
}

.editorial-stamp.stamp-true {
  color: var(--stamp-green);
  background-color: var(--stamp-green-bg);
}

.editorial-stamp.stamp-fake {
  color: var(--stamp-red);
  background-color: var(--stamp-red-bg);
}

.editorial-stamp.stamp-warn {
  color: var(--stamp-amber);
  background-color: var(--stamp-amber-bg);
}

.article-excerpt {
  font-size: 0.9rem;
  color: var(--text-ink-secondary);
  line-height: 1.55;
}

/* ==========================================================================
   A CAUSA DA DIVERGÊNCIA (MEMO DO AUDITOR)
   ========================================================================== */

.auditor-memo-box {
  background-color: var(--bg-highlight);
  border: 1px solid var(--border-hairline);
  border-left: 6px solid var(--border-rule);
  padding: 18px 22px;
  border-radius: var(--border-radius);
  margin-bottom: 24px;
}

.memo-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--text-ink);
  text-transform: uppercase;
}

.memo-text {
  font-size: 0.96rem;
  color: var(--text-ink);
  line-height: 1.6;
}

/* Fontes Oficiais Consultadas */
.dossier-evidence-strip {
  border-top: 1px solid var(--border-hairline);
  padding-top: 16px;
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 10px;
}

.evidence-title {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--text-ink-muted);
}

.evidence-tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.doc-tag {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  font-family: var(--font-mono);
  font-size: 0.76rem;
  padding: 3px 8px;
  color: var(--text-ink);
  border-radius: 2px;
}

/* ==========================================================================
   PAINEL METODOLÓGICO EDITORIAL (OS TRÊS PILARES)
   ========================================================================== */

.editorial-framework {
  border-top: 2px solid var(--border-rule);
  padding-top: 32px;
}

.framework-header {
  margin-bottom: 24px;
}

.framework-title {
  font-family: var(--font-serif);
  font-size: clamp(1.4rem, 2.5vw, 1.8rem);
  font-weight: 800;
  letter-spacing: -0.01em;
  color: var(--text-ink);
}

.framework-columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

@media (max-width: 860px) {
  .framework-columns {
    grid-template-columns: 1fr;
  }
}

.framework-card {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  border-radius: var(--border-radius);
  padding: 24px;
}

.card-num {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--stamp-red);
  margin-bottom: 8px;
  display: block;
}

.card-headline {
  font-family: var(--font-serif);
  font-size: 1.12rem;
  font-weight: 800;
  margin-bottom: 10px;
  line-height: 1.35;
  color: var(--text-ink);
}

.card-body {
  font-size: 0.92rem;
  color: var(--text-ink-secondary);
  line-height: 1.55;
}

/* ==========================================================================
   RODAPÉ DA GAZETA
   ========================================================================== */

.gazette-footer {
  border-top: 2px solid var(--border-rule);
  padding: 24px 0;
  background-color: var(--bg-paper);
  font-size: 0.85rem;
  color: var(--text-ink-secondary);
}

.footer-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.footer-meta {
  font-size: 0.78rem;
  color: var(--text-ink-muted);
  margin-top: 2px;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
'''
INTERFACE_DIR.joinpath("styles.css").write_text(styles_css, encoding="utf-8")
print(f"Arquivos da interface sincronizados e restaurados com timestamp {ts}!")
