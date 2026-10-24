import os, sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

m2_root = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
cat_json = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json')

with open(cat_json, 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f'Total items: {len(items)}')

topics = {
    'obras_paralisadas': ['obra', 'tcu', 'paralisada', 'parada', '8 mil', '11.500', '14 mil', '11500'],
    'cartao_corporativo': ['cartão corporativo', 'cartao corporativo', 'sigilo de 100 anos'],
    'divida_inadimplencia': ['endividamento', 'inadimplência', 'inadimplencia', 'desenrola', 'nome sujo'],
    'salario_minimo_inflacao': ['salário mínimo', 'salario minimo', '900', 'inflação', 'poder de compra', 'reajuste'],
    'bolsa_familia': ['bolsa família', 'bolsa familia', '600', '190', 'auxílio brasil'],
    'br319_transposicao': ['br-319', 'br 319', 'transposição', 'transposicao', 'são francisco', 'santos-guarujá'],
    'pac_investimentos': ['pac', '1,7 trilhão', '1,7 tri', 'investimento'],
    'seguranca_milicia': ['milícia', 'milicia', 'segurança', 'homicídio', 'polícia', 'cv', 'pcc'],
    'agro_exportacao': ['agro', 'exportação', 'exportacao', 'superávit', 'balança comercial', 'plano safra'],
    'escala_6x1': ['escala 6x1', '6x1', 'fim da escala'],
    'tributaria_iva': ['tributária', 'tributaria', 'iva', '28%'],
    'richarlison_mst': ['richarlison', 'mst', 'ilha'],
    'feminicidio': ['feminicídio', 'feminicidio', 'mulher'],
    'pedagio_motos': ['pedágio', 'pedagio', 'moto'],
    'fome_33_milhoes': ['fome', '33 milhões', 'mapa da fome']
}

matches = {k: [] for k in topics}

for it in items:
    text = (it.get('alegacao_citada', '') + ' ' + it.get('afirmacao_resumida', '')).lower()
    for top, kws in topics.items():
        if any(kw in text for kw in kws):
            matches[top].append({
                'project': it['projeto_origem'],
                'id': it['id_original'],
                'candidate': it['candidato_original'],
                'verdict': it['veredito_original'],
                'quote': it['alegacao_citada'][:100]
            })

for top, m in matches.items():
    projs = set(x['project'] for x in m)
    print(f'Topic: {top:25} -> {len(m):2} occurrences across {len(projs)} projects: {projs}')
