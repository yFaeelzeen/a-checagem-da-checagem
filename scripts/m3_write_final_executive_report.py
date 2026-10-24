import os, sys
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
final_md_path = os.path.join(target_dir, 'RELATORIO_FINAL_AUDITORIA_INDEPENDENTE.md')

content = '''# Relatório Executivo Final — Auditoria Factual Independente do Dossiê de Checadores

- **Data de Emissão:** 24 de outubro de 2026
- **Objeto da Auditoria:** Checagens publicadas sobre o debate presidencial da TV Globo (23/10/2026) entre Luiz Inácio Lula da Silva e Flávio Bolsonaro por cinco iniciativas:
  1. *Verifique os Fatos* (https://verifiqueosfatos.com/)
  2. *Pinóquio ao Vivo* (https://pinoquio.live/)
  3. *Verifique a Verdade* (https://verifiqueaverdade.com.br/)
  4. *FlagCheck* (https://flagcheck.com.br/)
  5. *Checagem ao Vivo* (https://checagemaovivo.org/)
- **Diretório dos Resultados:** `C:\\Users\\RAFAE\\Downloads\\dossie_auditoria_independente_20261024\\`

---

## 1. Resumo Executivo

A presente auditoria independente realizou uma investigação documental, estrutural e factual profunda sobre os dados coletados e consolidados na Missão 2. 

Principais conclusões da auditoria:
1. **Reconciliação Estrutural Rigorosa:** O catálogo consolidado possui exatamente **383 registros de dados** (384 linhas no CSV com cabeçalho), divididos em:
   - 75 do *Verifique os Fatos*
   - 175 do *Pinóquio.live*
   - 132 do *Verifique a Verdade*
   - 1 registro de painel agregado do *FlagCheck* (que agrega 152 falas de 6 agências)
   - 0 do *Checagem ao Vivo* (plataforma efêmera desligada após a transmissão).
2. **Qualidade Factual das Checagens:**
   - Em declarações comprovadamente falsas (como a compra de ilha do MST por Richarlison, a aprovação do fim da escala 6x1 ou o piso permanente de R$ 600 sob Bolsonaro), **todas as agências convergiram unanimemente** no veredito negativo.
   - Nas divergências observadas, a causa principal não foi invenção ou erro grosseiro de cálculo, mas sim **discrepância metodológica de enquadramento**: tolerar o dado numérico quando este é oficial (ex.: 11.500 obras no TCU) versus punir a atribuição de responsabilidade causal ao oponente político.
3. **Assimetria de Transparência nas Fontes:**
   - *Pinóquio.live* e *Verifique a Verdade* apresentaram **100% de transparência**, fornecendo hiperlinks diretos para fontes primárias e governamentais.
   - O *Verifique os Fatos* apresentou **0% de fontes transparentes com link no feed público**, servindo apenas textos narrativos sem hiperlinks verificáveis no card.
4. **Disparidade de Critérios Editoriais e Gatekeeping:**
   - O *Verifique os Fatos* exibiu assimetria extrema pró-Lula (95,8% de vereditos negativos para Flávio contra apenas 7,4% de negativos para Lula), decorrente de um filtro editorial que selecionou 48 falas vulneráveis de Flávio contra apenas 27 de Lula.
   - O *Verifique a Verdade* exibiu o comportamento inverso (61,3% de falas verdadeiras para Flávio contra 38,6% para Lula), fundamentado em checagens severas sobre obras federais inconclusas atribuídas ao governo atual.

---

## 2. Escopo e Metodologia da Auditoria

A auditoria operou sob princípios de reproducibilidade matemática e separação epistêmica estrita:
- **Nenhum arquivo original da Missão 1 ou Missão 2 foi alterado** (integridade 100% confirmada via SHA-256).
- Foram cruzadas as bases de dados brutas (`posts.json`, `event.json`, HTMLs SSR de Next.js) contra dados oficiais de órgãos públicos: TCU, Banco Central do Brasil (SGS), IBGE, Ministério da Fazenda, Casa Civil, Portal da Transparência, TJRJ e Fórum Brasileiro de Segurança Pública (FBSP).
- Foram analisados exaustivamente **15 casos de alta relevância**, cobrindo obras públicas, despesas de cartão corporativo, endividamento, salário mínimo, Bolsa Família, feminicídio, reforma tributária e inquéritos criminais.

---

## 3. Matriz dos Principais Casos Investigados e Avaliação Independente

| ID | Fala Original / Tema | Candidato | Veredito das Plataformas | Avaliação Factual Independente | Veredito da Auditoria |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **CASO-01** | *11.500 obras paradas no TCU* | Flávio | VoF: Parcial<br>Pin: Enganoso<br>VaV: Verdadeiro | O número do TCU (11.469) é rigorosamente verdadeiro. O erro reside na atribuição causal ("no atual governo"), pois a maioria advém de convênios municipais históricos. | **Parcialmente Verdadeiro** |
| **CASO-02** | *Lula herdou 6 mil obras paradas* | Lula | Pin: Enganoso<br>VaV: Verdadeiro | O TCU registrava 8.603 obras paralisadas em abril de 2023. Lula errou em 30% para baixo (subestimou o passivo deixado pela gestão anterior). | **Impreciso** (Erro contra si mesmo) |
| **CASO-04** | *Sem o PT, mínimo seria R$ 900* | Lula | Pin: Enganoso<br>VaV: Verdadeiro | Corrigido pelo INPC desde 2002, o salário seria R$ 804 em 2026. A tese central procede (houve ganho real substancial); o valor sem aumento real seria ainda menor que 900. | **Verdadeiro no Conceito Central** |
| **CASO-05** | *Bolsonaro deu no mínimo R$ 600* | Flávio | VoF: Falso<br>Pin: Enganoso<br>VaV: Falso | O valor sob Bolsonaro foi emergencial até 31/12/2022 (EC 123/22). O PLOA 2023 enviado por Bolsonaro previa R$ 405. A perenização decorreu da PEC da Transição. | **Falso / Enganoso** |
| **CASO-06** | *Bolsa Família média de R$ 190 no PT* | Flávio | Pin: Enganoso<br>VaV: Falso | Comparação de valor nominal de 2018 com 2026 sem ajuste inflacionário. O poder de compra de 2018 corrigido pelo IPCA é muito superior a R$ 190. | **Falso / Distorção Estatística** |
| **CASO-07** | *Estamos fazendo a BR-319* | Lula | Pin: Enganoso<br>VaV: Falso | O trecho do meio (400 km) não tem licença ambiental para pavimentação e segue embargado judicialmente. Há apenas manutenção. | **Falso / Enganoso** |
| **CASO-08** | *Túnel Santos-Guarujá: dinheiro é nosso* | Lula | Pin: Enganoso<br>VaV: Falso | A obra é uma PPP com cofinanciamento paritário de 50% do Governo Federal e 50% do Estado de SP (Tarcísio de Freitas), além de capital privado. | **Falso no Atributivo** |
| **CASO-09** | *Aprovamos o fim da escala 6x1* | Lula | Pin: Falso<br>VaV: Falso | A PEC da jornada ainda tramita no Congresso e não foi votada nem aprovada. | **Falso** |
| **CASO-10** | *IVA cobrado ano que vem será 28%* | Flávio | VoF: Parcial<br>Pin: Enganoso<br>VaV: Impreciso | A cobrança em 2026 será apenas um teste de 1% que abate tributos existentes. A alíquota de 28% é estimativa de teto para 2033. | **Parcialmente Falso** |
| **CASO-11** | *Richarlison comprou ilha do MST* | Flávio | VoF: Falso<br>Pin: Falso<br>VaV: Falso | O litígio de posse na Ilha Grande é com empresa privada e posseiros locais. O MST não tem qualquer relação com o imóvel. | **Falso Absoluto** |
| **CASO-12** | *Nunca fui investigado por milícia* | Flávio | Pin: Insustentável<br>VaV: Verdadeiro | Tecnicamente não houve inquérito pelo crime autônomo de milícia armada (art. 288-A), mas houve investigações e vínculos probatórios com membros da cúpula do Escritório do Crime no gabinete. | **Divergência Formal vs Factual** |
| **CASO-13** | *Brasileiros estão devendo mais* | Flávio | Pin: Verdadeiro<br>VaV: Verdadeiro | O endividamento das famílias medido pelo Banco Central (Série SGS 29037) passou de 49,1% em 2022 para 49,9% da renda anual em 2026. | **Verdadeiro** |
| **CASO-14** | *Recorde de feminicídio no Brasil* | Flávio | Pin: Verdadeiro<br>VaV: Verdadeiro | O Anuário do Fórum Brasileiro de Segurança Pública e o MJSP confirmam os maiores patamares absolutos da série histórica (mais de 1.400 vítimas/ano). | **Verdadeiro nos Dados Oficiais** |
| **CASO-15** | *Bolsonaro gastou +30% em cartão* | Lula | Pin: Falso<br>VaV: Falso | Planilhas da Presidência da República desclassificadas pela CGU com correção pelo IPCA não corroboram a diferença de 30%. | **Falso** |

---

## 4. Análise de Viés e Consistência Metodológica

A auditoria separou com rigor **três planos de constatação**:

### 1. Fatos Demonstrados
- O *Verifique os Fatos* atribuiu **95,8% de rótulos negativos a Flávio Bolsonaro** e **66,7% de rótulos positivos a Lula**. O site dedicou quase 2/3 de sua cobertura a focar falas de Flávio e não disponibilizou fontes no feed.
- O *Verifique a Verdade* atribuiu **28,1% de vereditos Falso a Lula contra apenas 12,0% para Flávio**, concedendo 61,3% de Verdadeiro a Flávio.
- O *Pinóquio.live* foi o mais abrangente (175 checagens) e aplicou penalizações equilibradas a ambos por meio de nuances como "Enganoso" e "Exagerado", mantendo taxas de "Verdadeiro" superiores a 55% para ambos os candidatos.

### 2. Indícios que Justificam Investigação
- O fenômeno de *Gatekeeping* (seleção de quais falas checar): ao selecionar apenas falas frágeis de um concorrente e declarações consolidadas do outro, um checador consegue produzir um placar amplamente desfavorável sem necessariamente falsificar o texto de cada checagem individual.

### 3. Hipóteses Não Comprovadas
- Não foi comprovada adulteração maliciosa de dados brutos ou conluio. As divergências decorrem essencialmente da linha editorial de cada iniciativa e do nível de rigor aplicado a afirmações aproximadas.

---

## 5. Limitações da Coleta e Questões Inconclusivas

1. **Checagem ao Vivo:** Não foi possível auditar as checagens pontuais do *Checagem ao Vivo* porque a plataforma foi desligada após a transmissão, servindo apenas tela de agradecimento.
2. **FlagCheck:** A ausência de uma API ou listagem com o texto integral das 152 transcrições impede a auditoria individualizada de cada frase agregada por suas 6 agências parceiras.

---

## 6. Confirmação de Integridade dos Arquivos

Todos os 140 arquivos da pasta original preservada (`verifiqueosfatos-recovery-20261024`) e todos os arquivos da pasta da Missão 2 foram conferidos bit-a-bit via SHA-256 e **permaneceram estritamente intactos**.
'''

with open(final_md_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Wrote RELATORIO_FINAL_AUDITORIA_INDEPENDENTE.md successfully.')
