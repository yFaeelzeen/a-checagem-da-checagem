import os, sys, json, csv
sys.stdout.reconfigure(encoding='utf-8')

m2_cat_path = r'C:\Users\RAFAE\Downloads\dossie_checadores_coleta_20261024_091925\06_RELATORIOS_CONSOLIDADOS\catalogo_estruturado_checagens_consolidado.json'
m4_ind_path = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\02_CHECAGENS_INDIVIDUAIS.json'
out_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'

with open(m2_cat_path, 'r', encoding='utf-8') as f:
    indep_records = json.load(f)

with open(m4_ind_path, 'r', encoding='utf-8') as f:
    portal_checks = json.load(f)

cases_definition = [
    {
        'id': 'CONF-01',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'TCU acaba de soltar relatório apontando mais de 11.500 obras paralisadas no atual governo federal',
        'kws': ['11.500', '11.469', '11500', '11,5 mil', '11.500 obras'],
        'objeto_factual': 'Existência de relatório do TCU com ~11.500 obras paralisadas e sua atribuição ao atual governo'
    },
    {
        'id': 'CONF-02',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Lula',
        'fala_resumo': 'Lula herdou 6.000 obras paralisadas deixadas pelo governo Bolsonaro',
        'kws': ['6.000', '6 mil', 'herdou 6', '6000 obras'],
        'objeto_factual': 'Número de obras paralisadas registradas pelo TCU no início do mandato em 2023'
    },
    {
        'id': 'CONF-03',
        'tema': 'Obras Públicas / TCU',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Bolsonaro pegou o Brasil com 14 mil obras paradas e entregou com pouco mais de 8 mil',
        'kws': ['14 mil', '8 mil', '8.603'],
        'objeto_factual': 'Variação do estoque de obras paralisadas entre 2019 e 2022 segundo dados do TCU'
    },
    {
        'id': 'CONF-04',
        'tema': 'Programas Sociais',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Foi Bolsonaro que deu o piso de no mínimo R$ 600 do Bolsa Família',
        'kws': ['600', 'bolsa família', 'auxílio brasil'],
        'objeto_factual': 'Autoria da fixação do piso de R$ 600 e sua validade temporal (EC 123/2022 vs EC 126/2022)'
    },
    {
        'id': 'CONF-05',
        'tema': 'Programas Sociais',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'A média do Bolsa Família nos governos do PT era de R$ 190',
        'kws': ['190', 'bolsa família', 'média'],
        'objeto_factual': 'Valor nominal histórico do Bolsa Família em 2018 versus valor real corrigido pelo IPCA'
    },
    {
        'id': 'CONF-06',
        'tema': 'Infraestrutura e Meio Ambiente',
        'candidato': 'Lula',
        'fala_resumo': 'Estamos fazendo a BR-319, que liga Porto Velho a Manaus',
        'kws': ['br-319', 'br 319', 'porto velho', 'manaus'],
        'objeto_factual': 'Existência de obras de pavimentação no trecho central da BR-319 e licenciamento do Ibama'
    },
    {
        'id': 'CONF-07',
        'tema': 'Infraestrutura Portuária',
        'candidato': 'Lula',
        'fala_resumo': 'No túnel Santos-Guarujá quem está colocando dinheiro para fazer somos nós',
        'kws': ['túnel', 'tunel', 'santos-guarujá', 'santos guaruja'],
        'objeto_factual': 'Estrutura de financiamento do túnel (parceria de 50% Governo Federal e 50% Governo de SP)'
    },
    {
        'id': 'CONF-08',
        'tema': 'Trabalho e Legislação',
        'candidato': 'Lula',
        'fala_resumo': 'Nós aprovamos o fim da escala 6x1',
        'kws': ['6x1', 'escala'],
        'objeto_factual': 'Status legislativo da PEC da jornada 6x1 no Congresso Nacional'
    },
    {
        'id': 'CONF-09',
        'tema': 'Economia e Tributos',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'IVA começa a ser cobrado no ano que vem com alíquota estimada de 28%, a maior do mundo',
        'kws': ['iva', '28%', 'alíquota', 'carga tributária', 'reforma tributária'],
        'objeto_factual': 'Alíquota de teste em 2026 (1%) versus estimativa de teto projetada para 2033'
    },
    {
        'id': 'CONF-10',
        'tema': 'Agronegócio / Política',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Jogador Richarlison comprou uma ilha de integrantes do MST',
        'kws': ['richarlison', 'ilha', 'mst'],
        'objeto_factual': 'Origem e partes envolvidas na disputa de posse da ilha em Angra dos Reis'
    },
    {
        'id': 'CONF-11',
        'tema': 'Segurança e Investigações',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Flávio afirma que nunca foi investigado por causa de envolvimento com milícia',
        'kws': ['milícia', 'milicia', 'escritório do crime'],
        'objeto_factual': 'Tipificação formal dos inquéritos no STF/MPRJ versus apuração de vínculos no gabinete da Alerj'
    },
    {
        'id': 'CONF-12',
        'tema': 'Economia e Salário Mínimo',
        'candidato': 'Lula',
        'fala_resumo': 'Sem os reajustes acima da inflação do PT, salário mínimo seria apenas R$ 900',
        'kws': ['900', 'salário mínimo', 'salario minimo', 'inpc'],
        'objeto_factual': 'Correção estrita do salário mínimo pelo INPC desde 2002 (resultando em ~R$ 804)'
    },
    {
        'id': 'CONF-13',
        'tema': 'Desenvolvimento Social / Fome',
        'candidato': 'Lula',
        'fala_resumo': 'Eu tinha acabado com a fome nesse país em 2012',
        'kws': ['mapa da fome', 'fome', '2012', 'fao'],
        'objeto_factual': 'Data do relatório da FAO que retirou o Brasil do Mapa da Fome (2014) e conceito técnico'
    },
    {
        'id': 'CONF-14',
        'tema': 'Desenvolvimento Social / Fome',
        'candidato': 'Lula',
        'fala_resumo': 'Voltou à presidência em 2023 com 33 milhões de pessoas passando fome no Brasil',
        'kws': ['33 milhões', 'passando fome', 'insegurança alimentar'],
        'objeto_factual': 'Inquérito da Rede PENSSAN sobre insegurança alimentar grave em 2022'
    },
    {
        'id': 'CONF-15',
        'tema': 'Transparência e Gastos',
        'candidato': 'Lula',
        'fala_resumo': 'Bolsonaro gastou no cartão corporativo quase 30% a mais do que nós',
        'kws': ['cartão corporativo', 'cartao corporativo', '30%'],
        'objeto_factual': 'Comparações de gastos da Presidência corrigidos pela inflação desclassificados pela CGU'
    },
    {
        'id': 'CONF-16',
        'tema': 'Transportes / Concessões',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Bolsonaro criou a regra de pedágio zero para motos nas concessões de rodovias',
        'kws': ['pedágio', 'pedagio', 'moto', 'motocicleta', 'pedágio zero'],
        'objeto_factual': 'Portaria 104/2021 do Ministério da Infraestrutura para novos editais de concessão'
    },
    {
        'id': 'CONF-17',
        'tema': 'Agronegócio / Comércio Exterior',
        'candidato': 'Lula',
        'fala_resumo': 'Nunca se exportou tanto no país e abrimos 700 novos mercados para o agro',
        'kws': ['nunca se exportou', 'exportou tanto', 'novos mercados', '700 novos'],
        'objeto_factual': 'Recorde da balança comercial e aberturas de mercados pelo Ministério da Agricultura'
    },
    {
        'id': 'CONF-18',
        'tema': 'Economia / Endividamento',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Os brasileiros estão devendo mais no atual governo / endividamento recorde',
        'kws': ['devendo mais', 'endividamento', 'famílias'],
        'objeto_factual': 'Série SGS 29037 do Banco Central sobre endividamento das famílias com o SFN'
    },
    {
        'id': 'CONF-19',
        'tema': 'Segurança Pública / Feminicídio',
        'candidato': 'Flávio Bolsonaro',
        'fala_resumo': 'Recorde de mulheres assassinadas e de feminicídio no governo Lula',
        'kws': ['feminicídio', 'feminicidio', 'mulheres assassinadas'],
        'objeto_factual': 'Registros de feminicídio no Anuário Brasileiro de Segurança Pública (FBSP)'
    },
    {
        'id': 'CONF-20',
        'tema': 'Infraestrutura / Rodovias',
        'candidato': 'Lula',
        'fala_resumo': 'Estamos fazendo a Serra das Araras, uma obra de quase R$ 12 bilhões',
        'kws': ['serra das araras', '12 bilhões', '12 bi'],
        'objeto_factual': 'Valor do investimento e modelo de concessão privada na Via Dutra'
    }
]

