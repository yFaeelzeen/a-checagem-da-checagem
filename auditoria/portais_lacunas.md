# Relatório Consolidado de Lacunas, Limitações de Coleta e Tratamento de Plataformas Efêmeras

- **Data da Auditoria:** 24 de outubro de 2026
- **Finalidade:** Documentar rigorosamente as limitações metodológicas, o tratamento específico do *FlagCheck* e do *Checagem ao Vivo*, e as fronteiras epistêmicas da lista fechada de quatro fontes autorizadas.

---

## 1. Tratamento Específico do FlagCheck e do Checagem ao Vivo

A auditoria aplicou as diretrizes estritas da Missão 4 para evitar qualquer distorção ou fabricação de registros:

### A. FlagCheck (https://flagcheck.com.br/)
- **Situação no Dossiê:** O catálogo da Missão 2 possui **apenas 1 registro agregado de metadados**, representativo do painel geral que monitorou 152 falas categorizadas por 6 agências.
- **Rigor Metodológico Aplicado:**
  1. A auditoria **não transformou o painel de 152 falas em 152 fichas individuais fictícias**.
  2. O FlagCheck é tratado estritamente como um agregador estatístico e de metadados Schema.org.
  3. Quando uma fala aparece checada no UOL, G1, Estadão ou Lupa, ela foi registrada estritamente sob o veículo original que a publicou, **nunca como se o texto integral tivesse sido recuperado da base interna do FlagCheck**.
  4. Nenhum veredito arbitrário foi imputado ao FlagCheck onde a plataforma apenas exibia percentuais de convergência.

---

### B. Checagem ao Vivo (https://checagemaovivo.org/)
- **Situação no Dossiê:** Foram recuperadas **zero fichas individuais de checagem**.
- **Distinção Fundamental:** A condição de **zero fichas recuperadas** decorre do encerramento da infraestrutura de backend após a transmissão ao vivo (retornando HTTP 503 e servindo tela estática de agradecimento), o que **não significa que a iniciativa tenha realizado zero checagens durante o evento**.
- **Rigor Metodológico Aplicado:**
  1. Nenhuma checagem foi deduzida ou retroalimentada artificialmente para preencher a coluna do Checagem ao Vivo.
  2. Todos os relatórios de síntese registram a situação do Checagem ao Vivo como *"Não disponível no material acessível (serviço offline pós-debate)"*.

---

## 2. Limitações da Lista Fechada de Quatro Fontes Autorizadas

Conforme a cláusula 2 do mandato da Missão 4, a verificação externa restringiu-se exclusivamente às quatro URLs autorizadas:

1. **UOL Confere (1 URL):**
   - *Limitação:* O artigo específico referenciado (`debate-globo-checagem-flavio-lula.ghtm`) concentrou 26 checagens voltadas para o candidato Flávio Bolsonaro. As checagens de Lula da mesma noite podem ter sido publicadas em páginas correlatas ou atualizações de liveblog não incluídas na URL fornecida. Em respeito à proibição de buscar URLs externas, a auditoria registrou apenas o que constava na página autorizada.
2. **Estadão Verifica (1 URL AMP):**
   - *Limitação:* A URL AMP continha uma cobertura muito ampla (93 blocos), com tópicos detalhados minuto a minuto, exibindo excelente equilíbrio paritário entre Lula e Flávio.
3. **G1 — Fato ou Fake (1 URL AMP):**
   - *Limitação:* O artigo continha 57 checagens, com predominância de notas breves sobre Lula (47 falas) e 10 de Flávio.
4. **Agência Lupa (1 URL WordPress):**
   - *Limitação:* O artigo cobriu mais de 40 declarações com foco em temas polêmicos e declarações de dados históricos.

---

## 3. Síntese Epistêmica das Lacunas

| Categoria | Definição Formal | Casos Reais na Auditoria |
| :--- | :--- | :--- |
| **Ausência Confirmada** | O recurso ou declaração foi procurado na página autorizada e confirmou-se que a reportagem não o abordou. | Alegações sobre feminicídio e Serra das Araras não checadas pelo UOL nesta URL específica. |
| **Inacessibilidade Técnica** | Erro de rede ou protocolo no momento do acesso. | UOL exigiu cabeçalho compatível com navegador móvel para contornar HTTP 403 do WAF. Checagem ao Vivo inacessível (503). |
| **Conteúdo Parcial** | O veículo citou a fala, mas publicou nota curta sem explicar o denominador exato. | Algumas notas breves do G1 sobre gastos do PAC. |
| **Situação Indeterminada** | A fonte autorizada não fornece elementos textuais suficientes para julgar a compatibilidade com outro veículo. | Comparação entre estimativas de alíquotas futuras em que o veículo não cita o ano de vigência. |
