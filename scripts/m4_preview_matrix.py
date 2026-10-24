import json

with open(r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

for r in rows:
    u = r['uol_verdict'][:10]
    g = r['g1_verdict'][:10]
    e = r['estadao_verdict'][:10]
    l = r['lupa_verdict'][:10]
    t = r['claim_title'][:35]
    print(f"[{r['claim_group_id']}] {t:35} | Veículos: {r['outlets_count']} | UOL: {u:10} | G1: {g:10} | EST: {e:10} | LUP: {l:10}")