comparison_matrix = []

for c in cases_definition:
    kws = c['kws']
    cand = c['candidato']
    
    # Independentes
    vof_item = None
    pin_item = None
    vav_item = None
    
    for r in indep_records:
        if cand.lower().split()[0] not in r['candidato_original'].lower():
            continue
        txt = (r['alegacao_citada'] + ' ' + r['afirmacao_resumida'] + ' ' + r['justificativa_verificacao']).lower()
        if any(k in txt for k in kws):
            p = r['projeto_origem']
            if p == 'Verifique os Fatos' and not vof_item: vof_item = r
            elif p == 'Pinóquio.live' and not pin_item: pin_item = r
            elif p == 'Verifique a Verdade' and not vav_item: vav_item = r
            
    # Portais
    uol_item = None
    g1_item = None
    est_item = None
    lup_item = None
    
    for p in portal_checks:
        if cand.lower().split()[0] not in p['candidato'].lower() and p['candidato'] != 'Desconhecido':
            continue
        txt = (p['declaracao'] + ' ' + p['tema'] + ' ' + p['justificativa']).lower()
        if any(k in txt for k in kws):
            v = p['veiculo']
            if 'UOL' in v and not uol_item: uol_item = p
            elif 'G1' in v and not g1_item: g1_item = p
            elif 'Estadão' in v and not est_item: est_item = p
            elif 'Lupa' in v and not lup_item: lup_item = p

    # Build row
    row = {
        'id_confronto': c['id'],
        'tema': c['tema'],
        'candidato': c['candidato'],
        'alegacao_resumo': c['fala_resumo'],
        'objeto_factual': c['objeto_factual'],
        # Independentes
        'vof_veredito': vof_item['veredito_original'] if vof_item else 'Não checado',
        'vof_justificativa': vof_item['justificativa_verificacao'][:300] if vof_item else '-',
        'pin_veredito': pin_item['veredito_original'] if pin_item else 'Não checado',
        'pin_justificativa': pin_item['justificativa_verificacao'][:300] if pin_item else '-',
        'vav_veredito': vav_item['veredito_original'] if vav_item else 'Não checado',
        'vav_justificativa': vav_item['justificativa_verificacao'][:300] if vav_item else '-',
        # Portais
        'uol_veredito': uol_item['veredito_original'] if uol_item else 'Não checado',
        'uol_justificativa': uol_item['justificativa'][:300] if uol_item else '-',
        'g1_veredito': g1_item['veredito_original'] if g1_item else 'Não checado',
        'g1_justificativa': g1_item['justificativa'][:300] if g1_item else '-',
        'est_veredito': est_item['veredito_original'] if est_item else 'Não checado',
        'est_justificativa': est_item['justificativa'][:300] if est_item else '-',
        'lup_veredito': lup_item['veredito_original'] if lup_item else 'Não checado',
        'lup_justificativa': lup_item['justificativa'][:300] if lup_item else '-',
        # Confronto
        'confronto_conclusao': '',
        'tipo_divergencia_bloco': '',
        'alinhamento_indep_vs_portais': ''
    }
    
    # Specific confrontation evaluations based on established findings
    if c['id'] == 'CONF-01':
        row['confronto_conclusao'] = 'Divisão simétrica idêntica nos dois blocos: tanto entre independentes (VaV verdadeiro vs Pinóquio enganoso/VoF parcial) quanto entre portais (G1/Estadão verdadeiro vs UOL falso/Lupa falta contexto), a divergência é de enquadramento (validade do relatório do TCU vs atribuição causal ao governo federal).'
        row['tipo_divergencia_bloco'] = 'Metodológica / Enquadramento'
        row['alinhamento_indep_vs_portais'] = 'Paralelismo Metodológico Perfeito'
    elif c['id'] == 'CONF-02':
        row['confronto_conclusao'] = 'Independentes e portais concordam nos dados do TCU (8.603 obras paradas). Contudo, G1 e UOL punem com FALSO/FAKE pela discrepância numérica de 30%, enquanto Lupa usa SUBESTIMADO e Verifique a Verdade considera VERDADEIRO por ser erro que prejudica o próprio candidato.'
        row['tipo_divergencia_bloco'] = 'Tolerância a Erro Contra Si Mesmo'
        row['alinhamento_indep_vs_portais'] = 'Concordância Factual com Divergência de Taxonomia'
    elif c['id'] == 'CONF-04':
        row['confronto_conclusao'] = 'Ambos os blocos concordam sobre a vigência da EC 123/2022 (até 31/12/2022) e o PLOA de R$ 405. VoF, Pinóquio, UOL, G1 e Lupa convergem na rejeição da perenidade sob Bolsonaro. Apenas o Estadão concedeu Verdadeiro no selo por foco na data de início do desembolso.'
        row['tipo_divergencia_bloco'] = 'Temporal / Autoria'
        row['alinhamento_indep_vs_portais'] = 'Alta Convergência Crítica'
    elif c['id'] == 'CONF-05':
        row['confronto_conclusao'] = 'Rejeição quase unânime da comparação de valor nominal sem correção pelo IPCA. Pinóquio, VaV, UOL, G1 e Estadão apontam distorção econômica grave. A Lupa validou estritamente o valor nominal da série histórica com ressalva.'
        row['tipo_divergencia_bloco'] = 'Distorção Estatística Nominal vs Real'
        row['alinhamento_indep_vs_portais'] = 'Convergência Metodológica Ampla'
    elif c['id'] == 'CONF-06':
        row['confronto_conclusao'] = 'Tanto os independentes (VaV, Pinóquio) quanto os portais (G1, Lupa) concordam que o trecho do meio da rodovia BR-319 está embargado pelo Ibama sem licença de pavimentação. A frase de Lula é rechaçada como Falso/Enganoso/Não é bem assim.'
        row['tipo_divergencia_bloco'] = 'Factual / Execução de Obra'
        row['alinhamento_indep_vs_portais'] = 'Convergência Plena'
    elif c['id'] == 'CONF-07':
        row['confronto_conclusao'] = 'Independentes e portais apontam que o túnel é uma PPP paritária (50% do Governo de SP e 50% do Governo Federal). Lula erra ao afirmar exclusividade de aporte federal.'
        row['tipo_divergencia_bloco'] = 'Factual / Atribuição Orçamentária'
        row['alinhamento_indep_vs_portais'] = 'Convergência Plena'
    elif c['id'] == 'CONF-08':
        row['confronto_conclusao'] = 'Checado exaustivamente pelos independentes (VaV e Pinóquio classificam como Falso absoluto, pois a PEC ainda tramita). Os portais tradicionais não deram destaque a essa frase nas matérias autorizadas.'
        row['tipo_divergencia_bloco'] = 'Exclusividade de Cobertura dos Independentes'
        row['alinhamento_indep_vs_portais'] = 'Independentes Mais Ágeis em Tramitação Legislativa'
    elif c['id'] == 'CONF-09':
        row['confronto_conclusao'] = 'Concordância unânime entre todos os checadores de que a alíquota em 2026 será de apenas 1% de teste (0,9% CBS + 0,1% IBS) e que a alíquota de 28% é teto projetado para a década seguinte. Flávio fundiu prazos.'
        row['tipo_divergencia_bloco'] = 'Cronologia Tributária'
        row['alinhamento_indep_vs_portais'] = 'Convergência Total'
    elif c['id'] == 'CONF-10':
        row['confronto_conclusao'] = 'Classificado unanimemente como Falso/Fake em ambos os blocos. O litígio de posse em Angra dos Reis não tem qualquer relação com o MST.'
        row['tipo_divergencia_bloco'] = 'Falsidade Factual Absoluta'
        row['alinhamento_indep_vs_portais'] = 'Consenso Absoluto'
    elif c['id'] == 'CONF-11':
        row['confronto_conclusao'] = 'Caso mais emblemático de divergência interna nos dois blocos: VaV (indep), UOL, Estadão e Lupa (portais) classificam como Verdadeiro adotando critério de tipificação penal estrita (sem denúncia pelo art. 288-A de milícia); Pinóquio (indep) e G1 (portal) aplicam Insustentável / Não é bem assim com base nos laços substantivos investigados no gabinete.'
        row['tipo_divergencia_bloco'] = 'Formalismo Jurídico vs Investigação Substantiva'
        row['alinhamento_indep_vs_portais'] = 'Fratura Idêntica e Espelhada em Ambos os Blocos'
    elif c['id'] == 'CONF-12':
        row['confronto_conclusao'] = 'VaV (indep) valida o conceito central de ganho real do salário mínimo (o INPC puro daria ~R$ 804); Pinóquio e G1 punem a diferença numérica de R$ 96 como Enganoso / Não é bem assim.'
        row['tipo_divergencia_bloco'] = 'Metodológica / Rigor Numérico'
        row['alinhamento_indep_vs_portais'] = 'Convergência de Argumentação'
    elif c['id'] == 'CONF-13':
        row['confronto_conclusao'] = 'Lula errou o ano (o relatório da FAO é de 2014, não 2012). G1, Estadão, Lupa e Pinóquio registram a imprecisão cronológica mantendo a veracidade do marco da FAO.'
        row['tipo_divergencia_bloco'] = 'Cronologia de Relatório Internacional'
        row['alinhamento_indep_vs_portais'] = 'Convergência Plena'
    elif c['id'] == 'CONF-14':
        row['confronto_conclusao'] = 'Corroborado por Pinóquio, VaV, G1 e Lupa com base no Inquérito da Rede PENSSAN de 2022 sobre insegurança alimentar grave.'
        row['tipo_divergencia_bloco'] = 'Validação de Pesquisa Técnica'
        row['alinhamento_indep_vs_portais'] = 'Convergência Total'
    elif c['id'] == 'CONF-15':
        row['confronto_conclusao'] = 'Planilhas da Presidência e CGU corrigidas pelo IPCA desmentem a diferença de 30% alegada por Lula. VaV, Pinóquio e G1 desautorizam a frase.'
        row['tipo_divergencia_bloco'] = 'Factual / Planilhas Oficiais'
        row['alinhamento_indep_vs_portais'] = 'Convergência Plena'
    elif c['id'] == 'CONF-16':
        row['confronto_conclusao'] = 'A regra de isenção para motos foi introduzida pela Portaria 104/2021 nos novos editais federais, sem afetar contratos anteriores. VaV, UOL e Estadão validam com a ressalva de escopo.'
        row['tipo_divergencia_bloco'] = 'Escopo Administrativo'
        row['alinhamento_indep_vs_portais'] = 'Convergência Total'
    elif c['id'] == 'CONF-17':
        row['confronto_conclusao'] = 'Concordância unânime entre todos os checadores de ambos os blocos (VaV, Pinóquio, G1, Estadão e Lupa) sobre o recorde histórico de exportações agrícolas e aberturas sanitárias.'
        row['tipo_divergencia_bloco'] = 'Factual / Dados Oficiais'
        row['alinhamento_indep_vs_portais'] = 'Consenso Pleno'
    elif c['id'] == 'CONF-18':
        row['confronto_conclusao'] = 'Confirmado por VaV, Pinóquio, UOL e G1 com base na Série SGS 29037 do Banco Central (endividamento passou de 49,1% para 49,9% da renda anual).'
        row['tipo_divergencia_bloco'] = 'Factual / Série Banco Central'
        row['alinhamento_indep_vs_portais'] = 'Consenso Pleno'
    elif c['id'] == 'CONF-19':
        row['confronto_conclusao'] = 'Checado exaustivamente pelos independentes (VaV e Pinóquio confirmam o recorde do Anuário de Segurança Pública com ressalva sobre a evolução da tipificação policial). Portais não incluíram o tema nas matérias autorizadas.'
        row['tipo_divergencia_bloco'] = 'Cobertura Temática'
        row['alinhamento_indep_vs_portais'] = 'Independentes Cobriram o Tema com Rigor Técnico'
    elif c['id'] == 'CONF-20':
        row['confronto_conclusao'] = 'Checado por Pinóquio e VaV: obra executada pela concessionária Motiva com aporte de R$ 1,5 bilhão, e não R$ 12 bilhões governamentais diretos. Lula exagerou as cifras.'
        row['tipo_divergencia_bloco'] = 'Factual / Orçamento de Concessão'
        row['alinhamento_indep_vs_portais'] = 'Cobertura Especializada Independente'
    else:
        row['confronto_conclusao'] = 'Confronto factual entre dados primários e declaração.'
        row['tipo_divergencia_bloco'] = 'Metodológica'
        row['alinhamento_indep_vs_portais'] = 'Convergência Geral'

    comparison_matrix.append(row)

