import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

m2_root = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925'
cat_json = os.path.join(m2_root, '06_RELATORIOS_CONSOLIDADOS', 'catalogo_estruturado_checagens_consolidado.json')
with open(cat_json, 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's inspect details for all 15 cases
# We want to map each case to its specific matches across all 4 projects
cases_def = [
    {
        'id': 'CASO-01',
        'title': 'Obras paralisadas no Brasil: relatório do TCU aponta 11.500 obras',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Economia e Obras Públicas'
    },
    {
        'id': 'CASO-02',
        'title': 'Lula herdou 6 mil obras paralisadas ao assumir em 2023',
        'speaker': 'Lula',
        'theme': 'Economia e Obras Públicas'
    },
    {
        'id': 'CASO-03',
        'title': 'Governo Bolsonaro pegou 14 mil obras paradas e entregou pouco mais de 8 mil',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Economia e Obras Públicas'
    },
    {
        'id': 'CASO-04',
        'title': 'Sem reajustes acima da inflação do PT, salário mínimo seria apenas R$ 900',
        'speaker': 'Lula',
        'theme': 'Economia e Salário Mínimo'
    },
    {
        'id': 'CASO-05',
        'title': 'Foi Bolsonaro que deu o piso de no mínimo R$ 600 do Bolsa Família',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Programas Sociais'
    },
    {
        'id': 'CASO-06',
        'title': 'Média do Bolsa Família nos governos do PT era de R$ 190',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Programas Sociais'
    },
    {
        'id': 'CASO-07',
        'title': 'Estamos fazendo a pavimentação da BR-319 (Porto Velho - Manaus)',
        'speaker': 'Lula',
        'theme': 'Infraestrutura e Meio Ambiente'
    },
    {
        'id': 'CASO-08',
        'title': 'No túnel Santos-Guarujá quem está colocando dinheiro para fazer somos nós',
        'speaker': 'Lula',
        'theme': 'Infraestrutura'
    },
    {
        'id': 'CASO-09',
        'title': 'Nós aprovamos o fim da escala 6x1',
        'speaker': 'Lula',
        'theme': 'Trabalho e Legislação'
    },
    {
        'id': 'CASO-10',
        'title': 'Reforma Tributária: IVA começará com alíquota estimada em 28%, a maior do mundo',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Economia e Tributos'
    },
    {
        'id': 'CASO-11',
        'title': 'Jogador Richarlison teria comprado uma ilha do MST',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Agronegócio / Política'
    },
    {
        'id': 'CASO-12',
        'title': 'Flávio Bolsonaro afirma que nunca foi investigado por envolvimento com milícia',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Segurança e Investigações'
    },
    {
        'id': 'CASO-13',
        'title': 'Endividamento das famílias brasileiras aumentou e brasileiros estão devendo mais',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Economia e Crédito'
    },
    {
        'id': 'CASO-14',
        'title': 'Casos de feminicídio bateram recorde histórico no Brasil',
        'speaker': 'Flávio Bolsonaro',
        'theme': 'Segurança Pública'
    },
    {
        'id': 'CASO-15',
        'title': 'Gastos com cartão corporativo e sigilo de 100 anos no governo Bolsonaro',
        'speaker': 'Lula',
        'theme': 'Transparência e Corrupção'
    }
]

print('Cases defined:', len(cases_def))
