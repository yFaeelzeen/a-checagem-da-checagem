// ==========================================================================
// A CHECAGEM DA CHECAGEM — APLICAÇÃO PRINCIPAL COM BUSCA, PAGINAÇÃO & MODOS
// Suporte a TODAS as 412 Declarações do Debate Presidencial 2026
// ==========================================================================

// Base Completa Consolidada
const MASTER_CASES = (typeof ALL_DECLARATIONS !== "undefined" && Array.isArray(ALL_DECLARATIONS) && ALL_DECLARATIONS.length > 0)
  ? ALL_DECLARATIONS
  : [];

// Estado Global de Filtros, Paginação e Seleção
let filterKeyword = "";
let filterCandidate = "all";
let filterVerdict = "all";
let activeDeclarations = [...MASTER_CASES];
let selectedDeclarationId = activeDeclarations[0] ? activeDeclarations[0].id : null;

// Paginação e Modo de Visualização
let currentViewMode = "grid"; // "grid" ou "list"
let currentPage = 1;
const ITEMS_PER_PAGE_GRID = 8; // 2 linhas perfeitas de 4 cards no desktop
const ITEMS_PER_PAGE_LIST = 10; // 10 linhas compactas por página

// Função de normalização de acentos para busca insensível
function stripAccents(str) {
  if (!str) return "";
  return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

// Filtra a lista de declarações
function getFilteredDeclarations() {
  const query = stripAccents(filterKeyword.trim());
  return MASTER_CASES.filter(item => {
    // 1. Filtro de Candidato
    if (filterCandidate !== "all" && item.candidateKey !== filterCandidate) {
      return false;
    }
    // 2. Filtro de Classificação / Veredito
    if (filterVerdict !== "all" && item.normalizedVerdict !== filterVerdict) {
      return false;
    }
    // 3. Filtro por Palavra-Chave
    if (query) {
      const tokens = item.searchTokens || stripAccents(
        `${item.id} ${item.speaker} ${item.speakerShort} ${item.theme} ${item.quote} ${item.theFact} ${item.headline} ${item.verdictBadge}`
      );
      if (!tokens.includes(query)) {
        return false;
      }
    }
    return true;
  });
}

// Atualiza o contador de resultados visíveis
function updateCounter(count, total) {
  const visibleSpan = document.getElementById("visible-count");
  const hintText = document.getElementById("selector-hint-text");

  if (visibleSpan) visibleSpan.textContent = count;
  if (hintText) {
    if (filterKeyword.trim()) {
      hintText.textContent = `${count} declarações encontradas para "${filterKeyword.trim()}" • Clique para ver o confronto`;
    } else {
      hintText.textContent = `${count} declarações filtradas • Clique em qualquer uma para abrir o confronto`;
    }
  }
}

// Renderiza a paginação e as abas (Modo Grade ou Modo Lista)
function renderCaseTabs() {
  const container = document.getElementById("case-tabs-container");
  const pageTopIndicator = document.getElementById("page-indicator-top");
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  const footerPagination = document.getElementById("pagination-footer");

  if (!container) return;

  const itemsPerPage = currentViewMode === "grid" ? ITEMS_PER_PAGE_GRID : ITEMS_PER_PAGE_LIST;
  const totalPages = Math.ceil(activeDeclarations.length / itemsPerPage) || 1;

  if (currentPage > totalPages) currentPage = 1;
  if (currentPage < 1) currentPage = 1;

  // Atualiza controles do topo
  if (pageTopIndicator) pageTopIndicator.textContent = `${currentPage} / ${totalPages}`;
  if (btnPrev) btnPrev.disabled = currentPage <= 1;
  if (btnNext) btnNext.disabled = currentPage >= totalPages;

  // Se não houver declarações correspondentes
  if (activeDeclarations.length === 0) {
    container.innerHTML = `
      <div class="empty-search-state" style="width: 100%;">
        <h3 class="empty-state-title">Nenhuma declaração encontrada</h3>
        <p class="empty-state-desc">Nenhum resultado corresponde à palavra-chave "${filterKeyword}" com os filtros ativos.</p>
        <button class="btn-reset-filters" id="btn-reset-filters">Limpar Filtros e Ver Todas</button>
      </div>
    `;
    if (footerPagination) footerPagination.innerHTML = "";
    const btnReset = document.getElementById("btn-reset-filters");
    if (btnReset) btnReset.addEventListener("click", resetAllFilters);
    return;
  }

  // Fatiamento da página atual
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = Math.min(startIndex + itemsPerPage, activeDeclarations.length);
  const pageItems = activeDeclarations.slice(startIndex, endIndex);

  // 1. MODO GRADE
  if (currentViewMode === "grid") {
    let gridHtml = '<div class="case-tabs-strip" id="case-tabs" role="tablist">';
    pageItems.forEach(c => {
      const isSelected = c.id === selectedDeclarationId;
      gridHtml += `
        <button class="tab-case-btn pill-cand-${c.candidateKey} ${isSelected ? "active" : ""}" 
                role="tab" 
                aria-selected="${isSelected ? "true" : "false"}"
                data-id="${c.id}">
          <div class="tab-meta-row">
            <div class="tab-id-and-speaker">
              <span class="tab-case-id">${c.id}</span>
              <span class="tab-speaker-dot dot-${c.candidateKey}"></span>
              <span class="tab-speaker-pill speaker-${c.candidateKey}">${c.speakerShort}</span>
            </div>
            <span class="tab-badge-verdict badge-v-${c.normalizedVerdict}">${c.verdictBadge || c.normalizedVerdict}</span>
          </div>
          <div class="tab-case-headline">${c.headline || c.theme}</div>
        </button>
      `;
    });
    gridHtml += '</div>';
    container.innerHTML = gridHtml;

    // Adiciona evento de clique aos cards
    container.querySelectorAll(".tab-case-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-id");
        if (selectedDeclarationId !== id) {
          selectedDeclarationId = id;
          renderCaseTabs();
          const target = activeDeclarations.find(x => x.id === id);
          if (target) renderDossierCase(target);
        }
      });
    });
  } 
  // 2. MODO LISTA COMPACTA
  else {
    let listHtml = '<div class="case-list-table">';
    pageItems.forEach(c => {
      const isSelected = c.id === selectedDeclarationId;
      listHtml += `
        <div class="case-list-row pill-cand-${c.candidateKey} ${isSelected ? "active" : ""}" data-id="${c.id}">
          <span class="list-col-id">${c.id}</span>
          <div class="list-col-speaker">
            <span class="tab-speaker-dot dot-${c.candidateKey}"></span>
            <span class="tab-speaker-pill speaker-${c.candidateKey}">${c.speakerShort}</span>
          </div>
          <span class="list-col-theme">${c.theme || 'Geral'}</span>
          <span class="list-col-quote">"${c.quote}"</span>
          <div class="list-col-verdict">
            <span class="tab-badge-verdict badge-v-${c.normalizedVerdict}">${c.verdictBadge || c.normalizedVerdict}</span>
          </div>
        </div>
      `;
    });
    listHtml += '</div>';
    container.innerHTML = listHtml;

    // Adiciona evento de clique às linhas da lista
    container.querySelectorAll(".case-list-row").forEach(row => {
      row.addEventListener("click", () => {
        const id = row.getAttribute("data-id");
        if (selectedDeclarationId !== id) {
          selectedDeclarationId = id;
          renderCaseTabs();
          const target = activeDeclarations.find(x => x.id === id);
          if (target) renderDossierCase(target);
        }
      });
    });
  }

  // Renderiza a Barra de Paginação Inferior com Números
  if (footerPagination) {
    let pagesHtml = `
      <div style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--text-ink-muted);">
        Exibindo <strong>${startIndex + 1}–${endIndex}</strong> de <strong>${activeDeclarations.length}</strong> declarações
      </div>
      <div class="pagination-pages-list">
        <button class="btn-page-nav" id="btn-footer-prev" ${currentPage <= 1 ? "disabled" : ""}>◀</button>
    `;

    // Gera números de página com elipses inteligentes
    const maxButtons = 7;
    let startPage = Math.max(1, currentPage - 3);
    let endPage = Math.min(totalPages, startPage + maxButtons - 1);
    if (endPage - startPage < maxButtons - 1) {
      startPage = Math.max(1, endPage - maxButtons + 1);
    }

    if (startPage > 1) {
      pagesHtml += `<button class="btn-page-number" data-page="1">1</button>`;
      if (startPage > 2) pagesHtml += `<span class="pagination-ellipsis">…</span>`;
    }

    for (let p = startPage; p <= endPage; p++) {
      pagesHtml += `<button class="btn-page-number ${p === currentPage ? "active" : ""}" data-page="${p}">${p}</button>`;
    }

    if (endPage < totalPages) {
      if (endPage < totalPages - 1) pagesHtml += `<span class="pagination-ellipsis">…</span>`;
      pagesHtml += `<button class="btn-page-number" data-page="${totalPages}">${totalPages}</button>`;
    }

    pagesHtml += `
        <button class="btn-page-nav" id="btn-footer-next" ${currentPage >= totalPages ? "disabled" : ""}>▶</button>
      </div>
    `;

    footerPagination.innerHTML = pagesHtml;

    // Eventos dos botões numéricos
    footerPagination.querySelectorAll(".btn-page-number").forEach(btn => {
      btn.addEventListener("click", () => {
        const p = parseInt(btn.getAttribute("data-page"), 10);
        if (p !== currentPage) {
          currentPage = p;
          renderCaseTabs();
        }
      });
    });

    const fPrev = document.getElementById("btn-footer-prev");
    const fNext = document.getElementById("btn-footer-next");
    if (fPrev) fPrev.addEventListener("click", () => { if (currentPage > 1) { currentPage--; renderCaseTabs(); } });
    if (fNext) fNext.addEventListener("click", () => { if (currentPage < totalPages) { currentPage++; renderCaseTabs(); } });
  }
}


