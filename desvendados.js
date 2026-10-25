/**
 * desvendados.js — Módulo de Integração das Visões #veiculos e #declaracoes
 * Baseado na engenharia reversa probatória do desvendados.com/checadores
 * 19 veículos auditados, 4 categorias analíticas e 224 declarações confrontadas.
 */

(function () {
  "use strict";

  // Estado global dos filtros das declarações
  const filterState = {
    candidate: "all",      // 'all' | 'flavio' | 'lula'
    group: "all",          // 'all' | 'newsrooms' | 'academic' | 'independent'
    antagonisticOnly: false,
    multipleOnly: false,
    query: ""
  };

  // Estado de ordenação da tabela de veículos
  // null = agrupado por categoria; 'flavio' = ordenado por % falso Flávio; 'lula' = ordenado por % falso Lula
  let outletSortCandidate = null;

  // Tooltip ativo
  let activeTooltipTarget = null;

  // Rótulos de veredito e abreviações
  const VERDICT_LABELS = {
    true: "Verdadeiro",
    partial: "Parcial / Impreciso",
    false: "Falso",
    unsupported: "Insustentável / Sem Dados"
  };

  const VERDICT_SHORT = {
    true: "V",
    partial: "P",
    false: "F",
    unsupported: "I"
  };

  const CONSENSUS_TITLES = {
    unanimous: "Classificação unânime",
    antagonistic: "Classificações antagônicas",
    close: "Avaliações próximas"
  };

  // ==========================================================================
  // ROTEAMENTO POR HASH (#veiculos, #declaracoes, #dossie)
  // ==========================================================================
  function initViewRouting() {
    const tabButtons = document.querySelectorAll(".btn-investigation-tab");
    const views = {
      dossie: document.getElementById("view-dossie"),
      veiculos: document.getElementById("view-veiculos"),
      declaracoes: document.getElementById("view-declaracoes")
    };

    function switchView(viewName, updateHash = true) {
      const validView = views[viewName] ? viewName : "dossie";

      tabButtons.forEach(btn => {
        const isMatch = btn.dataset.view === validView;
        btn.classList.toggle("active", isMatch);
        btn.setAttribute("aria-selected", isMatch ? "true" : "false");
        btn.tabIndex = isMatch ? 0 : -1;
      });

      Object.entries(views).forEach(([name, el]) => {
        if (!el) return;
        if (name === validView) {
          el.removeAttribute("hidden");
          el.style.display = "block";
        } else {
          el.setAttribute("hidden", "true");
          el.style.display = "none";
        }
      });

      if (updateHash) {
        const targetHash = validView === "dossie" ? "#dossie" : `#${validView}`;
        if (window.location.hash !== targetHash) {
          history.replaceState(null, "", targetHash);
        }
      }

      if (validView === "veiculos") {
        renderOutletTable();
      } else if (validView === "declaracoes") {
        renderClaimsMatrix();
      }
    }

    tabButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        switchView(btn.dataset.view, true);
      });
      btn.addEventListener("keydown", (e) => {
        if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
          e.preventDefault();
          const btns = Array.from(tabButtons);
          const idx = btns.indexOf(btn);
          const nextIdx = (idx + (e.key === "ArrowRight" ? 1 : -1) + btns.length) % btns.length;
          btns[nextIdx].focus();
          switchView(btns[nextIdx].dataset.view, true);
        }
      });
    });

    function handleHashChange() {
      const hash = window.location.hash.toLowerCase().replace("#", "");
      if (hash === "veiculos") {
        switchView("veiculos", false);
      } else if (hash === "declaracoes") {
        switchView("declaracoes", false);
      } else {
        switchView("dossie", false);
      }
    }

    window.addEventListener("hashchange", handleHashChange);
    handleHashChange();
  }

  // ==========================================================================
  // VISÃO 1: #veiculos — MATRIZ COMPARATIVA DE VEÍCULOS
  // ==========================================================================
  function renderOutletTable() {
    const tableEl = document.getElementById("outlet-table");
    if (!tableEl || !window.DESVENDADOS_OUTLETS) return;

    const outlets = window.DESVENDADOS_OUTLETS;
    const groups = window.DESVENDADOS_GROUPS;
    const utils = window.DESVENDADOS_UTILS;

    // Calcula totais de cada veículo
    const outletStats = outlets.map(o => ({
      outlet: o,
      flavio: utils.getOutletTotals(o, "flavio"),
      lula: utils.getOutletTotals(o, "lula")
    }));

    // Cria cabeçalho com botões de ordenação acessíveis
    const thead = document.createElement("thead");
    const trHead = document.createElement("tr");

    // Coluna Veículo
    const thOutlet = document.createElement("th");
    thOutlet.className = "th-outlet";
    const btnSortOutlet = document.createElement("button");
    btnSortOutlet.type = "button";
    btnSortOutlet.className = `btn-sort-column ${outletSortCandidate === null ? "active-sort" : ""}`;
    btnSortOutlet.setAttribute("aria-pressed", outletSortCandidate === null ? "true" : "false");
    btnSortOutlet.innerHTML = `
      <span class="sort-col-title">Veículo / Checador</span>
      <span class="sort-col-sub">${outletSortCandidate === null ? "agrupado por tipo" : "agrupar por tipo"}</span>
    `;
    btnSortOutlet.addEventListener("click", () => {
      outletSortCandidate = null;
      renderOutletTable();
    });
    thOutlet.appendChild(btnSortOutlet);

    // Coluna Flávio
    const thFlavio = document.createElement("th");
    thFlavio.className = "th-candidate th-flavio";
    const btnSortFlavio = document.createElement("button");
    btnSortFlavio.type = "button";
    btnSortFlavio.className = `btn-sort-column ${outletSortCandidate === "flavio" ? "active-sort" : ""}`;
    btnSortFlavio.setAttribute("aria-pressed", outletSortCandidate === "flavio" ? "true" : "false");
    btnSortFlavio.innerHTML = `
      <span class="sort-col-title">Flávio Bolsonaro</span>
      <span class="sort-col-sub">${outletSortCandidate === "flavio" ? "% falso ↓" : "% falso (ordenar)"}</span>
    `;
    btnSortFlavio.addEventListener("click", () => {
      outletSortCandidate = outletSortCandidate === "flavio" ? null : "flavio";
      renderOutletTable();
    });
    thFlavio.appendChild(btnSortFlavio);

    // Coluna Lula
    const thLula = document.createElement("th");
    thLula.className = "th-candidate th-lula";
    const btnSortLula = document.createElement("button");
    btnSortLula.type = "button";
    btnSortLula.className = `btn-sort-column ${outletSortCandidate === "lula" ? "active-sort" : ""}`;
    btnSortLula.setAttribute("aria-pressed", outletSortCandidate === "lula" ? "true" : "false");
    btnSortLula.innerHTML = `
      <span class="sort-col-title">Luiz Inácio Lula da Silva</span>
      <span class="sort-col-sub">${outletSortCandidate === "lula" ? "% falso ↓" : "% falso (ordenar)"}</span>
    `;
    btnSortLula.addEventListener("click", () => {
      outletSortCandidate = outletSortCandidate === "lula" ? null : "lula";
      renderOutletTable();
    });
    thLula.appendChild(btnSortLula);

    trHead.append(thOutlet, thFlavio, thLula);
    thead.appendChild(trHead);

    // Constrói linhas da tabela
    const tbody = document.createElement("tbody");

    function renderStatsCell(totals) {
      const td = document.createElement("td");
      td.className = "td-candidate-stats";

      if (!totals || totals.total === 0) {
        td.innerHTML = `<span class="empty-stats-note">sem checagens registradas</span>`;
        return td;
      }

      const falseRate = utils.calcFalseRate(totals);
      const falsePct = falseRate !== null ? Math.round(falseRate * 100) : 0;

      // Barra proporcional multi-segmento
      const barTrack = document.createElement("div");
      barTrack.className = "outlet-bar-track";
      barTrack.setAttribute("role", "progressbar");
      barTrack.setAttribute("aria-valuenow", String(falsePct));
      barTrack.setAttribute("aria-valuemin", "0");
      barTrack.setAttribute("aria-valuemax", "100");
      barTrack.setAttribute("title", `Falso: ${falsePct}%, Total: ${totals.total}`);

      const segments = [
        { key: "true", class: "seg-true", count: totals.true },
        { key: "partial", class: "seg-partial", count: totals.partial },
        { key: "false", class: "seg-false", count: totals.false },
        { key: "unsupported", class: "seg-unsupported", count: totals.unsupported }
      ];

      segments.forEach(seg => {
        if (seg.count > 0) {
          const s = document.createElement("span");
          s.className = `outlet-bar-seg ${seg.class}`;
          s.style.width = `${(seg.count / totals.total) * 100}%`;
          barTrack.appendChild(s);
        }
      });

      const metricRow = document.createElement("div");
      metricRow.className = "outlet-metric-row";
      metricRow.appendChild(barTrack);

      const ratePill = document.createElement("b");
      ratePill.className = "outlet-rate-num";
      ratePill.textContent = `${falsePct}%`;
      metricRow.appendChild(ratePill);

      const breakdown = document.createElement("div");
      breakdown.className = "outlet-breakdown-text";
      
      const countsText = [
        totals.true > 0 ? `${totals.true} V` : null,
        totals.partial > 0 ? `${totals.partial} P` : null,
        totals.false > 0 ? `${totals.false} F` : null,
        totals.unsupported > 0 ? `${totals.unsupported} I` : null
      ].filter(Boolean).join(" · ");

      breakdown.innerHTML = `<strong>${totals.total}</strong> checagens · <span class="breakdown-details">${countsText}</span>`;

      td.append(metricRow, breakdown);
      return td;
    }

    function createOutletRow(stat) {
      const tr = document.createElement("tr");
      tr.className = "outlet-row";

      // Coluna Nome / Descrição
      const tdOutlet = document.createElement("td");
      tdOutlet.className = "td-outlet-info";

      const nameSpan = document.createElement("span");
      nameSpan.className = "outlet-name-text";
      nameSpan.textContent = stat.outlet.name;

      const groupObj = groups.find(g => g.id === stat.outlet.group);
      const groupLabel = groupObj ? groupObj.shortName : "";

      const metaParts = [];
      if (stat.outlet.description) metaParts.push(stat.outlet.description);
      if (groupLabel && outletSortCandidate !== null) metaParts.push(groupLabel.toLowerCase());

      const metaSpan = document.createElement("span");
      metaSpan.className = "outlet-meta-text";
      metaSpan.textContent = metaParts.join(" · ");

      tdOutlet.append(nameSpan, metaSpan);

      // Colunas dos candidatos
      const tdFlavio = renderStatsCell(stat.flavio);
      const tdLula = renderStatsCell(stat.lula);

      tr.append(tdOutlet, tdFlavio, tdLula);
      return tr;
    }

    if (outletSortCandidate === null) {
      // Agrupado por categoria
      groups.forEach(g => {
        const groupStats = outletStats.filter(s => s.outlet.group === g.id);
        if (groupStats.length === 0) return;

        const trGroup = document.createElement("tr");
        trGroup.className = "outlet-group-header-row";
        const tdGroup = document.createElement("td");
        tdGroup.colSpan = 3;
        tdGroup.className = "td-group-header";
        tdGroup.textContent = g.name;
        trGroup.appendChild(tdGroup);
        tbody.appendChild(trGroup);

        groupStats.forEach(s => {
          tbody.appendChild(createOutletRow(s));
        });
      });
    } else {
      // Ordenado por taxa de falsidade do candidato selecionado (descendente)
      const cand = outletSortCandidate;
      const sorted = [...outletStats].sort((a, b) => {
        const rateA = utils.calcFalseRate(a[cand]) ?? -1;
        const rateB = utils.calcFalseRate(b[cand]) ?? -1;
        return rateB - rateA;
      });
      sorted.forEach(s => {
        tbody.appendChild(createOutletRow(s));
      });
    }

    tableEl.replaceChildren(thead, tbody);
  }

  // ==========================================================================
  // VISÃO 2: #declaracoes — MATRIZ DE DECLARAÇÕES E CONSENSO MULTIAGÊNCIA
  // ==========================================================================
  function renderClaimsMatrix() {
    const tableEl = document.getElementById("claim-table");
    const countEl = document.getElementById("claim-count");
    const tooltipEl = document.getElementById("claim-tooltip");
    if (!tableEl || !window.DESVENDADOS_CLAIMS) return;

    const allOutlets = window.DESVENDADOS_OUTLETS;
    const allClaims = window.DESVENDADOS_CLAIMS;
    const groups = window.DESVENDADOS_GROUPS;
    const utils = window.DESVENDADOS_UTILS;

    // Filtra veículos (exclui agregadores de placar pois não possuem veredito fala a fala)
    const activeOutlets = allOutlets.filter(o => {
      if (o.group === "aggregate") return false;
      if (filterState.group !== "all" && o.group !== filterState.group) return false;
      return true;
    });

    // Filtra e ordena as declarações
    const normQuery = utils.normalizeStr(filterState.query.trim());

    const filteredClaims = allClaims.filter(claim => {
      const ratings = utils.getClaimRatings(claim, activeOutlets);
      if (ratings.length === 0) return false;

      // Filtro de candidato
      if (filterState.candidate !== "all" && claim.candidate !== filterState.candidate) {
        return false;
      }

      const consensus = utils.getConsensus(claim, activeOutlets);

      // Filtro de divergência antagônica
      if (filterState.antagonisticOnly && consensus !== "antagonistic") {
        return false;
      }

      // Filtro de 2+ veículos
      if (filterState.multipleOnly && ratings.length < 2) {
        return false;
      }

      // Filtro de busca textual
      if (normQuery !== "" && !utils.normalizeStr(claim.text).includes(normQuery)) {
        return false;
      }

      return true;
    }).map((claim, idx) => ({
      claim,
      index: idx,
      count: utils.getClaimRatings(claim, activeOutlets).length
    })).sort((a, b) => {
      const candOrder = { flavio: 0, lula: 1 };
      const cDiff = (candOrder[a.claim.candidate] ?? 0) - (candOrder[b.claim.candidate] ?? 0);
      if (cDiff !== 0) return cDiff;
      if (b.count !== a.count) return b.count - a.count;
      return a.index - b.index;
    }).map(item => item.claim);

    if (countEl) {
      countEl.textContent = `${filteredClaims.length} declarações exibidas`;
    }

    // Gerenciamento de Tooltip
    function hideTooltip() {
      if (!tooltipEl) return;
      tooltipEl.hidden = true;
      if (activeTooltipTarget) {
        activeTooltipTarget.classList.remove("active-focus-cell");
        activeTooltipTarget = null;
      }
    }

    function positionTooltip(targetEl) {
      if (!tooltipEl) return;
      tooltipEl.hidden = false;
      const rect = targetEl.getBoundingClientRect();
      const tipWidth = tooltipEl.offsetWidth;
      const tipHeight = tooltipEl.offsetHeight;

      let left = rect.left + rect.width / 2 - tipWidth / 2;
      left = Math.max(10, Math.min(left, window.innerWidth - tipWidth - 10));

      const theadEl = tableEl.querySelector("thead");
      const theadBottom = theadEl ? theadEl.getBoundingClientRect().bottom : 80;

      let top = rect.top - tipHeight - 10;
      if (top < theadBottom + 8) {
        top = rect.bottom + 10;
      }

      tooltipEl.style.left = `${left}px`;
      tooltipEl.style.top = `${top}px`;
    }

    function showCellTooltip(cellEl, claimIdx, outletIdx) {
      const claim = filteredClaims[claimIdx];
      const outlet = activeOutlets[outletIdx];
      if (!claim || !outlet) return;

      const ratingData = claim.ratings[outlet.id];
      if (!ratingData) return;

      const [verdictCode, verdictText, note] = ratingData;

      hideTooltip();

      tooltipEl.innerHTML = `
        <div class="tooltip-header">
          <span class="tooltip-outlet-name">${outlet.name}</span>
          <span class="tooltip-verdict-badge badge-${verdictCode}">${verdictText || VERDICT_LABELS[verdictCode]}</span>
        </div>
        ${note ? `<div class="tooltip-note-body">${note}</div>` : ""}
      `;

      positionTooltip(cellEl);
      cellEl.classList.add("active-focus-cell");
      activeTooltipTarget = cellEl;
    }

    function showHeaderTooltip(thEl, outletIdx) {
      const outlet = activeOutlets[outletIdx];
      if (!outlet) return;

      const groupObj = groups.find(g => g.id === outlet.group);
      const groupName = groupObj ? groupObj.name : "";

      hideTooltip();

      tooltipEl.innerHTML = `
        <div class="tooltip-header">
          <span class="tooltip-outlet-name">${outlet.name}</span>
        </div>
        <div class="tooltip-note-body">${outlet.description || ""} · <em>${groupName}</em></div>
      `;

      positionTooltip(thEl);
      activeTooltipTarget = thEl;
    }

    // Constrói Colgroup para layout de tabela estável
    const colgroup = document.createElement("colgroup");
    const colClaim = document.createElement("col");
    colClaim.className = "col-claim-text";
    colgroup.appendChild(colClaim);

    activeOutlets.forEach(() => {
      const col = document.createElement("col");
      col.className = "col-outlet-cell";
      colgroup.appendChild(col);
    });

    // Constrói Cabeçalho Duplo da Tabela (Grupos + Siglas dos Veículos)
    const thead = document.createElement("thead");
    thead.className = "claims-matrix-thead";

    const trGroupRow = document.createElement("tr");
    trGroupRow.className = "tr-groups-header";

    const thClaimHead = document.createElement("th");
    thClaimHead.rowSpan = 2;
    thClaimHead.className = "th-claim-heading";
    thClaimHead.textContent = "Declaração Auditada";
    trGroupRow.appendChild(thClaimHead);

    groups.forEach(g => {
      const outletsInGroup = activeOutlets.filter(o => o.group === g.id);
      if (outletsInGroup.length === 0) return;

      const thGroup = document.createElement("th");
      thGroup.colSpan = outletsInGroup.length;
      thGroup.className = "th-group-title";
      thGroup.title = g.name;
      thGroup.textContent = g.compactName;
      trGroupRow.appendChild(thGroup);
    });

    const trOutletsRow = document.createElement("tr");
    trOutletsRow.className = "tr-outlets-header";

    activeOutlets.forEach((o, oIdx) => {
      const thO = document.createElement("th");
      thO.className = "th-outlet-abbr";
      thO.dataset.outletIdx = String(oIdx);
      thO.title = `${o.name} (${o.description || ""})`;

      const spanAbbr = document.createElement("span");
      spanAbbr.className = "outlet-vertical-abbr";
      spanAbbr.textContent = o.abbreviation || o.name.slice(0, 4);
      thO.appendChild(spanAbbr);

      trOutletsRow.appendChild(thO);
    });

    thead.append(trGroupRow, trOutletsRow);

    // Constrói Corpo da Tabela
    const tbody = document.createElement("tbody");
    tbody.className = "claims-matrix-tbody";

    let currentCandidate = null;

    if (filteredClaims.length === 0) {
      const trEmpty = document.createElement("tr");
      const tdEmpty = document.createElement("td");
      tdEmpty.colSpan = activeOutlets.length + 1;
      tdEmpty.className = "td-empty-claims";
      tdEmpty.textContent = "Nenhuma declaração encontrada com os filtros selecionados.";
      trEmpty.appendChild(tdEmpty);
      tbody.appendChild(trEmpty);
    } else {
      filteredClaims.forEach((claim, cIdx) => {
        // Separador de Candidato
        if (claim.candidate !== currentCandidate) {
          currentCandidate = claim.candidate;
          const trCand = document.createElement("tr");
          trCand.className = "tr-candidate-divider";
          const tdCand = document.createElement("td");
          tdCand.colSpan = activeOutlets.length + 1;
          tdCand.className = `td-candidate-title ${claim.candidate === "flavio" ? "cand-flavio" : "cand-lula"}`;
          
          const candCount = filteredClaims.filter(c => c.candidate === currentCandidate).length;
          tdCand.innerHTML = `
            <strong>${claim.candidate === "flavio" ? "Flávio Bolsonaro (PL)" : "Luiz Inácio Lula da Silva (PT)"}</strong>
            <span class="cand-claims-total">${candCount} declarações</span>
          `;
          trCand.appendChild(tdCand);
          tbody.appendChild(trCand);
        }

        const trRow = document.createElement("tr");
        trRow.className = "claim-matrix-row";

        // Célula da Declaração
        const tdClaim = document.createElement("td");
        tdClaim.className = "td-claim-content";

        const consensus = utils.getConsensus(claim, activeOutlets);
        if (consensus) {
          const badgeConsensus = document.createElement("span");
          badgeConsensus.className = `consensus-badge consensus-${consensus}`;
          badgeConsensus.textContent = CONSENSUS_TITLES[consensus];
          tdClaim.appendChild(badgeConsensus);
        }

        const textQuote = document.createElement("blockquote");
        textQuote.className = "claim-quote-text";
        textQuote.textContent = `“${claim.text}”`;
        tdClaim.appendChild(textQuote);

        // Sumário de checadores desta fala
        const dist = utils.getClaimDistribution(claim, activeOutlets);
        const distSpan = document.createElement("span");
        distSpan.className = "claim-distribution-meta";
        const metaParts = [`${dist.total} ${dist.total === 1 ? "veículo" : "veículos"}`];
        if (dist.true > 0) metaParts.push(`${dist.true} V`);
        if (dist.partial > 0) metaParts.push(`${dist.partial} P`);
        if (dist.false > 0) metaParts.push(`${dist.false} F`);
        if (dist.unsupported > 0) metaParts.push(`${dist.unsupported} I`);
        distSpan.textContent = metaParts.join(" · ");
        tdClaim.appendChild(distSpan);

        trRow.appendChild(tdClaim);

        // Células de cada veículo
        activeOutlets.forEach((outlet, oIdx) => {
          const tdCell = document.createElement("td");
          const ratingData = claim.ratings[outlet.id];

          if (ratingData) {
            const [verdictCode] = ratingData;
            tdCell.className = `td-verdict-cell cell-${verdictCode}`;
            tdCell.dataset.claimIdx = String(cIdx);
            tdCell.dataset.outletIdx = String(oIdx);
            tdCell.setAttribute("tabindex", "0");
            tdCell.setAttribute("role", "button");
            tdCell.setAttribute("aria-label", `${outlet.name}: ${ratingData[1] || VERDICT_LABELS[verdictCode]}`);
            tdCell.title = `${outlet.name}: ${ratingData[1] || VERDICT_LABELS[verdictCode]}`;

            const chip = document.createElement("span");
            chip.className = "cell-verdict-chip";
            chip.textContent = VERDICT_SHORT[verdictCode];
            tdCell.appendChild(chip);
          } else {
            tdCell.className = "td-verdict-cell cell-empty";
            tdCell.innerHTML = `<span class="cell-empty-dash">-</span>`;
          }

          trRow.appendChild(tdCell);
        });

        tbody.appendChild(trRow);
      });
    }

    tableEl.replaceChildren(colgroup, thead, tbody);

    // Eventos de Tooltip com Delegação e Suporte Acessível
    tableEl.addEventListener("mouseover", (e) => {
      const cell = e.target.closest("td[data-claim-idx]");
      const head = e.target.closest("th[data-outlet-idx]");
      if (cell) {
        showCellTooltip(cell, Number(cell.dataset.claimIdx), Number(cell.dataset.outletIdx));
      } else if (head) {
        showHeaderTooltip(head, Number(head.dataset.outletIdx));
      } else {
        hideTooltip();
      }
    });

    tableEl.addEventListener("click", (e) => {
      const cell = e.target.closest("td[data-claim-idx]");
      const head = e.target.closest("th[data-outlet-idx]");
      if (cell) {
        e.stopPropagation();
        showCellTooltip(cell, Number(cell.dataset.claimIdx), Number(cell.dataset.outletIdx));
      } else if (head) {
        e.stopPropagation();
        showHeaderTooltip(head, Number(head.dataset.outletIdx));
      }
    });

    tableEl.addEventListener("focusin", (e) => {
      const cell = e.target.closest("td[data-claim-idx]");
      if (cell) {
        showCellTooltip(cell, Number(cell.dataset.claimIdx), Number(cell.dataset.outletIdx));
      }
    });

    tableEl.addEventListener("mouseleave", hideTooltip);
    document.addEventListener("click", hideTooltip);
    window.addEventListener("scroll", hideTooltip, { passive: true });
  }

  // ==========================================================================
  // INICIALIZAÇÃO DOS FILTROS E CONTROLES DE #declaracoes
  // ==========================================================================
  function initClaimsControls() {
    // Filtro de candidato
    const candButtons = document.querySelectorAll("[data-claim-filter-candidate]");
    candButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        candButtons.forEach(b => {
          const isSelected = b === btn;
          b.classList.toggle("active", isSelected);
          b.setAttribute("aria-pressed", isSelected ? "true" : "false");
        });
        filterState.candidate = btn.dataset.claimFilterCandidate;
        renderClaimsMatrix();
      });
    });

    // Filtro de grupo de veículos
    const groupButtons = document.querySelectorAll("[data-claim-filter-group]");
    groupButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        groupButtons.forEach(b => {
          const isSelected = b === btn;
          b.classList.toggle("active", isSelected);
          b.setAttribute("aria-pressed", isSelected ? "true" : "false");
        });
        filterState.group = btn.dataset.claimFilterGroup;
        renderClaimsMatrix();
      });
    });

    // Toggle Antagônicos
    const chkAntagonistic = document.getElementById("claim-antagonistic-toggle");
    if (chkAntagonistic) {
      chkAntagonistic.addEventListener("change", () => {
        filterState.antagonisticOnly = chkAntagonistic.checked;
        renderClaimsMatrix();
      });
    }

    // Toggle Múltiplos Veículos
    const chkMultiple = document.getElementById("claim-multiple-toggle");
    if (chkMultiple) {
      chkMultiple.addEventListener("change", () => {
        filterState.multipleOnly = chkMultiple.checked;
        renderClaimsMatrix();
      });
    }

    // Busca Textual
    const searchInput = document.getElementById("claim-query-input");
    if (searchInput) {
      searchInput.addEventListener("input", () => {
        filterState.query = searchInput.value;
        renderClaimsMatrix();
      });
    }
  }

  // ==========================================================================
  // BOOTSTRAP AO CARREGAR O DOM
  // ==========================================================================
  document.addEventListener("DOMContentLoaded", () => {
    initViewRouting();
    initClaimsControls();
  });
})();
