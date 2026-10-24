import os, sys, json, csv
sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'

with open(os.path.join(out_dir, '02_CHECAGENS_INDIVIDUAIS.json'), 'r', encoding='utf-8') as f:
    checks = json.load(f)

# Define clusters of comparable claims across the 4 outlets
claim_groups = [
    {
        'group_id': 'GRP-01',
        'title': 'Obras paralisadas no Brasil e dados do TCU (11.500 obras)',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Infraestrutura e Obras Públicas',
        'proposition': 'Flávio afirma que relatório recente do TCU aponta mais de 11.500 obras paralisadas no atual governo federal.',
        'keywords': ['11.500', '11.469', '11500', 'obras paralisadas']
    },
    {
        'group_id': 'GRP-02',
        'title': 'Lula herdou 6 mil obras paradas ao assumir em 2023',
        'candidate': 'Lula',
        'topic': 'Infraestrutura e Obras Públicas',
        'proposition': 'Lula afirma que herdou 6.000 obras paradas deixadas pelo governo anterior.',
        'keywords': ['6.000', '6 mil', 'herdou 6', 'obras paradas']
    },
    {
        'group_id': 'GRP-03',
        'title': 'Piso permanente de R$ 600 do Bolsa Família foi criado por Bolsonaro',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Programas Sociais',
        'proposition': 'Flávio afirma que foi Jair Bolsonaro quem instituiu o valor permanente de no mínimo R$ 600 do Bolsa Família.',
        'keywords': ['600', 'bolsa família', 'auxílio brasil']
    },
    {
        'group_id': 'GRP-04',
        'title': 'Média de R$ 190 do Bolsa Família nos governos do PT',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Programas Sociais',
        'proposition': 'Flávio compara o valor atual de R$ 600 dizendo que a média no governo do PT era de R$ 190.',
        'keywords': ['190', 'média']
    },
    {
        'group_id': 'GRP-05',
        'title': 'Pavimentação da BR-319 (Porto Velho - Manaus) em andamento',
        'candidate': 'Lula',
        'topic': 'Infraestrutura e Meio Ambiente',
        'proposition': 'Lula afirma que o governo federal está fazendo a pavimentação da rodovia BR-319.',
        'keywords': ['br-319', 'br 319', 'porto velho']
    },
    {
        'group_id': 'GRP-06',
        'title': 'Financiamento exclusivo do túnel Santos-Guarujá',
        'candidate': 'Lula',
        'topic': 'Infraestrutura Portuária',
        'proposition': 'Lula afirma que o governo federal é quem está colocando o dinheiro para construir o túnel Santos-Guarujá.',
        'keywords': ['túnel', 'tunel', 'santos-guarujá', 'santos']
    },
    {
        'group_id': 'GRP-07',
        'title': 'Aprovação do fim da jornada de trabalho 6x1',
        'candidate': 'Lula',
        'topic': 'Trabalho e Legislação',
        'proposition': 'Lula afirma que o governo/Congresso aprovou o fim da escala de trabalho 6x1.',
        'keywords': ['6x1', 'escala']
    },
    {
        'group_id': 'GRP-08',
        'title': 'Reforma Tributária e alíquota de 28% do IVA em 2026',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Economia e Tributação',
        'proposition': 'Flávio afirma que a nova alíquota do IVA cobrada no ano seguinte será de 28%, a maior do mundo.',
        'keywords': ['iva', '28%', 'alíquota', 'reforma tributária']
    },
    {
        'group_id': 'GRP-09',
        'title': 'Jogador Richarlison comprou uma ilha do MST',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Agronegócio / Política',
        'proposition': 'Flávio afirma que o jogador de futebol Richarlison comprou uma ilha de integrantes do MST.',
        'keywords': ['richarlison', 'ilha', 'mst']
    },
    {
        'group_id': 'GRP-10',
        'title': 'Flávio nunca foi investigado por envolvimento com milícia',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Segurança e Justiça',
        'proposition': 'Flávio afirma categoricamente que nunca foi investigado por envolvimento com milícia.',
        'keywords': ['milícia', 'milicia', 'escritório do crime']
    },
    {
        'group_id': 'GRP-11',
        'title': 'Recorde histórico de feminicídios no Brasil',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Segurança Pública',
        'proposition': 'Flávio afirma que o Brasil registrou recorde de feminicídios e de mulheres assassinadas no governo Lula.',
        'keywords': ['feminicídio', 'feminicidio', 'mulheres assassinadas']
    },
    {
        'group_id': 'GRP-12',
        'title': 'Salário mínimo seria de R$ 900 sem os aumentos reais do PT',
        'candidate': 'Lula',
        'topic': 'Economia e Trabalho',
        'proposition': 'Lula afirma que sem a política de valorização acima da inflação o salário mínimo seria de apenas R$ 900.',
        'keywords': ['900', 'salário mínimo']
    },
    {
        'group_id': 'GRP-13',
        'title': 'Brasil saiu do Mapa da Fome em 2012',
        'candidate': 'Lula',
        'topic': 'Desenvolvimento Social',
        'proposition': 'Lula afirma que tirou o Brasil do Mapa da Fome da ONU no ano de 2012.',
        'keywords': ['fome', 'mapa da fome', '2012']
    },
    {
        'group_id': 'GRP-14',
        'title': 'Gastos no cartão corporativo da Presidência sob Bolsonaro',
        'candidate': 'Lula',
        'topic': 'Transparência e Gastos',
        'proposition': 'Lula afirma que Bolsonaro gastou no cartão corporativo quase 30% a mais que suas gestões.',
        'keywords': ['cartão corporativo', 'cartao', '30%']
    },
    {
        'group_id': 'GRP-15',
        'title': 'Bolsonaro criou pedágio zero para motos em rodovias',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Infraestrutura e Transportes',
        'proposition': 'Flávio afirma que Bolsonaro criou a regra de isenção de pedágio para motocicletas nas novas concessões.',
        'keywords': ['pedágio', 'pedagio', 'moto', 'motocicleta']
    },
    {
        'group_id': 'GRP-16',
        'title': 'Brasil bateu recorde de exportações agrícolas e abertura de mercados',
        'candidate': 'Lula',
        'topic': 'Agronegócio e Comércio Exterior',
        'proposition': 'Lula afirma que o país nunca exportou tanto e abriu centenas de novos mercados agropecuários.',
        'keywords': ['exportou tanto', 'exportações', 'novos mercados']
    },
    {
        'group_id': 'GRP-17',
        'title': 'Endividamento das famílias brasileiras aumentou',
        'candidate': 'Flávio Bolsonaro',
        'topic': 'Economia e Finanças Pessoais',
        'proposition': 'Flávio afirma que os brasileiros estão mais endividados no atual governo.',
        'keywords': ['endividamento', 'devendo mais']
    },
    {
        'group_id': 'GRP-18',
        'title': 'Serra das Araras é obra de R$ 12 bilhões executada pelo governo',
        'candidate': 'Lula',
        'topic': 'Infraestrutura Rodoviária',
        'proposition': 'Lula afirma que o governo federal está executando a obra da Serra das Araras avaliada em quase R$ 12 bilhões.',
        'keywords': ['serra das araras', '12 bilhões', '12 bi']
    }
]

