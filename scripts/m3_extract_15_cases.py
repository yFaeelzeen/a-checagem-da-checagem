import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

m2_root = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
cat_json = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json')

with open(cat_json, 'r', encoding='utf-8') as f:
    items = json.load(f)

cases_to_find = [
    # 1. 11.500 obras paralisadas TCU (Flávio)
    ('CASO-01', 'obras_tcu_11500', lambda t: '11.500' in t or '11500' in t or '11.469' in t),
    # 2. Lula herdou 6 mil obras paralisadas (Lula)
    ('CASO-02', 'obras_herdou_6mil', lambda t: ('6 mil' in t or '6.000' in t) and 'obra' in t),
    # 3. Flávio pegou 14 mil e entregou com pouco mais de 8 mil obras (Flávio)
    ('CASO-03', 'obras_14mil_8mil', lambda t: '14 mil' in t and ('8 mil' in t or '8.603' in t)),
    # 4. Salário mínimo seria 900 sem reajustes acima da inflação (Lula)
    ('CASO-04', 'salario_minimo_900', lambda t: '900' in t and ('mínimo' in t or 'minimo' in t)),
    # 5. Bolsonaro que deu no mínimo R$ 600 do Bolsa Família (Flávio)
    ('CASO-05', 'bolsa_familia_600', lambda t: '600' in t and ('bolsa família' in t or 'bolsa familia' in t or 'auxílio' in t or 'auxilio' in t)),
    # 6. Média do Bolsa Família no governo Lula era R$ 190 (Flávio)
    ('CASO-06', 'bolsa_familia_190', lambda t: '190' in t and ('bolsa' in t or 'família' in t or 'familia' in t)),
    # 7. BR-319 que "estamos fazendo" (Lula)
    ('CASO-07', 'br319_fazendo', lambda t: 'br-319' in t or 'br 319' in t),
    # 8. Túnel Santos-Guarujá quem está colocando dinheiro somos nós (Lula)
    ('CASO-08', 'tunel_santos_guaruja', lambda t: 'santos-guarujá' in t or 'santos guaruja' in t or 'túnel santos' in t or 'tunel santos' in t),
    # 9. Aprovamos o fim da escala 6x1 (Lula)
    ('CASO-09', 'escala_6x1', lambda t: '6x1' in t),
    # 10. Reforma tributária: IVA estimado em 28% a maior do mundo (Flávio)
    ('CASO-10', 'reforma_tributaria_iva', lambda t: '28%' in t or ('iva' in t and 'alíquota' in t)),
    # 11. Richarlison comprou ilha do MST (Flávio)
    ('CASO-11', 'richarlison_mst', lambda t: 'richarlison' in t or ('ilha' in t and 'mst' in t)),
    # 12. Flávio nunca foi investigado por envolvimento com milícia (Flávio)
    ('CASO-12', 'flavio_investigacao_milicia', lambda t: 'milícia' in t or 'milicia' in t),
    # 13. Endividamento das famílias / devendo mais no atual governo (Flávio)
    ('CASO-13', 'endividamento_familias', lambda t: 'devendo mais' in t or ('endividamento' in t and 'família' in t)),
    # 14. Feminicídio / violência contra mulher aumento/queda (Flávio/Lula)
    ('CASO-14', 'feminicidio', lambda t: 'feminicídio' in t or 'feminicidio' in t),
    # 15. Gastos com cartões corporativos / sigilo de 100 anos (Lula)
    ('CASO-15', 'cartao_corporativo', lambda t: 'cartão corporativo' in t or 'cartao corporativo' in t)
]

found_cases = {}
for cid, cname, predicate in cases_to_find:
    found_cases[cid] = {'name': cname, 'matches': []}
    for it in items:
        full_text = (it.get('alegacao_citada', '') + ' ' + it.get('afirmacao_resumida', '') + ' ' + it.get('justificativa_verificacao', '')).lower()
        if predicate(full_text):
            found_cases[cid]['matches'].append(it)

print('=== 15 CASES DISCOVERY ===')
for cid, data in found_cases.items():
    projs = set(x['projeto_origem'] for x in data['matches'])
    print(f"{cid} [{data['name']}]: {len(data['matches'])} matches in projects {projs}")
