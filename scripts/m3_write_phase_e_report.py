import os, sys
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
md_path = os.path.join(target_dir, '04_CONSISTENCIA_METODOLOGICA.md')

content = '''# Relatório de Consistência Metodológica e Análise de Cobertura (Fase E)

- **Data da Auditoria:** 24 de outubro de 2026
- **Objetivo:** Avaliar a simetria de critérios, distribuição de temas, volume de cobertura e proporcionalidade de vereditos entre Lula e Flávio Bolsonaro nas diferentes plataformas.
- **Princípio Epistêmico:** Separação estrita entre (1) fatos demonstrados; (2) indícios que justificam investigação; e (3) hipóteses não comprovadas. Não inferir viés partidário automaticamente a partir de discrepâncias puramente numéricas sem examinar a complexidade das declarações.

---

## 1. Fatos Demonstrados (Evidências Numéricas Estritas)

### A. Assimetria Radical no Verifique os Fatos (`verifiqueosfatos.com`)
A análise computacional das 75 checagens publicadas pelo *Verifique os Fatos* revelou um contraste extremo na distribuição de vereditos:
- **Flávio Bolsonaro (48 checagens):**
  - **Falso:** 24 (50,0%)
  - **Parcial:** 22 (45,8%)
  - **Verdadeiro:** 2 (4,2%)
  - *Proporção negativa (Falso + Parcial):* **95,8%**
- **Lula (27 checagens):**
  - **Verdadeiro:** 18 (66,7%)
  - **Parcial:** 7 (25,9%)
  - **Falso:** 2 (7,4%)
  - *Proporção positiva (Verdadeiro):* **66,7%**

Além disso, houve assimetria no volume de checagens: o projeto dedicou **64% de todo o seu esforço editorial** a Flávio Bolsonaro (48 checagens contra 27 de Lula), com taxa de aprovação de apenas 4,2% para Flávio versus 66,7% para Lula.

---

### B. Distribuição no Pinóquio ao Vivo (`pinoquio.live`)
O *Pinóquio.live* utilizou uma taxonomia de 5 níveis (`verdadeiro`, `falso`, `enganoso`, `exagerado`, `insustentavel`) com volume substancialmente maior (175 checagens):
- **Flávio Bolsonaro (101 checagens):**
  - **Verdadeiro:** 57 (56,4%)
  - **Enganoso:** 23 (22,8%)
  - **Falso:** 8 (7,9%)
  - **Exagerado:** 7 (6,9%)
  - **Insustentável:** 6 (5,9%)
- **Lula (74 checagens):**
  - **Verdadeiro:** 52 (70,3%)
  - **Exagerado:** 8 (10,8%)
  - **Enganoso:** 7 (9,5%)
  - **Falso:** 5 (6,8%)
  - **Insustentável:** 2 (2,7%)

No *Pinóquio.live*, a maioria das afirmações de ambos os candidatos recebeu o rótulo positivo de Verdadeiro (56,4% para Flávio e 70,3% para Lula). A principal penalização aplicada a Flávio concentrou-se no rótulo intermediário de "Enganoso" (22,8%), especialmente ao atribuir a governos petistas a responsabilidade exclusiva por indicadores históricos ou taxas nominais.

---

### C. Inversão no Verifique a Verdade (`verifiqueaverdade.com.br`)
O *Verifique a Verdade* apresentou um quadro oposto ao do *Verifique os Fatos*:
- **Flávio Bolsonaro (75 checagens):**
  - **Verdadeiro:** 46 (61,3%)
  - **Impreciso:** 14 (18,7%)
  - **Falso:** 9 (12,0%)
  - **Não verificável:** 6 (8,0%)
- **Lula (57 checagens):**
  - **Verdadeiro:** 22 (38,6%)
  - **Impreciso:** 17 (29,8%)
  - **Falso:** 16 (28,1%)
  - **Não verificável:** 2 (3,5%)

Neste projeto, Lula teve **mais que o dobro de vereditos negativos absolutos (Falso: 28,1% vs 12,0% de Flávio)** e uma taxa de Verdadeiro muito menor (38,6% vs 61,3%). A justificativa editorial explícita do site argumentou que Lula incorreu em erros fáticos severos sobre obras federais (BR-319, Túnel Santos-Guarujá, leilão de dívidas) e esgotou seu tempo no tema livre sem apresentar alegações factualmente sustentadas.

---

## 2. Indícios que Justificam Investigação

1. **Seleção de Falas (Gatekeeping Assimétrico):**
   - O *Verifique os Fatos* selecionou 48 frases de Flávio focadas prioritariamente em temas de alta vulnerabilidade (acusações sobre Richarlison, 11.500 obras, auxílio eleitoral) e apenas 27 de Lula, poupando o mandatário de checagens minuciosas sobre promessas legislativas (como a aprovação da escala 6x1) ou gastos com cartões corporativos.
   
2. **Critérios de Tolerância Editorial Diferenciados:**
   - Em *Verifique a Verdade*, observou-se uma regra metodológica flexível em que erros numéricos de Lula que jogavam contra ele mesmo (ex.: dizer que herdou 6 mil obras quando eram 8,6 mil) receberam o selo "Verdadeiro", enquanto em *Pinóquio* o mesmo tipo de discrepância ensejou "Enganoso".
   - Por outro lado, o *Verifique a Verdade* foi extremamente rigoroso com Lula ao julgar "Falso" declarações sobre projetos em andamento ("estamos fazendo"), enquanto concedeu "Verdadeiro" a Flávio no caso da milícia ao adotar a interpretação puramente penal e formal do inquérito.

---

## 3. Hipóteses Não Comprovadas

1. **Hipótese de Má-Fé Deliberada ou Orquestração Partidária:**
   - Embora as distribuições estatísticas entre *Verifique os Fatos* (pró-Lula) e *Verifique a Verdade* (pró-Flávio) apontem discrepâncias gritantes de placar, a auditoria não encontrou evidências técnicas de código, injeção artificial de dados ou dolo configurado.
   - A divergência decorre primordialmente da **linha editorial de seleção de falas (sample bias)** e da **filosofia de checagem**: punir a intenção versus punir a literalidade do dado técnico.
'''

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Wrote 04_CONSISTENCIA_METODOLOGICA.md')