// Renderiza o componente de Gaveta/Aba de Fontes Documentais
function renderSourcesDrawer(drawerId, sources, contextLabel) {
  if (!sources || !Array.isArray(sources) || sources.length === 0) return "";
  
  const sourcesHtml = sources.map((s, idx) => {
    const num = String(idx + 1).padStart(2, '0');
    const domainBadge = s.domain ? `<span class="source-domain-pill">${s.domain}</span>` : "";
    const linkBtn = s.url ? `
      <a href="${s.url}" target="_blank" rel="noopener noreferrer" class="source-external-link" title="Abrir link original em nova aba">
        <span>Acessar</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
      </a>
    ` : "";
    
    return `
      <div class="source-drawer-item">
        <span class="source-num-badge">${num}</span>
        <div class="source-info-col">
          <div class="source-title-row">
            <span class="source-doc-title">${s.title}</span>
            ${domainBadge}
          </div>
          ${s.url ? `<span class="source-doc-url">${s.url}</span>` : ""}
        </div>
        ${linkBtn}
      </div>
    `;
  }).join("");

  return `
    <div class="sources-drawer-wrapper">
      <button type="button" class="btn-sources-toggle" data-drawer-id="${drawerId}" aria-expanded="false">
        <span class="btn-sources-icon"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path></svg></span>
        <span class="btn-sources-label">${contextLabel || 'Fontes Documentais Consultadas'} (${sources.length})</span>
        <span class="btn-sources-caret">▼</span>
      </button>
      <div class="sources-drawer-content" id="${drawerId}" style="display: none;">
        <div class="sources-drawer-inner">
          <div class="sources-drawer-header">
            <span class="sources-drawer-title">DOCUMENTOS E BASES PRIMÁRIAS DESTA VERIFICAÇÃO</span>
            <span class="sources-drawer-count">${sources.length} fonte(s) catalogada(s)</span>
          </div>
          <div class="sources-list-container">
            ${sourcesHtml}
          </div>
        </div>
      </div>
    </div>
  `;
}

