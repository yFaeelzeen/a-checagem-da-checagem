import os, sys, json, csv, re
sys.stdout.reconfigure(encoding='utf-8')

m2_cat_path = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925\06_RELATORIOS_CONSOLIDADOS\catalogo_estruturado_checagens_consolidado.json'
m4_ind_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\02_CHECAGENS_INDIVIDUAIS.json'

with open(m2_cat_path, 'r', encoding='utf-8') as f:
    indep_records = json.load(f)

with open(m4_ind_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)

# Define 20 key themes with search regex / keywords to link claims across both sides
claim_clusters = [
    {
        'id': 'CONF-01',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'TCU acaba de soltar relatório apontando mais de 11.500 obras paralisadas no atual governo',
        'kws': ['11.500', '11.469', '11500', '11,5 mil']
    },
    {
        'id': 'CONF-02',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Lula',
        'alegacao_resumo': 'Lula herdou 6.000 obras paralisadas deixadas pelo governo anterior',
        'kws': ['6.000', '6 mil', 'herdou 6', '6000 obras']
    },
    {
        'id': 'CONF-03',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Governo Bolsonaro pegou 14 mil obras paralisadas e entregou com pouco mais de 8 mil',
        'kws': ['14 mil', '8 mil', '8.603']
    },
    {
        'id': 'CONF-04',
        'tema': 'Programas Sociais',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Foi Bolsonaro que deu o piso de no mínimo R$ 600 do Bolsa Família',
        'kws': ['600', 'bolsa família', 'auxílio brasil']
    },
    {
        'id': 'CONF-05',
        'tema': 'Programas Sociais',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Média do Bolsa Família nos governos do PT era de R$ 190',
        'kws': ['190', 'bolsa família', 'média']
    },
    {
        'id': 'CONF-06',
        'tema': 'Infraestrutura / Meio Ambiente',
        'candidato': 'Lula',
        'alegacao_resumo': 'Estamos fazendo a rodovia BR-319 (Porto Velho - Manaus)',
        'kws': ['br-319', 'br 319', 'porto velho', 'manaus']
    },
    {
        'id': 'CONF-07',
        'tema': 'Infraestrutura Portuária',
        'candidato': 'Lula',
        'alegacao_resumo': 'No túnel Santos-Guarujá quem está colocando dinheiro para fazer somos nós',
        'kws': ['túnel', 'tunel', 'santos-guarujá', 'santos guaruja']
    },
    {
        'id': 'CONF-08',
        'tema': 'Trabalho e Legislação',
        'candidato': 'Lula',
        'alegacao_resumo': 'Nós aprovamos o fim da escala 6x1',
        'kws': ['6x1', 'escala']
    },
    {
        'id': 'CONF-09',
        'tema': 'Economia / Reforma Tributária',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'IVA começa a ser cobrado no ano que vem com alíquota estimada em 28%, a maior do mundo',
        'kws': ['iva', '28%', 'alíquota', 'carga tributária']
    },
    {
        'id': 'CONF-10',
        'tema': 'Agronegócio / Política',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Jogador Richarlison comprou uma ilha de integrantes do MST',
        'kws': ['richarlison', 'ilha', 'mst']
    },
    {
        'id': 'CONF-11',
        'tema': 'Segurança e Investigações',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Flávio afirma que nunca foi investigado por causa de envolvimento com milícia',
        'kws': ['milícia', 'milicia', 'escritório do crime']
    },
    {
        'id': 'CONF-12',
        'tema': 'Economia e Salário Mínimo',
        'candidato': 'Lula',
        'alegacao_resumo': 'Sem os reajustes acima da inflação do PT, salário mínimo seria de apenas R$ 900',
        'kws': ['900', 'salário mínimo', 'salario minimo', 'inpc']
    },
    {
        'id': 'CONF-13',
        'tema': 'Desenvolvimento Social / Fome',
        'candidato': 'Lula',
        'alegacao_resumo': 'Eu tinha acabado com a fome nesse país em 2012',
        'kws': ['mapa da fome', 'fome', '2012', 'fao']
    },
    {
        'id': 'CONF-14',
        'tema': 'Desenvolvimento Social / Fome',
        'candidato': 'Lula',
        'alegacao_resumo': 'Voltou à presidência em 2023 com 33 milhões de pessoas passando fome no Brasil',
        'kws': ['33 milhões', 'passando fome', 'insegurança alimentar']
    },
    {
        'id': 'CONF-15',
        'tema': 'Transparência e Gastos',
        'candidato': 'Lula',
        'alegacao_resumo': 'Bolsonaro gastou no cartão corporativo quase 30% a mais do que nós',
        'kws': ['cartão corporativo', 'cartao corporativo', '30%']
    },
    {
        'id': 'CONF-16',
        'tema': 'Transportes / Concessões',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Bolsonaro criou a regra de pedágio zero para motos nas concessões de rodovias',
        'kws': ['pedágio', 'pedagio', 'moto', 'motocicleta', 'pedágio zero']
    },
    {
        'id': 'CONF-17',
        'tema': 'Agronegócio / Balança Comercial',
        'candidato': 'Lula',
        'alegacao_resumo': 'Nunca se exportou tanto no país e abrimos 700 novos mercados para o agro',
        'kws': ['nunca se exportou', 'exportou tanto', 'novos mercados', '700 novos']
    },
    {
        'id': 'CONF-18',
        'tema': 'Economia / Endividamento',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Os brasileiros estão devendo mais no atual governo / endividamento recorde',
        'kws': ['devendo mais', 'endividamento', 'famílias']
    },
    {
        'id': 'CONF-19',
        'tema': 'Segurança Pública / Feminicídio',
        'candidato': 'Flávio Bolsonaro',
        'alegacao_resumo': 'Recorde de mulheres assassinadas e de feminicídio no governo Lula',
        'kws': ['feminicídio', 'feminicidio', 'mulheres assassinadas']
    },
    {
        'id': 'CONF-20',
        'tema': 'Infraestrutura / Rodovias',
        'candidato': 'Lula',
        'alegacao_resumo': 'Estamos fazendo a Serra das Araras, uma obra de quase R$ 12 bilhões',
        'kws': ['serra das araras', '12 bilhões', '12 bi']
    }
]

