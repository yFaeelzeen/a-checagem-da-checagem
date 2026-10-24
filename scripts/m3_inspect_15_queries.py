import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

m2_root = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
cat_json = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json')
with open(cat_json, 'r', encoding='utf-8') as f:
    items = json.load(f)

def search_text(kw_list):
    res = []
    for it in items:
        t = (it['alegacao_citada'] + ' ' + it['afirmacao_resumida'] + ' ' + it['justificativa_verificacao']).lower()
        if all(k in t for k in kw_list):
            res.append(it)
    return res

queries = [
    ('CASO-01 (11.500 obras)', ['11', 'obra']),
    ('CASO-02 (Lula herdou 6 mil)', ['6 mil', 'obra']),
    ('CASO-03 (Bolsonaro 14 mil e 8 mil)', ['14 mil', 'obra']),
    ('CASO-04 (Salário mínimo 900)', ['900', 'mínimo']),
    ('CASO-05 (Bolsonaro piso 600)', ['600', 'bolsa']),
    ('CASO-06 (Média Bolsa 190)', ['190', 'bolsa']),
    ('CASO-07 (BR-319 fazendo)', ['br-319']),
    ('CASO-08 (Túnel Santos-Guarujá)', ['santos-guarujá']),
    ('CASO-09 (Escala 6x1)', ['6x1']),
    ('CASO-10 (Reforma Tributária 28%)', ['28%', 'iva']),
    ('CASO-11 (Richarlison MST)', ['richarlison']),
    ('CASO-12 (Flávio Milícia)', ['milícia']),
    ('CASO-13 (Endividamento famílias)', ['devendo mais']),
    ('CASO-14 (Feminicídio recorde)', ['feminicídio']),
    ('CASO-15 (Cartão corporativo 100 anos)', ['cartão corporativo'])
]

for name, q in queries:
    matches = search_text(q)
    print(f'=== {name} ({len(matches)} matches) ===')
    for m in matches:
        print(f"  [{m['projeto_origem']}] ID={m['id_original']} CAND={m['candidato_original']} VERD={m['veredito_original']}")
        print(f"    Fala: {m['alegacao_citada'][:100]}")
        print(f"    Fontes: {m['fontes']}")
