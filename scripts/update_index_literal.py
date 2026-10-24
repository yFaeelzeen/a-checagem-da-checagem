# Script para atualizar index.html e styles.css com linguagem literal e direta
from pathlib import Path

INTERFACE_DIR = Path(r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface")

# 1. ATUALIZAR index.html
index_html = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A Checagem da Checagem — Dossiê de Auditoria Factual 2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400..900;1,7..72,400..700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
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

  <script src="app.js"></script>
</body>
</html>
'''

INTERFACE_DIR.joinpath("index.html").write_text(index_html, encoding="utf-8")
print("index.html atualizado com sucesso!")