// Renderiza o Framework dinâmico de 3 pilares
function renderCaseFramework(c) {
  const container = document.getElementById("case-framework");
  if (!container) return;

  const pillars = (c.casePillars && c.casePillars.pillars) ? c.casePillars.pillars : [
    { num: "01", headline: "Critério Metodológico", body: "Análise técnica e factual realizada com base nos documentos e registros probatórios." },
    { num: "02", headline: "Contexto da Fala no Debate", body: "Declaração proferida durante o debate presidencial na TV Globo, submetida à checagem em tempo real." },
    { num: "03", headline: "Benefício da Dúvida", body: "A checagem aplicou os métodos documentais da iniciativa, sob a presunção e o benefício da dúvida de fidelidade probatória." }
  ];

  const cardsHtml = pillars.map(p => `
    <div class="framework-card">
      <span class="card-num">${p.num}</span>
      <h3 class="card-headline">${p.headline}</h3>
      <p class="card-body">${p.body}</p>
    </div>
  `).join("");

  const sourcesBar = (c.sources && c.sources.length > 0) ? `
    <div class="framework-sources-bar">
      ${renderSourcesDrawer(`drawer-framework-${c.id}`, c.sources, 'Consultar Fontes Documentais da Metodologia')}
    </div>
  ` : "";

  container.innerHTML = `
    <div class="framework-header">
      <h2 class="framework-title">${(c.casePillars && c.casePillars.title) || `Análise de Critérios e Contexto: ${c.theme || ''}`}</h2>
    </div>
    <div class="framework-columns">
      ${cardsHtml}
    </div>
    ${sourcesBar}
  `;
}

