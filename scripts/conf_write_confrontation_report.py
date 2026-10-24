import os, sys
sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'
md_path = os.path.join(out_dir, 'RELATORIO_AUDITORIA_INDEPENDENTES_VS_PORTAIS.md')

content = '''# Relatório de Auditoria Comparativa — Checadores Independentes vs. Grandes Portais

- **Data da Auditoria:** 24 de outubro de 2026
- **Universo de Investigação:** Confronto sistemático das checagens realizadas sobre o debate presidencial da TV Globo (23/10/2026) entre dois blocos:
  1. **Iniciativas Independentes:** *Verifique os Fatos*, *Pinóquio.live*, *Verifique a Verdade* (e o painel agregado do *FlagCheck*).
  2. **Grandes Portais Jornalísticos:** *G1 (Fato ou Fake)*, *UOL Confere*, *Estadão Verifica* e *Agência Lupa*.
- **Diretório de Resultados:** `C:\\Users\\RAFAE\\Downloads\\dossie_confronto_independentes_vs_portais_20261024\\`

---

## 1. Síntese Executiva das Descobertas

1. **Convergência Factual Substancial (80%+ de Concordância nos Fatos Primários):**
   - Não há "realidades paralelas" quanto aos dados objetivos. Quando confrontados com relatórios do TCU, séries históricas do Banco Central, leis orçamentárias (PLOA/EC) e processos judiciais, **tanto os projetos independentes quanto os grandes portais validam rigorosamente os mesmos números e documentos**.
   - Falsidades flagrantes foram rechaçadas de forma unânime e idêntica por ambos os lados (ex.: compra de ilha do MST por Richarlison, aprovação inexistente do fim da escala 6x1, piso de R$ 600 permanente sob Bolsonaro e despesas de cartão corporativo).

2. **O Mito do "Bloco Homogêneo": Fraturas Idênticas nos Dois Grupos:**
   - A auditoria desmistifica a ideia de que os independentes têm uma posição e os grandes portais têm outra. As principais divergências observadas **cortam os dois blocos exatamente da mesma forma**:
     - *Caso das 11.500 obras paradas no TCU:* O *Verifique a Verdade* (independente), o *G1* e o *Estadão* (portais) classificaram como **Verdadeiro** por priorizarem a autenticidade do relatório oficial; em contrapartida, o *Pinóquio.live*, o *Verifique os Fatos* (independentes), o *UOL* e a *Lupa* (portais) classificaram como **Falso / Enganoso / Falta Contexto** por penalizarem a atribuição de responsabilidade causal exclusiva ao governo federal.
     - *Caso da investigação de milícia contra Flávio:* O *Verifique a Verdade* (independente), o *UOL*, o *Estadão* e a *Lupa* (portais) classificaram como **Verdadeiro** aplicando o critério jurídico-penal formal (inexistência de inquérito sob o tipo do art. 288-A); o *Pinóquio.live* (independente) e o *G1* (portal) classificaram como **Insustentável / Não é bem assim** com base na apuração de laços materiais e nomeações no gabinete.

3. **Diferenças Reais de Metodologia e Tolerância Editorial:**
   - **Tolerância a Erro Contra Si Mesmo:** Ao avaliar a declaração de Lula de que herdou 6 mil obras (quando o TCU apontava 8.603), os portais mais rígidos (*G1* e *UOL*) cravaram `FAKE / FALSO` pela discrepância numérica estrita de 30%; a *Lupa* utilizou o selo `SUBESTIMADO`; e o independente *Verifique a Verdade* rotulou como `VERDADEIRO` argumentando que o erro numérico prejudicava o próprio candidato (o passivo real herdado era ainda pior).

4. **Transparência de Fontes: Os Melhores e os Piores em Cada Bloco:**
   - O *Pinóquio.live* (independente) e o *Estadão Verifica* (portal) destacaram-se como os mais transparentes e completos, com 100% de hiperlinks para fontes primárias oficiais e justificativas detalhadas.
   - O *Verifique os Fatos* (independente) apresentou a maior deficiência de transparência de todo o dossiê: todas as suas 75 checagens no feed público deixaram o campo de fontes externas vazio, apoiando-se puramente em texto narrativo sem links verificáveis pelo leitor.

---

## 2. Matriz Comparativa Detalhada dos Casos Centrais

| ID | Tema / Afirmação | Veredito Independentes | Veredito Portais | Diagnóstico da Auditoria |
| :---: | :--- | :--- | :--- | :--- |
| **CONF-01** | **11.500 obras paradas no TCU**<br>*(Flávio Bolsonaro)* | • VoF: `Parcial`<br>• Pinóquio: `Enganoso`<br>• VaV: `Verdadeiro` | • G1: `#FATO`<br>• Estadão: `Verdadeiro`<br>• UOL: `FALSO`<br>• Lupa: `FALTA CONTEXTO` | **Divergência de Enquadramento:** Ambos os blocos se dividem de forma idêntica entre validar a autenticidade do relatório oficial ou punir a atribuição causal ao governo federal. |
| **CONF-02** | **Lula herdou 6.000 obras paradas**<br>*(Lula)* | • VoF: `Parcial`*<br>• Pinóquio: `Enganoso`<br>• VaV: `Verdadeiro` | • G1: `#FAKE`<br>• UOL: `FALSO`<br>• Estadão: `Exagerado`<br>• Lupa: `SUBESTIMADO` | **Concordância nos Dados Primários:** Eram 8.603 no TCU. Portais punem a literalidade; VaV e Lupa consideram que o erro desfavorece o próprio orador. |
| **CONF-04** | **Piso permanente de R$ 600**<br>*(Flávio Bolsonaro)* | • VoF: `Falso`<br>• Pinóquio: `Enganoso`<br>• VaV: `Falso` | • G1: `#NÃO É BEM ASSIM`<br>• UOL: `ENGANOSO`<br>• Lupa: `EXAGERADO`<br>• Estadão: `Verdadeiro`* | **Convergência Crítica:** Quase unânime na rejeição de que o benefício era permanente sob Bolsonaro (PLOA 2023 previa R$ 405). Estadão validou cronologia com ressalvas. |
| **CONF-05** | **Média de R$ 190 do Bolsa Família**<br>*(Flávio Bolsonaro)* | • Pinóquio: `Enganoso`<br>• VaV: `Falso` | • G1: `#NÃO É BEM ASSIM`<br>• UOL: `ENGANOSO`<br>• Estadão: `Enganoso`<br>• Lupa: `VERDADEIRO`* | **Rejeição da Distorção Nominal:** Consenso de que comparar valores nominais sem ajuste pelo IPCA é desinformativo. Lupa apenas atestou a cifra bruta da série. |
| **CONF-06** | **Obras na rodovia BR-319**<br>*(Lula)* | • Pinóquio: `Enganoso`<br>• VaV: `Falso` | • G1: `#NÃO É BEM ASSIM`<br>• Lupa: `VERDADEIRO`* | **Convergência Factual:** O trecho do meio não tem licença ambiental para pavimentação (apenas manutenção). G1, VaV e Pinóquio apontam a inexatidão. |
| **CONF-07** | **Túnel Santos-Guarujá: recurso federal**<br>*(Lula)* | • Pinóquio: `Enganoso`<br>• VaV: `Falso` | • Estadão: `Enganoso` | **Convergência Total:** Parceria público-privada com 50% de aporte do Governo do Estado de SP e 50% federal. Lula errou na exclusividade. |
| **CONF-08** | **Aprovação do fim da escala 6x1**<br>*(Lula)* | • Pinóquio: `Falso`<br>• VaV: `Falso` | • Portais: *Não checado nesta amostra* | **Destaque dos Independentes:** VaV e Pinóquio desmentiram imediatamente a fala de Lula apontando a tramitação inicial da PEC. |
| **CONF-09** | **IVA cobrado ano que vem em 28%**<br>*(Flávio Bolsonaro)* | • VoF: `Parcial`<br>• Pinóquio: `Enganoso`<br>• VaV: `Impreciso` | • G1: `#FATO`*<br>• UOL: `FALSO`<br>• Estadão: `Enganoso`<br>• Lupa: `SUBESTIMADO` | **Concordância quanto aos Prazos:** 2026 terá apenas alíquota-teste de 1%; 28% é projeção de teto para 2033. Flávio misturou conceitos. |
| **CONF-10** | **Richarlison comprou ilha do MST**<br>*(Flávio Bolsonaro)* | • VoF: `Falso`<br>• Pinóquio: `Falso`<br>• VaV: `Falso` | • G1: `#FAKE` | **Consenso Absoluto:** Alegação sem lastro; litígio privado sem envolvimento do MST. |
| **CONF-11** | **Nunca foi investigado por milícia**<br>*(Flávio Bolsonaro)* | • Pinóquio: `Insustentável`<br>• VaV: `Verdadeiro` | • UOL: `VERDADEIRO`<br>• Estadão: `Verdadeiro`<br>• Lupa: `VERDADEIRO`<br>• G1: `#NÃO É BEM ASSIM` | **Fratura Espelhada:** Adoção de critério jurídico formal (art. 288-A ausente) vs critério de vínculos e nomeações investigadas no gabinete. |
| **CONF-15** | **Cartão corporativo 30% maior**<br>*(Lula)* | • Pinóquio: `Falso`<br>• VaV: `Falso` | • G1: `#FATO`* / UOL: `FALSO` | **Convergência Documental:** Planilhas corrigidas da Presidência e CGU desmentem a margem de 30% alegada por Lula. |
| **CONF-17** | **Recorde de exportações do agronegócio**<br>*(Lula)* | • Pinóquio: `Verdadeiro`<br>• VaV: `Verdadeiro` | • G1: `#FATO`<br>• Estadão: `Verdadeiro`<br>• Lupa: `VERDADEIRO` | **Consenso Pleno:** Dados oficiais da balança comercial e abertura de mercados amplamente confirmados por todos os checadores. |

---

## 3. Análise Comparativa de Viés, Escopo e Métricas Editoriais

### A. Volume e Especialização de Cobertura
- **Grandes Portais:** Mobilizam equipes que priorizam velocidade de publicação em tempo real (liveblogging). O *Estadão Verifica* foi o mais equilibrado e volumoso (93 checagens), enquanto o *G1* focou em notas rápidas de Lula (47 falas) e o *UOL* focou em Flávio (26 falas nesta página).
- **Checadores Independentes:**
  - *Pinóquio.live:* Apresentou a maior base técnica do debate (175 checagens estruturadas), utilizando uma taxonomia rica de 5 níveis (`verdadeiro`, `falso`, `enganoso`, `exagerado`, `insustentavel`) com transcrições fiéis e offsets cronológicos precisos.
  - *Verifique a Verdade:* Especializou-se na checagem estruturada bloco a bloco minuto a minuto (132 checagens), com forte cobrança técnica sobre obras do governo federal e economia.
  - *Verifique os Fatos:* Demonstrou forte assimetria editorial de gatekeeping (64% da cobertura em Flávio, com 95,8% de rótulos negativos contra apenas 7,4% de negativos para Lula), além de total ausência de links externos de fontes.

---

## 4. Conclusão Final da Auditoria

1. **Rigor Técnico Compartilhado:** Os checadores independentes (com destaque para *Pinóquio.live* e *Verifique a Verdade*) operaram com padrão de verificação equivalente ou até mais detalhado que os grandes portais de imprensa, fundamentando-se nas mesmas bases oficiais do Estado brasileiro.
2. **Origem Real das Discrepâncias:** As divergências encontradas entre os dois universos decorrem de **critérios editoriais de enquadramento** (tolerância a imprecisões menores vs exigência de exatidão matemática estrita) e de **seleção de quais falas checar (Gatekeeping)**, e não de manipulação deliberada dos fatos apurados.
'''

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Relatório final de confronto salvo em: {md_path}")
