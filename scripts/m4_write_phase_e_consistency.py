import os, sys
sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'
md_path = os.path.join(out_dir, '05_CONSISTENCIA_EDITORIAL_LULA_FLAVIO.md')

content = '''# Análise de Consistência Editorial e Avaliação de Simetria entre Lula e Flávio Bolsonaro

- **Data da Auditoria:** 24 de outubro de 2026
- **Escopo:** Avaliação rigorosa da distribuição quantitativa, seleção temática e critérios de rigor aplicados às falas dos dois candidatos pelos quatro veículos autorizados (UOL Confere, G1, Estadão Verifica e Agência Lupa).

---

## 1. Cobertura Quantitativa e Gatekeeping

A tabela abaixo consolida o total de checagens individuais identificadas nas reportagens das quatro publicações:

| Veículo | Total de Checagens | Checagens de Lula | Checagens de Flávio | Proporção Lula / Flávio |
| :--- | :---: | :---: | :---: | :---: |
| **G1 — Fato ou Fake** | 57 | 47 (82,5%) | 10 (17,5%) | Forte assimetria em direção a Lula |
| **Estadão Verifica** | 93 | 45 (48,4%) | 48 (51,6%) | **Paridade quantitativa estrita** |
| **Agência Lupa** | 43 | 13 (30,2%) | 30 (69,8%) | Assimetria em direção a Flávio |
| **UOL Confere** | 26 | 0* (0,0%) | 26 (100,0%) | Foco exclusivo em falas de Flávio |
| **TOTAL CONSOLIDADO** | **219** | **105 (47,9%)** | **114 (52,1%)** | **Equilíbrio Agregado Quase Perfeito** |

*\*Nota sobre o UOL Confere:* A URL autorizada do UOL capturou a tranche focada na verificação em tempo real das falas de Flávio Bolsonaro durante os blocos iniciais do debate, não contendo checagens estruturadas de Lula nesta página específica. Em contraste, o G1 concentrou o maior volume de notas curtas sob o perfil de Lula, enquanto o Estadão manteve divisão rigorosamente paritária (45 vs 48).

---

## 2. Padrões de Rigor e Tratamento de Declarações Equivalentes

A auditoria examinou se os veículos aplicaram a mesma régua metodológica a estruturas argumentativas análogas de ambos os candidatos:

### Caso A: Número Correto com Atribuição Causal Controversa
- **Flávio (11.500 obras do TCU):** O número é correto segundo o TCU, mas as obras pertencem a convênios municipais.
  - *Tratamento:* UOL puniu como `FALSO`; G1 e Estadão premiaram como `FATO / Verdadeiro`; Lupa usou `FALTA CONTEXTO`.
- **Lula (R$ 800 bi executados no PAC):** O montante de investimento somando todas as fontes é real segundo a Secom, mas inclui aportes estatais e privados não diretamente decorrentes do orçamento federal.
  - *Tratamento:* G1 e Estadão concederam `FATO / Verdadeiro`; Lupa pontuou que inclui desembolsos de estatais e concessões.
- *Avaliação:* **Critério Simétrico.** G1 e Estadão mantiveram a mesma tolerância em ambos os casos, validando a existência do indicador público.

---

### Caso B: Erro Numérico que Desfavorece o Próprio Orador
- **Lula (Herdou 6 mil obras paradas quando eram 8.603):** Errou para baixo, subestimando o passivo da gestão Bolsonaro.
  - *Tratamento:* G1 cravou `#FAKE`; UOL cravou `FALSO`; Lupa usou `SUBESTIMADO`.
- **Flávio (Bolsonaro entregou com pouco mais de 8 mil obras):** Citou o número do diagnóstico de abril de 2023 do TCU.
  - *Tratamento:* Foi validado com ressalva sobre a mudança da base total de auditoria.
- *Avaliação:* O rótulo taxativo de `#FAKE` do G1 sobre o dado de 6 mil obras de Lula demonstra **aplicação estrita e implacável da literalidade numérica**, sem concessões hermenêuticas para a intenção do orador.

---

### Caso C: Alegações Factualmente Inexistentes
- **Lula (Aprovação do fim da escala 6x1):** A PEC está apenas tramitando.
  - *Tratamento:* Rejeição unânime como falso/sem respaldo.
- **Flávio (Richarlison comprou ilha do MST):** O MST não tem relação com o imóvel.
  - *Tratamento:* Rejeição unânime como falso/fake.
- *Avaliação:* **Simetria Total.** Nenhuma agência atenuou falsidades demonstráveis de qualquer um dos lados.

---

## 3. Conclusões Sustentadas sobre Viés Editorial

1. **Inexistência de Viés Sistêmico Homogêneo na Imprensa:**
   - Não se sustenta a hipótese de alinhamento orquestrado das quatro agências. O G1 checou proporcionalmente muito mais falas de Lula (47 a 10), enquanto a Lupa checou mais falas de Flávio (30 a 13) e o Estadão dividiu quase cirurgicamente o espaço (45 a 48).
2. **Causa Real das Diferenças de Placar:**
   - A disparidade entre os placares observados decorre do **recorte de amostragem (Gatekeeping)** e do **tamanho da redação/tempo de apuração**. Cada veículo seleciona as frases de acordo com o impacto no momento do debate.
3. **Robustez dos Fatos Primários:**
   - Quando confrontados com documentos legais, relatórios do TCU, leis orçamentárias e séries do IBGE/Banco Central, os quatro veículos apresentaram consistência plena quanto aos dados de base.
'''

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Wrote 05_CONSISTENCIA_EDITORIAL_LULA_FLAVIO.md')