# Function to search matches in independentes
def match_indep(kws, cand):
    res = {}
    for r in indep_records:
        proj = r['projeto_origem']
        c_cand = r['candidato_original']
        # normalize candidate match
        if cand.lower().split()[0] not in c_cand.lower():
            continue
        full_txt = (r['alegacao_citada'] + ' ' + r['afirmacao_resumida'] + ' ' + r['justificativa_verificacao']).lower()
        if any(kw.lower() in full_txt for kw in kws):
            if proj not in res:
                res[proj] = r
    return res

# Function to search matches in portais
def match_portals(kws, cand):
    res = {}
    for p in portal_checks:
        v = p['veiculo']
        p_cand = p['candidato']
        if cand.lower().split()[0] not in p_cand.lower() and p_cand != 'Desconhecido':
            continue
        full_txt = (p['declaracao'] + ' ' + p['tema'] + ' ' + p['justificativa']).lower()
        if any(kw.lower() in full_txt for kw in kws):
            if v not in res:
                res[v] = p
    return res

print("Testando pareamento dos 20 clusters:")
cluster_matches = []
for c in claim_clusters:
    ind = match_indep(c['kws'], c['candidato'])
    por = match_portals(c['kws'], c['candidato'])
    cluster_matches.append({
        'cluster': c,
        'indep': ind,
        'portais': por
    })
    print(f"[{c['id']}] {c['alegacao_resumo'][:45]:45} | Indep: {list(ind.keys())} | Portais: {list(por.keys())}")
