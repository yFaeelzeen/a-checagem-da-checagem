# Script para adicionar estilos literais ao styles.css
from pathlib import Path

CSS_FILE = Path(r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface\styles.css")
content = CSS_FILE.read_text(encoding="utf-8")

old_transcript_section = r'''/* Bloco da Frase Taquigráfica Proferida */
.transcript-statement-box {
  background-color: var(--bg-paper-alt);
  border-left: 4px solid var(--border-rule);
  padding: 18px 24px;
  margin-bottom: 28px;
}

.statement-eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--text-ink-muted);
  margin-bottom: 6px;
}

.statement-quote {
  font-family: var(--font-serif);
  font-size: clamp(1.15rem, 2vw, 1.45rem);
  font-weight: 700;
  font-style: italic;
  line-height: 1.45;
  color: var(--text-ink);
}'''

new_literal_section = r'''/* ==========================================================================
   PAINEL LITERAL (FICHA DIRETA: FALA, FATO REAL E MOTIVO DA DISCORDÂNCIA)
   ========================================================================== */

.literal-summary-panel {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 22px;
}

.literal-entry {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  border-left: 5px solid var(--border-rule);
  border-radius: var(--border-radius);
  padding: 16px 20px;
  transition: background-color 0.15s ease;
}

.literal-entry.quote-entry {
  border-left-color: var(--border-rule);
  background-color: var(--bg-paper-alt);
}

.literal-entry.fact-entry {
  border-left-color: var(--stamp-green);
  background-color: var(--stamp-green-bg);
}

.literal-entry.conflict-entry {
  border-left-color: var(--stamp-amber);
  background-color: var(--stamp-amber-bg);
}

.entry-label {
  font-family: var(--font-mono);
  font-size: 0.73rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--text-ink-muted);
  margin-bottom: 6px;
  text-transform: uppercase;
}

.entry-label.label-fact {
  color: var(--stamp-green);
}

.entry-label.label-conflict {
  color: var(--stamp-amber);
}

.entry-quote {
  font-family: var(--font-serif);
  font-size: clamp(1.15rem, 1.8vw, 1.35rem);
  font-weight: 700;
  font-style: italic;
  line-height: 1.45;
  color: var(--text-ink);
}

.entry-body {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-ink);
  font-weight: 500;
}

/* ==========================================================================
   BARRA DO PLACAR GERAL DAS AGÊNCIAS
   ========================================================================== */

.scoreboard-strip {
  background-color: var(--bg-paper-alt);
  border: 1px solid var(--border-hairline);
  border-radius: var(--border-radius);
  padding: 12px 18px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 26px;
}

.scoreboard-title {
  font-family: var(--font-mono);
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--text-ink-muted);
}

.scoreboard-pills-list {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.score-pill {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 3px;
  border: 1.5px solid currentColor;
  letter-spacing: 0.04em;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.score-pill strong {
  font-size: 0.95rem;
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

/* Compatibilidade com classes anteriores */
.transcript-statement-box {
  background-color: var(--bg-paper-alt);
  border-left: 4px solid var(--border-rule);
  padding: 18px 24px;
  margin-bottom: 28px;
}

.statement-eyebrow {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--text-ink-muted);
  margin-bottom: 6px;
}

.statement-quote {
  font-family: var(--font-serif);
  font-size: clamp(1.15rem, 2vw, 1.45rem);
  font-weight: 700;
  font-style: italic;
  line-height: 1.45;
  color: var(--text-ink);
}'''

if old_transcript_section in content:
    content = content.replace(old_transcript_section, new_literal_section)
    CSS_FILE.write_text(content, encoding="utf-8")
    print("styles.css atualizado com sucesso!")
else:
    print("Aviso: old_transcript_section não encontrada diretamente.")