# Match each check from 02_CHECAGENS_INDIVIDUAIS to groups
matrix_rows = []

for grp in claim_groups:
    row = {
        'claim_group_id': grp['group_id'],
        'candidate': grp['candidate'],
        'topic': grp['topic'],
        'claim_title': grp['title'],
        'normalized_proposition': grp['proposition'],
        'uol_verdict': 'Não localizada no material acessível',
        'uol_reasoning': '',
        'g1_verdict': 'Não localizada no material acessível',
        'g1_reasoning': '',
        'estadao_verdict': 'Não localizada no material acessível',
        'estadao_reasoning': '',
        'lupa_verdict': 'Não localizada no material acessível',
        'lupa_reasoning': '',
        'outlets_count': 0
    }
    
    # search checks
    for c in checks:
        text = (c['declaracao'] + ' ' + c['tema'] + ' ' + c['justificativa']).lower()
        if any(kw in text for kw in grp['keywords']):
            # check vehicle
            v = c['veiculo']
            if 'G1' in v and row['g1_verdict'] == 'Não localizada no material acessível':
                row['g1_verdict'] = c['veredito_original']
                row['g1_reasoning'] = c['justificativa'][:400]
                row['outlets_count'] += 1
            elif 'UOL' in v and row['uol_verdict'] == 'Não localizada no material acessível':
                row['uol_verdict'] = c['veredito_original']
                row['uol_reasoning'] = c['justificativa'][:400]
                row['outlets_count'] += 1
            elif 'Estadão' in v and row['estadao_verdict'] == 'Não localizada no material acessível':
                row['estadao_verdict'] = c['veredito_original']
                row['estadao_reasoning'] = c['justificativa'][:400]
                row['outlets_count'] += 1
            elif 'Lupa' in v and row['lupa_verdict'] == 'Não localizada no material acessível':
                row['lupa_verdict'] = c['veredito_original']
                row['lupa_reasoning'] = c['justificativa'][:400]
                row['outlets_count'] += 1
                
    # classify equivalence and agreement
    cnt = row['outlets_count']
    if cnt >= 2:
        row['equivalence_status'] = 'Equivalente'
    elif cnt == 1:
        row['equivalence_status'] = 'Exclusiva de um veículo'
    else:
        row['equivalence_status'] = 'Não localizada'
        
    # Analyze agreement
    verdicts = [row['uol_verdict'], row['g1_verdict'], row['estadao_verdict'], row['lupa_verdict']]
    active_v = [v for v in verdicts if v != 'Não localizada no material acessível']
    
    # Categorization logic
    if len(active_v) <= 1:
        row['agreement_type'] = 'Sem comparação'
        row['divergence_type'] = 'N/A (veículo único)'
    else:
        # Check if they share the same sentiment (all negative, all positive, or mixed)
        is_all_neg = all(any(neg in v.upper() for neg in ['FALSO', 'FAKE', 'ENGANOSO', 'NÃO É BEM ASSIM', 'FALTA CONTEXTO', 'SUBESTIMADO']) for v in active_v)
        is_all_pos = all(any(pos in v.upper() for pos in ['VERDADEIRO', 'FATO']) for v in active_v)
        
        if is_all_neg:
            row['agreement_type'] = 'Concordância de mérito com rótulos editoriais distintos'
            row['divergence_type'] = 'Rótulo / Limiar de Tolerância'
        elif is_all_pos:
            row['agreement_type'] = 'Concordância plena de veredito e justificativa'
            row['divergence_type'] = 'Sem divergência relevante'
        else:
            row['agreement_type'] = 'Divergência substantiva'
            row['divergence_type'] = 'Metodológica / Escopo'
            
    matrix_rows.append(row)