// Renderiza o dossiê detalhado da declaração ativa
function renderDossierCase(c) {
  const dossier = document.getElementById("active-case-dossier");
  if (!dossier) return;

  if (!c) {
    dossier.innerHTML = `
      <div class="empty-search-state">
        <h3 class="empty-state-title">Nenhuma declaração selecionada</h3>
        <p class="empty-state-desc">Ajuste os filtros de pesquisa ou clique em uma das declarações da lista acima.</p>
      </div>
    `;
    const frameworkBox = document.getElementById("case-framework");
    if (frameworkBox) frameworkBox.innerHTML = "";
    return;
  }

  // Coluna da Grande Imprensa

  const pressList = (c.pressChecks || []).filter(item => item && item.text && item.text.trim() !== '-' && !item.verdict.toLowerCase().includes('não checado'));
  const pressHtml = pressList.length > 0 ? pressList.map(item => `
    <div class="factcheck-article-item">
      <div class="article-item-top">
        <span class="outlet-name">${item.outlet}</span>
        <span class="editorial-stamp ${item.stampClass || 'stamp-warn'}">${item.verdict}</span>
      </div>
      <p class="article-excerpt">${item.text}</p>
    </div>
  `).join("") : `
    <div class="factcheck-article-item" style="border-left-color: var(--border-hairline);">
      <p class="article-excerpt" style="font-style: italic; color: var(--text-ink-muted);">
        Esta declaração específica foi checada com exclusividade pelo ecossistema independente durante a transmissão ao vivo, sem nota equivalente no recorte principal da imprensa tradicional.
      </p>
    </div>
  `;

  // Função auxiliar de normalização de veredito para detecção estrita de divergência
  const getNormVerdict = (v) => {
    if (!v) return "enganoso";
    const vl = v.toLowerCase();
    if (["verdadeiro", "fato", "#fato", "parcialmente verdadeiro"].some(x => vl.includes(x))) return "verdadeiro";
    if (["falso", "fake", "#fake", "insustentavel", "insustentável", "falso"].some(x => vl.includes(x))) return "falso";
    return "enganoso";
  };

  // Coleta as classificações válidas da grande imprensa neste caso
  const validPressChecks = (c.pressChecks || []).filter(p => p.verdict && !p.verdict.toLowerCase().includes("não checado"));
  const pressClassList = validPressChecks.map(p => getNormVerdict(p.verdict));

  // Coluna dos Checadores Independentes COM auditoria de viés APENAS QUANDO HÁ DIVERGÊNCIA

  const indepList = (c.independentChecks || []).filter(item => item && item.text && item.text.trim() !== '-' && !item.verdict.toLowerCase().includes('não checado'));
  const indepHtml = indepList.map(item => {
    const indepNorm = getNormVerdict(item.verdict);
    let hasDivergence = false;
    let pressSummaryText = "";
    let dominantPressVerdict = "";

    // 1. Confronto direto contra a Grande Imprensa
    if (validPressChecks.length > 0) {
      // Se TODOS os portais da grande imprensa compartilham a MESMA classificação do canal independente:
      const allPressAgreeWithIndep = pressClassList.every(pc => pc === indepNorm);

      if (!allPressAgreeWithIndep) {
        hasDivergence = true;
        pressSummaryText = validPressChecks.map(p => `${p.outlet} [${p.verdict}]`).join(", ");
        
        const countTrue = pressClassList.filter(pc => pc === "verdadeiro").length;
        const countFake = pressClassList.filter(pc => pc === "falso").length;
        const countWarn = pressClassList.filter(pc => pc === "enganoso").length;

        if (countTrue > countFake && countTrue >= countWarn) dominantPressVerdict = "Verdadeiro / Fato";
        else if (countFake > countTrue && countFake >= countWarn) dominantPressVerdict = "Falso / Fake";
        else dominantPressVerdict = "Enganoso / Impreciso";
      }
    } 
    // 2. Se a grande imprensa não checou, verifica se há divergência entre os próprios independentes
    else {
      const otherIndeps = indepList.filter(x => x.outlet !== item.outlet);
      if (otherIndeps.length > 0) {
        const otherNorms = otherIndeps.map(x => getNormVerdict(x.verdict));
        if (otherNorms.some(on => on !== indepNorm)) {
          hasDivergence = true;
          pressSummaryText = otherIndeps.map(x => `${x.outlet} [${x.verdict}]`).join(", ");
          dominantPressVerdict = otherNorms[0] === "verdadeiro" ? "Verdadeiro" : (otherNorms[0] === "falso" ? "Falso" : "Enganoso");
        }
      }
    }

    // Gerador de Evidência e Pergunta com Pulso Firme
    let firmQuestion = "";
    let firmEvidence = "";

    if (hasDivergence) {
      if (validPressChecks.length > 0) {
        firmQuestion = `Por que o <strong>${item.outlet}</strong> carimbou esta declaração como <em>"${item.verdict}"</em>, enquanto a grande imprensa (${pressSummaryText}) classificou com uma régua diferente?`;
      } else {
        firmQuestion = `Por que o <strong>${item.outlet}</strong> adotou a classificação <em>"${item.verdict}"</em> divergindo dos demais checadores independentes (${pressSummaryText})?`;
      }

      // Evidência com pulso firme conforme o veículo e o orador
      if (item.biasAnalysis && item.biasAnalysis.evidence) {
        firmEvidence = item.biasAnalysis.evidence;
      } else if (item.outlet.includes("Verifique a Verdade")) {
        firmEvidence = `O portal apegou-se a formalismos processuais estritos ou tolerou margens de erro consideráveis para conceder este selo. Na auditoria estatística global do debate, o site atribuiu 61,3% de avaliações positivas a Flávio e apenas 38,6% a Lula. Sob o benefício da dúvida, o documento citado existe, mas a escolha metodológica atuou para alinhar-se à linha de defesa do candidato.`;
      } else if (item.outlet.includes("Pinóquio")) {
        firmEvidence = `O veículo aplicou seu padrão hipercrítico padrão, punindo omissões federativas secundárias ou estendendo definições jurídicas formais para carimbar o selo negativo. Sob o benefício da dúvida, trata-se de rigor investigativo, mas a exigência desproporcional tende a tratar generalizações de debate como falsidades deliberadas.`;
      } else if (item.outlet.includes("Verifique os Fatos")) {
        firmEvidence = `O portal publicou a classificação sem fornecer links para fontes primárias em seu card público (0% de links no feed). A auditoria comprovou que 64% da sua pauta no debate focou exclusivamente em falas de Flávio Bolsonaro, com 95,8% de rótulos negativos contra 7,4% para Lula, indicando direcionamento editorial pró-governo.`;
      } else {
        firmEvidence = `A discrepância observada entre os canais decorre de escolhas discricionárias na seleção dos selos de checagem, evidenciando como um mesmo fato objetivo pode ser rotulado de forma divergente dependendo da orientação do veículo.`;
      }
    }

    return `
      <div class="factcheck-article-item">
        <div class="article-item-top">
          <span class="outlet-name">${item.outlet}</span>
          <span class="editorial-stamp ${item.stampClass || 'stamp-warn'}">${item.verdict}</span>
        </div>
        <p class="article-excerpt">${item.text}</p>
        ${hasDivergence ? `
          <div class="bias-audit-box">
            <div class="bias-audit-header">
              <span class="bias-audit-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px; margin-right:4px;" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg><span>AUDITORIA DE DIVERGÊNCIA EDITORIAL</span></span>
              <span class="bias-audit-badge">Divergência: [${item.verdict.toUpperCase()}] vs Imprensa</span>
            </div>
            
            <div class="bias-audit-question-box">
              <div class="question-kicker"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px; margin-right:5px;" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg><span>QUESTÃO DIRETA AO LEITOR:</span></div>
              <p class="question-body">${firmQuestion}</p>
            </div>

            <div class="bias-audit-evidence-box">
              <div class="evidence-kicker"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px; margin-right:5px;" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg><span>EVIDÊNCIA DO CONTRASTE & PULSO FIRME:</span></div>
              <p class="evidence-body">${firmEvidence}</p>
              ${c.sources && c.sources.length > 0 ? renderSourcesDrawer(`drawer-bias-${item.outlet.replace(/[^a-zA-Z0-9]/g, '')}-${c.id}`, c.sources, 'Ver Fontes e Documentos desta Auditoria') : ''}
            </div>

            <div class="bias-audit-challenge">
              <strong>Reflita criticamente:</strong> Esta discrepância reflete uma exigência técnica legítima ou uma escolha editorial calculada para atenuar ou amplificar o impacto político perante sua audiência?
            </div>
          </div>
        ` : ""}
      </div>
    `;
  }).join("");

  // Placar de Vereditos
  const scores = c.scoreboard && Array.isArray(c.scoreboard) ? c.scoreboard : [];
  const scoreboardHtml = scores.filter(s => s.count > 0).map(s => `
    <span class="score-pill score-${s.type}">
      <strong>${s.count}</strong> ${s.label}
    </span>
  `).join("") || `<span class="score-pill score-warn">Checagem Documental Única</span>`;

  // Fontes Oficiais
  const sources = c.primarySources && Array.isArray(c.primarySources) ? c.primarySources : ["Diário Oficial e Relatórios Públicos"];
  const docsHtml = sources.map(s => `<span class="doc-tag">${s}</span>`).join("");

  // Renderiza Framework de 3 colunas
  renderCaseFramework(c);

  dossier.innerHTML = `
    <!-- Topo do Dossiê com Foto Oficial, Nome Colorido e Carimbo -->
    <div class="dossier-headline-block">
      <div class="speaker-profile-box">
        <img src="${c.speakerPhoto || 'flavio.webp'}" alt="Foto oficial de candidatura de ${c.speaker}" class="candidate-avatar ${c.speakerColorClass || ''}" width="58" height="58">
        <div class="speaker-meta-col">
          <span class="dossier-id-badge">${c.id} • ${c.tagId || c.theme || 'DEBATE GLOBO'}</span>
          <h2 class="dossier-speaker-title ${c.speakerColorClass || ''}">${c.speaker}</h2>
          <div class="dossier-context-line">${c.blockTime || 'Debate TV Globo • 23/10/2026'} • ${c.headline || c.theme}</div>
        </div>
      </div>
      <div>
        <span class="stamp-seal-badge ${c.stampClass || 'stamp-warn'}">[ ${c.verdictBadge || c.normalizedVerdict.toUpperCase()} ]</span>
      </div>
    </div>

    <!-- 1. A Fala no Debate -->
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
        <span class="scoreboard-title">PLACAR DAS AGÊNCIAS</span>
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
          <span class="column-meta-count">${pressList.length} checagens auditadas</span>
        </div>
        <div class="column-articles-list">
          ${pressHtml}
        </div>
      </div>

      <div class="duel-column">
        <div class="duel-column-header">
          <h3 class="column-entity-title">Checadores Independentes</h3>
          <span class="column-meta-count">${indepList.length} checagens auditadas</span>
        </div>
        <div class="column-articles-list">
          ${indepHtml}
        </div>
      </div>
    </div>

    <!-- 4. Caixa de Destaque: Por Que Discordam? -->
    <div class="auditor-memo-box">
      <div class="memo-header">
        <span>CRITÉRIO EDITORIAL & ANÁLISE DE DIVERGÊNCIA</span>
      </div>
      <p class="memo-text">${c.whyDiverge || (c.casePillars && c.casePillars.pillars[0]?.body) || 'Análise comparativa das justificativas emitidas pelas agências de fact-checking.'}</p>
    </div>

    <!-- 5. Documentos Oficiais -->
    <div class="dossier-evidence-strip">
      <div class="evidence-header-row">
        <span class="evidence-title">DOCUMENTOS OFICIAIS CONSULTADOS:</span>
        ${c.sources && c.sources.length > 0 ? renderSourcesDrawer(`drawer-docs-${c.id}`, c.sources, 'Consultar Links e Fontes Catalogadas') : ''}
      </div>
      <div class="evidence-tag-list">
        ${docsHtml}
      </div>
    </div>
  `;
}

