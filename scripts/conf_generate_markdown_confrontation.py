import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'
in_json = os.path.join(out_dir, 'confronto_todas_382_checagens.json')

with open(in_json, 'r', encoding='utf-8') as f:
    records = json.load(f)

md_path = os.path.join(out_dir, 'CONFRONTO_EXAUSTIVO_382_DECLARACOES.md')

lines = [
    '# Confronto Exaustivo das 382 Checagens Independentes com os Grandes Portais',
    '',
    '- **Data da Auditoria:** 24 de outubro de 2026',
    '- **Total de Checagens Auditadas:** **382 checagens individuais** (175 Pinóquio.live + 132 Verifique a Verdade + 75 Verifique os Fatos).',
    '- **Universo dos Portais de Confronto:** 219 checagens individuais (*Estadão Verifica*, *G1 — Fato ou Fake*, *Agência Lupa* e *UOL Confere*).',
    '- **Resultado Geral do Pareamento:**',
    '  - **315 checagens (82,5%)** foram também abordadas e checadas por 1 ou mais grandes portais.',
    '  - **67 checagens (17,5%)** foram exclusivas dos checadores independentes (temas hiperespecíficos ou minutagem secundária).',
    '',
    '---',
    '',
    '## Estrutura do Confronto por Declaração',
    'Abaixo estão apresentadas as checagens com a identificação exata do site de origem, o texto da fala, a classificação atribuída e o espelhamento correspondente nos grandes portais.',
    ''
]

for idx, r in enumerate(records):
    ind_num = idx + 1
    proj = r['indep_projeto']
    cand = r['candidato']
    ind_quote = r['indep_declaracao'].strip().replace('|', '/')
    ind_verd = r['indep_veredito']
    ind_just = r['indep_justificativa'].strip().replace('|', '/').replace('\n', ' ')
    portais = r['portais_pareados']
    
    portal_names = ", ".join(portais.keys()) if portais else "Nenhum grande portal checou esta fala na amostra"
    
    if portais:
        portal_quotes = "<br><br>".join([f"**[{v}]**: *{p['declaracao'].strip().replace('|', '/')}*" for v, p in portais.items()])
        portal_verdicts = "<br>".join([f"**[{v}]**: `{p['veredito']}`" for v, p in portais.items()])
        portal_justs = "<br><br>".join([f"**[{v}]**: {p['justificativa'][:250].strip().replace('|', '/').replace(chr(10), ' ')}..." for v, p in portais.items()])
    else:
        portal_quotes = "-"
        portal_verdicts = "-"
        portal_justs = "Sem registro nos portais autorizados."
        
    lines.append(f'### DECLARAÇÃO {ind_num:03d} — {cand.upper()}')
    lines.append('')
    lines.append('| Dimensão | SITE INDEPENDENTE | GRANDE(S) PORTAL(IS) CORRESPONDENTE(S) |')
    lines.append('| :--- | :--- | :--- |')
    lines.append(f'| **Origem do Veículo** | **{proj}** | {portal_names} |')
    lines.append(f'| **O que foi falado** | *"{ind_quote}"* | {portal_quotes} |')
    lines.append(f'| **Classificação / Veredito** | **`{ind_verd}`** | {portal_verdicts} |')
    lines.append(f'| **Resumo da Justificativa** | {ind_just[:350]}... | {portal_justs} |')
    lines.append('')
    lines.append('---')
    lines.append('')

with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Salvo {md_path} com sucesso.")