# Save 03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.json
with open(os.path.join(out_dir, '03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.json'), 'w', encoding='utf-8') as f:
    json.dump(matrix_rows, f, indent=2, ensure_ascii=False)

# Save 03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.csv
with open(os.path.join(out_dir, '03_MATRIZ_COMPARATIVA_QUATRO_VEICULOS.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow([
        'ID Grupo', 'Candidato', 'Tema', 'Título da Alegação', 'Proposição Normalizada',
        'Veredito UOL', 'Justificativa UOL', 'Veredito G1', 'Justificativa G1',
        'Veredito Estadão', 'Justificativa Estadão', 'Veredito Lupa', 'Justificativa Lupa',
        'Qtd Veículos', 'Status Equivalência', 'Tipo de Concordância', 'Tipo de Divergência'
    ])
    for r in matrix_rows:
        w.writerow([
            r['claim_group_id'], r['candidate'], r['topic'], r['claim_title'], r['normalized_proposition'],
            r['uol_verdict'], r['uol_reasoning'], r['g1_verdict'], r['g1_reasoning'],
            r['estadao_verdict'], r['estadao_reasoning'], r['lupa_verdict'], r['lupa_reasoning'],
            r['outlets_count'], r['equivalence_status'], r['agreement_type'], r['divergence_type']
        ])

print(f'Successfully built comparative matrix with {len(matrix_rows)} claim groups across the 4 outlets.')