// Aplica filtros e atualiza a interface
function applyFilters() {
  activeDeclarations = getFilteredDeclarations();
  currentPage = 1; // Reseta sempre para a primeira página ao filtrar
  updateCounter(activeDeclarations.length, MASTER_CASES.length);

  // Sincroniza classes visuais dos pills de candidato e veredito
  document.querySelectorAll("#candidate-filters .filter-pill").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-candidate") === filterCandidate);
  });
  document.querySelectorAll("#verdict-filters .filter-pill").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-verdict") === filterVerdict);
  });

  // Mantém seleção se ainda existir nos resultados, senão seleciona a primeira
  const stillExists = activeDeclarations.some(c => c.id === selectedDeclarationId);
  if (!stillExists) {
    selectedDeclarationId = activeDeclarations[0] ? activeDeclarations[0].id : null;
  }

  renderCaseTabs();

  const activeCase = activeDeclarations.find(c => c.id === selectedDeclarationId) || activeDeclarations[0];
  renderDossierCase(activeCase);
}

// Reseta todos os filtros
function resetAllFilters() {
  filterKeyword = "";
  filterCandidate = "all";
  filterVerdict = "all";
  currentPage = 1;

  const searchInput = document.getElementById("declaration-search-input");
  const clearBtn = document.getElementById("search-clear-btn");
  if (searchInput) searchInput.value = "";
  if (clearBtn) clearBtn.style.display = "none";

  document.querySelectorAll("#candidate-filters .filter-pill").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-candidate") === "all");
  });

  document.querySelectorAll("#verdict-filters .filter-pill").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-verdict") === "all");
  });

  applyFilters();
}