# Save JSON
out_json_path = os.path.join(out_dir, 'matriz_confronto_independentes_vs_portais.json')
with open(out_json_path, 'w', encoding='utf-8') as f:
    json.dump(comparison_matrix, f, indent=2, ensure_ascii=False)

# Save CSV
out_csv_path = os.path.join(out_dir, 'matriz_confronto_independentes_vs_portais.csv')
with open(out_csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'ID Confronto', 'Tema', 'Candidato', 'Alegação Resumida', 'Objeto Factual',
        'VoF Veredito', 'VoF Justificativa', 'Pinóquio Veredito', 'Pinóquio Justificativa',
        'VaV Veredito', 'VaV Justificativa', 'UOL Veredito', 'UOL Justificativa',
        'G1 Veredito', 'G1 Justificativa', 'Estadão Veredito', 'Estadão Justificativa',
        'Lupa Veredito', 'Lupa Justificativa', 'Conclusão do Confronto',
        'Tipo de Divergência', 'Alinhamento Independentes vs Portais'
    ])
    for r in comparison_matrix:
        writer.writerow([
            r['id_confronto'], r['tema'], r['candidato'], r['alegacao_resumo'], r['objeto_factual'],
            r['vof_veredito'], r['vof_justificativa'], r['pin_veredito'], r['pin_justificativa'],
            r['vav_veredito'], r['vav_justificativa'], r['uol_veredito'], r['uol_justificativa'],
            r['g1_veredito'], r['g1_justificativa'], r['est_veredito'], r['est_justificativa'],
            r['lup_veredito'], r['lup_justificativa'], r['confronto_conclusao'],
            r['tipo_divergencia_bloco'], r['alinhamento_indep_vs_portais']
        ])

print(f"Matriz de confronto salva com sucesso em JSON e CSV com {len(comparison_matrix)} casos.")
