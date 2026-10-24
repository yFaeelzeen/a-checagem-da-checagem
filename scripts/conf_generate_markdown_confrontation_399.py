import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

REPO = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'
in_json = os.path.join(REPO, '05_confronto_independentes_vs_portais', 'confronto_todas_399_checagens.json')
out_md = os.path.join(REPO, '05_confronto_independentes_vs_portais', 'confronto_exaustivo_399_declaracoes.md')

with open(in_json, 'r', encoding='utf-8') as f:
    records = json.load(f)

md_lines = []
md_lines.append("# Confronto Exaustivo: Todas as 399 Checagens Independentes vs. Grandes Portais\n")
md_lines.append("> **Debate Presidencial TV Globo (23/10/2026) — 2º Turno das Eleições 2026**\n")
md_lines.append("> Este documento confronta exaustivamente cada uma das **399 checagens individuais** dos projetos independentes (*Pinóquio.live*, *Verifique a Verdade* atualizado para 149 checagens e *Verifique os Fatos*) contra as verificações dos 4 grandes portais autorizados (*G1 — Fato ou Fake*, *UOL Confere*, *Estadão Verifica* e *Agência Lupa*).\n")
md_lines.append("---\n\n")

for r in records:
    cid = r['id_confronto']
    proj = r['projeto_independente']
    orig_id = r['id_original_independente']
    cand = r['candidato']
    decl = r['declaracao_independente'].strip()
    verdict = r['veredito_independente']
    just = r['justificativa_independente'].strip()
    
    portais = r['portais_correspondentes']
    
    md_lines.append(f"### {cid} — {cand} ({proj} | `{orig_id}`)\n\n")
    
    if portais:
        p0 = portais[0]
        md_lines.append("```text")
        md_lines.append(f"{'DECLARAÇÃO (' + proj + ')':<45} DECLARAÇÃO ({p0['veiculo']})")
        
        # Word wrap side by side
        d_ind = (decl[:42] + '...') if len(decl) > 42 else decl
        d_por = (p0['declaracao_portal'][:42] + '...') if len(p0['declaracao_portal']) > 42 else p0['declaracao_portal']
        md_lines.append(f"{d_ind:<45} {d_por}")
        
        v_ind = f"[{verdict}]"
        v_por = f"[{p0['classificacao_portal']}]"
        md_lines.append(f"{v_ind:<45} {v_por}")
        md_lines.append("```\n")
        
        md_lines.append(f"**Fala completa (Independente):** *\"{decl}\"*\n\n")
        md_lines.append(f"**Veredito Independente:** `{verdict}` — {just}\n\n")
        
        md_lines.append(f"**Correspondentes nos Grandes Portais ({len(portais)} encontrados):**\n\n")
        for p in portais:
            md_lines.append(f"- **{p['veiculo']}** (`{p['portal_id']}`): Veredito **`{p['classificacao_portal']}`**\n")
            md_lines.append(f"  - *Declaração:* \"{p['declaracao_portal']}\"\n")
            md_lines.append(f"  - *Justificativa:* {p['justificativa_portal']}\n")
            md_lines.append(f"  - *Termos coincidentes:* `{', '.join(p['termos_comuns'])}` (Score: {p['score_similaridade']})\n\n")
    else:
        md_lines.append("```text")
        md_lines.append(f"{'DECLARAÇÃO (' + proj + ')':<45} GRANDE PORTAL")
        d_ind = (decl[:42] + '...') if len(decl) > 42 else decl
        md_lines.append(f"{d_ind:<45} [Sem correspondente direto catalogado]")
        v_ind = f"[{verdict}]"
        md_lines.append(f"{v_ind:<45} [Não verificado pelos 4 portais]")
        md_lines.append("```\n")
        md_lines.append(f"**Fala completa (Independente):** *\"{decl}\"*\n\n")
        md_lines.append(f"**Veredito Independente:** `{verdict}` — {just}\n\n")
        md_lines.append("*Nota: Declaração coberta exclusivamente pelo ecossistema independente.*\n\n")
        
    md_lines.append("---\n\n")

with open(out_md, 'w', encoding='utf-8') as f:
    f.write(''.join(md_lines))

print(f"Salvo arquivo markdown de confronto com {len(records)} checagens em: {out_md}")