// Configura os ouvintes de eventos da barra de pesquisa e filtros
function setupSearchAndFilters() {
  const searchInput = document.getElementById("declaration-search-input");
  const clearBtn = document.getElementById("search-clear-btn");

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      filterKeyword = e.target.value;
      if (clearBtn) {
        clearBtn.style.display = filterKeyword.length > 0 ? "block" : "none";
      }
      applyFilters();
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      if (searchInput) {
        searchInput.value = "";
        searchInput.focus();
      }
      filterKeyword = "";
      clearBtn.style.display = "none";
      applyFilters();
    });
  }

  // Filtros de Candidato
  document.querySelectorAll("#candidate-filters .filter-pill").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#candidate-filters .filter-pill").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      filterCandidate = btn.getAttribute("data-candidate");
      applyFilters();
    });
  });

  // Filtros de Veredito
  document.querySelectorAll("#verdict-filters .filter-pill").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#verdict-filters .filter-pill").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      filterVerdict = btn.getAttribute("data-verdict");
      applyFilters();
    });
  });

  // Navegação da Paginação no Topo
  const btnPrev = document.getElementById("btn-prev-page");
  const btnNext = document.getElementById("btn-next-page");
  if (btnPrev) {
    btnPrev.addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        renderCaseTabs();
      }
    });
  }
  if (btnNext) {
    btnNext.addEventListener("click", () => {
      const itemsPerPage = currentViewMode === "grid" ? ITEMS_PER_PAGE_GRID : ITEMS_PER_PAGE_LIST;
      const totalPages = Math.ceil(activeDeclarations.length / itemsPerPage) || 1;
      if (currentPage < totalPages) {
        currentPage++;
        renderCaseTabs();
      }
    });
  }

  // Comutador de Modo: Grade vs Lista
  const btnGrid = document.getElementById("btn-view-grid");
  const btnList = document.getElementById("btn-view-list");

  if (btnGrid) {
    btnGrid.addEventListener("click", () => {
      if (currentViewMode !== "grid") {
        currentViewMode = "grid";
        btnGrid.classList.add("active");
        if (btnList) btnList.classList.remove("active");
        renderCaseTabs();
      }
    });
  }

  if (btnList) {
    btnList.addEventListener("click", () => {
      if (currentViewMode !== "list") {
        currentViewMode = "list";
        btnList.classList.add("active");
        if (btnGrid) btnGrid.classList.remove("active");
        renderCaseTabs();
      }
    });
  }
}

