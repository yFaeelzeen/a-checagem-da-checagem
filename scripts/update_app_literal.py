# Script para atualizar interface com informações literais e de fácil assimilação
from pathlib import Path

INTERFACE_DIR = Path(r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface")

# 1. ATUALIZAR app.js
app_js_content = r'''// Casos Auditados do Dossiê "A Checagem da Checagem" — Versão com Linguagem Literal e Clara
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
      { count: 1, label: "ENGANOSO / FALTA CONTEXTO", type: "warn" }
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
      { count: 3, label: "FALTA CONTEXTO / INSUSTENTÁVEL", type: "warn" }
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

  // Renderiza badges do Placar Geral
  const scoreboardHtml = c.scoreboard.filter(s => s.count > 0).map(s => `
    <span class="score-pill score-${s.type}">
      <strong>${s.count}</strong> ${s.label}
    </span>
  `).join("");

  // Renderiza tags de fontes oficiais
  const docsHtml = c.primarySources.map(s => `<span class="doc-tag">${s}</span>`).join("");

  dossier.innerHTML = `
    <!-- Topo do Caso -->
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

    <!-- Painel Literal: Ficha Direta em 3 Fatos Claros -->
    <div class="literal-summary-panel">
      <!-- 1. O que foi dito -->
      <div class="literal-entry quote-entry">
        <div class="entry-label">O QUE FOI DITO NO DEBATE:</div>
        <blockquote class="entry-quote">"${c.quote}"</blockquote>
      </div>

      <!-- 2. O Fato Real -->
      <div class="literal-entry fact-entry">
        <div class="entry-label label-fact">O FATO REAL (O QUE DIZEM OS DOCUMENTOS):</div>
        <p class="entry-body">${c.theFact}</p>
      </div>

      <!-- 3. Por que discordam -->
      <div class="literal-entry conflict-entry">
        <div class="entry-label label-conflict">POR QUE AS AGÊNCIAS DISCORDAM NO VEREDITO?</div>
        <p class="entry-body">${c.whyDiverge}</p>
      </div>
    </div>

    <!-- Barra do Placar Geral das 7 Agências -->
    <div class="scoreboard-strip">
      <span class="scoreboard-title">PLACAR GERAL DAS AGÊNCIAS:</span>
      <div class="scoreboard-pills-list">
        ${scoreboardHtml}
      </div>
    </div>

    <!-- O Confronto em Duas Colunas -->
    <div class="comparison-duel-layout">
      <div class="duel-column">
        <div class="duel-column-header">
          <h3 class="column-entity-title">A Grande Imprensa</h3>
          <span class="column-meta-count">${c.pressChecks.length} veículos</span>
        </div>
        <div class="column-articles-list">
          ${pressHtml}
        </div>
      </div>

      <div class="duel-column">
        <div class="duel-column-header">
          <h3 class="column-entity-title">Checadores Independentes</h3>
          <span class="column-meta-count">${c.independentChecks.length} veículos</span>
        </div>
        <div class="column-articles-list">
          ${indepHtml}
        </div>
      </div>
    </div>

    <!-- Fontes Oficiais -->
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

INTERFACE_DIR.joinpath("app.js").write_text(app_js_content, encoding="utf-8")
print("app.js atualizado com sucesso!")
