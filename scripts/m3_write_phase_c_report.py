import os, sys
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
md_path = os.path.join(target_dir, '02_RELATORIO_DE_DIVERGENCIAS.md')

content = '''# Relatório Comparativo de Divergências e Avaliação Independente (Fase C)

- **Data da Auditoria:** 24 de outubro de 2026
- **Amostra Analisada:** 15 alegações centrais de alta relevância política, econômica e institucional do debate da TV Globo (23/10/2026).
- **Metodologia:** Confronto cruzado das fichas de checagem, inspeção direta das fontes primárias acessíveis e classificação formal dos tipos de divergência.

---

## 1. Tipologia de Divergências Observadas

A análise independente demonstrou que as discrepâncias entre os checadores dividem-se em categorias analíticas precisas:

1. **Divergência Metodológica (Foco no Número vs Foco na Atribuição Causal):**
   - *Exemplo típico (CASO-01 - 11.500 obras paralisadas):* O número citado por Flávio Bolsonaro (11.500) é rigorosamente verdadeiro segundo o TCU (11.469 contratos paralisados). O *Verifique a Verdade* concedeu o selo **Verdadeiro** por validar a cifra oficial. Já o *Pinóquio.live* rotulou como **Enganoso** e o *Verifique os Fatos* como **Parcial** porque o orador disse "no atual governo", quando as obras pertencem a convênios municipais acumulados ao longo de décadas.
   
2. **Divergência de Rigor com Erro que não Favorece o Orador:**
   - *Exemplo típico (CASO-02 - Lula herdou 6 mil obras):* O dado oficial do TCU em abril de 2023 era de 8.603 obras paralisadas. Lula citou 6.000 (errou para baixo contra seu próprio argumento). O *Verifique a Verdade* classificou como **Verdadeiro** argumentando que o erro numérico não beneficiava o orador; o *Pinóquio.live* classificou como **Enganoso** aplicando a regra de que o número real era substantivamente diferente (+43%).

3. **Divergência Jurídico-Formal vs Substantivo-Jornalística:**
   - *Exemplo crítico (CASO-12 - Flávio e investigações de milícia):* Flávio afirmou que "nunca foi investigado por envolvimento com milícia". O *Verifique a Verdade* cravou **Verdadeiro**, pois as ações penais formais no STF e MPRJ tipificaram peculato, lavagem de capitais e organização criminosa na Alerj (rachadinha), inexistindo denúncia formal pelo art. 288-A do CP (constituição de milícia armada). Em contrapartida, o *Pinóquio.live* considerou a fala **Insustentável**, pois os autos e relatórios de inteligência comprovaram vínculos diretos de contratações no gabinete da mãe e esposa do chefe do Escritório do Crime (Adriano da Nóbrega).

4. **Convergência Total em Falsidades Fáticas Absolutas:**
   - Em casos de declarações factualmente absurdas ou desprovidas de suporte probatório, houve 100% de convergência entre todos os checadores:
     - **CASO-05 (Bolsonaro e piso de R$ 600 permanente):** Falso/Enganoso (o PLOA de Bolsonaro previa R$ 405 para 2023).
     - **CASO-09 (Lula aprovar fim da escala 6x1):** Falso (a PEC está em tramitação inicial).
     - **CASO-11 (Richarlison comprar ilha do MST):** Falso (litígio estritamente privado/turístico).
     - **CASO-15 (Cartão corporativo 30% maior sob Bolsonaro):** Falso (despesas corrigidas pelo IPCA não sustentam o percentual).

---

## 2. Matriz Resumida dos 15 Casos Auditados

| ID | Tema | Candidato | Veredito Verifique os Fatos | Veredito Pinóquio.live | Veredito Verifique a Verdade | Avaliação Independente | Tipo de Divergência |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **CASO-01** | Obras TCU (11.500) | Flávio | Parcial | Enganoso | Verdadeiro | Parcialmente Verdadeiro / Enganoso no Atributivo | Metodológica / Escopo |
| **CASO-02** | Obras herdadas (6 mil) | Lula | - | Enganoso | Verdadeiro | Impreciso / Erro para baixo contra o orador | Metodológica |
| **CASO-03** | Obras (14 mil para 8 mil) | Flávio | - | Enganoso | Verdadeiro | Parcial / Bases de cálculo distintas no TCU | Metodológica / Temporal |
| **CASO-04** | Salário mínimo (R$ 900) | Lula | - | Enganoso | Verdadeiro | Verdadeiro no Conceito Central (INPC daria ~R$ 804) | Metodológica / Semântica |
| **CASO-05** | Bolsa Família R$ 600 | Flávio | Falso | Enganoso | Falso | Falso / Enganoso (EC 123/22 temporária; PLOA R$ 405) | Sem divergência relevante |
| **CASO-06** | Média Bolsa Família R$ 190 | Flávio | - | Enganoso | Falso | Falso / Enganoso (Comparação nominal sem IPCA) | Sem divergência relevante |
| **CASO-07** | Obras BR-319 | Lula | - | Enganoso | Falso | Falso / Enganoso (Trecho do meio embargado) | Sem divergência relevante |
| **CASO-08** | Túnel Santos-Guarujá | Lula | - | Enganoso | Falso | Falso no Atributivo (PPP Paritária 50% Gov SP) | Metodológica (Falso vs Enganoso) |
| **CASO-09** | Fim da escala 6x1 | Lula | - | Falso | Falso | Falso (Proposta ainda em tramitação legislativa) | Sem divergência relevante |
| **CASO-10** | IVA alíquota 28% em 2026 | Flávio | Parcial | Enganoso | Impreciso | Parcialmente Falso / Confusão de prazos e alíquotas | Sem divergência relevante |
| **CASO-11** | Richarlison ilha do MST | Flávio | Falso | Falso | Falso | Falso Absoluto (MST não possui nem vendeu ilha) | Sem divergência relevante |
| **CASO-12** | Investigação de milícia | Flávio | - | Insustentavel | Verdadeiro | Divergência Formal (tipificação) vs Factual (vínculos) | Factual / Metodológica |
| **CASO-13** | Endividamento das famílias | Flávio | - | Verdadeiro | Verdadeiro | Verdadeiro (Série BCB SGS 29037: de 49,1% a 49,9%) | Sem divergência relevante |
| **CASO-14** | Recorde de feminicídio | Flávio | - | Verdadeiro | Verdadeiro | Verdadeiro nos Registros (Anuário FBSP) | Sem divergência relevante |
| **CASO-15** | Cartão corporativo (+30%) | Lula | - | Falso | Falso | Falso (Planilhas da Presidência e CGU corrigidas) | Sem divergência relevante |
'''

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Wrote 02_RELATORIO_DE_DIVERGENCIAS.md')