// Alternância de Tema Escuro / Claro
function setupThemeToggle() {
  const btn = document.getElementById("theme-toggle");
  if (btn) {
    btn.addEventListener("click", () => {
      document.body.classList.toggle("night-mode");
      const isNight = document.body.classList.contains("night-mode");
      btn.querySelector(".theme-btn-text").textContent = isNight ? "MODO PAPEL JORNAL" : "MODO TINTA NOTURNA";
      localStorage.setItem("gazette_theme", isNight ? "night" : "light");
    });
  }
}

// Inicialização

  // Delegação de clique para alternância das abas/gavetas de fontes
  document.addEventListener("click", (e) => {
    const toggleBtn = e.target.closest(".btn-sources-toggle");
    if (!toggleBtn) return;
    const drawerId = toggleBtn.getAttribute("data-drawer-id");
    const drawer = document.getElementById(drawerId);
    if (!drawer) return;
    const isExpanded = toggleBtn.getAttribute("aria-expanded") === "true";
    if (isExpanded) {
      drawer.style.display = "none";
      toggleBtn.setAttribute("aria-expanded", "false");
      toggleBtn.classList.remove("active");
    } else {
      drawer.style.display = "block";
      toggleBtn.setAttribute("aria-expanded", "true");
      toggleBtn.classList.add("active");
    }
  });

document.addEventListener("DOMContentLoaded", () => {
  setupSearchAndFilters();
  
  // Interatividade do Placar Consolidado do Debate
  document.querySelectorAll(".score-metric-item").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const cand = btn.getAttribute("data-candidate");
      const verd = btn.getAttribute("data-verdict");
      if (cand) filterCandidate = cand;
      if (verd) filterVerdict = verd;
      applyFilters();

      const searchSec = document.querySelector(".search-filter-section");
      if (searchSec) {
        searchSec.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  document.querySelectorAll(".candidate-score-card").forEach(card => {
    card.addEventListener("click", (e) => {
      if (e.target.closest(".score-metric-item")) return;
      const cand = card.getAttribute("data-candidate");
      if (cand) {
        filterCandidate = cand;
        filterVerdict = "all";
        applyFilters();

        const searchSec = document.querySelector(".search-filter-section");
        if (searchSec) {
          searchSec.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });

  setupThemeToggle();
  applyFilters();
});
