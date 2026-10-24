# Relatório de Auditoria Estrutural e Reconciliação dos Números (Fase A)

- **Data da Auditoria:** 24 de outubro de 2026
- **Objeto Auditado:** Catálogo consolidado (`catalogo_estruturado_checagens_consolidado.csv` e `.json`) gerado na Missão 2 e inventários de preservação.
- **Ambiente de Auditoria:** `C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024\`

---

## 1. Verificação Quantitativa Exaustiva

A auditoria computacional do catálogo consolidado produziu os seguintes números exatos:

- **Total de Linhas no CSV:** **384 linhas** (1 linha de cabeçalho + 383 linhas de dados).
- **Total de Registros de Dados no CSV:** **383 registros**.
- **Total de Objetos no JSON:** **383 objetos** (100% de paridade entre CSV e JSON).
- **Duplicatas de Linhas Completas:** **0**.
- **Duplicatas de Chaves Primárias / ID no mesmo projeto:** **0**.

### Reconciliação por Projeto no Catálogo

| Projeto de Origem | Registros no Catálogo | Linhas de Dados | Registros sem Fontes | Registros sem Justificativa | Status Metodológico |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Verifique os Fatos** | 75 | 75 | 75 (100%) | 0 (0%) | 75 checagens individuais sem campos de fontes externas preenchidos |
| **Pinóquio.live** | 175 | 175 | 0 (0%) | 0 (0%) | 175 alegações checadas completas com fontes e justificativas |
| **Verifique a Verdade** | 132 | 132 | 0 (0%) | 0 (0%) | 132 artigos/cards individuais bloco a bloco |
| **FlagCheck** | 1 | 1 | 0 (0%) | 0 (0%) | 1 registro de metadados agregados do painel geral |
| **Checagem ao Vivo** | 0 | 0 | - | - | Plataforma efêmera (backend desligado pós-debate) |
| **TOTAL CONSOLIDADO** | **383** | **383** | **75** | **0** | **Reconciliação Exata e Verificada** |

---

## 2. Reconciliação Explícita: FlagCheck (152 falas vs. 1 registro no catálogo)

**A questão:** Na Missão 2 e na capa do site FlagCheck, anuncia-se *"23/10/2026 · 152 falas checadas · 6 checadores"*. No entanto, o catálogo consolidado possui apenas 1 registro do FlagCheck.

**A causa verificada:**
1. A engenharia reversa do código-fonte e do HTML servido pela rota `/eleicoes-2026/checagem-debate-globo/` demonstrou que o FlagCheck não é uma agência de checagem primária com redatores próprios em tempo real, mas sim uma plataforma de agregação estatística.
2. O HTML expõe no DOM apenas o placar geral, percentuais por candidato (Flávio: 86 falas; Lula: 66 falas), gráficos de blocos e uma seção editorial sintética de divergências.
3. Não há, no código da página nem em endpoints de API pública acessíveis no servidor, uma lista de 152 transcrições individuais estruturadas com citação e justificativa por item.
4. Por conseguinte, converter artificialmente o placar em 152 registros vazios violaria a regra de não inventar dados. O catálogo consolidou corretamente o painel em **1 registro de metadados agregados estruturados**, documentando as estatísticas globais e o Schema.org (`Article` e `Organization`).

---

## 3. Reconciliação Explícita: Contagem de Arquivos do Verifique os Fatos

**A questão:** Na Missão 2 foi citado um quantitativo preliminar de 86 arquivos para o Verifique os Fatos, enquanto outros relatórios citavam 80 ou 81.

**A contagem física auditada bit-a-bit:**
1. Na pasta de origem `verifiqueosfatos-recovery-20261024`, existem exatamente **81 arquivos** específicos do projeto Verifique os Fatos (excluindo as subpastas criadas posteriormente para os outros 4 sites).
2. Na pasta `00_ORIGINAIS_VERIFIQUE_OS_FATOS`, foram copiados exatamente **80 arquivos**.
3. A diferença de 1 arquivo corresponde a `RELATORIO_GERAL_MULTI_PLATAFORMAS.md`, que residia na raiz da pasta original e foi copiado na Missão 2 para `06_RELATORIOS_CONSOLIDADOS\RELATORIO_GERAL_MULTI_PLATAFORMAS_ORIGINAL.md`.
4. A menção a 86 arquivos decorreu da inclusão de 6 arquivos temporários e notas de scratch gerados durante a extração inicial antes da limpeza final.
5. **Conclusão:** A contagem física, reprodutível e oficial de arquivos preservados do Verifique os Fatos em `00_ORIGINAIS_VERIFIQUE_OS_FATOS` é de **exatamente 80 arquivos**.

---

## 4. Auditoria de Campos Ausentes e Integridade dos Registros

Foi gerado o arquivo analítico `01_DUPLICATAS_E_CAMPOS_AUSENTES.csv` com 815 ocorrências de campos não preenchidos:

1. **Horário / Posição (75 ausências):** As 75 checagens do *Verifique os Fatos* não registraram o campo `h` (hora/minuto da fala) no feed `posts.json`. Em contraste, *Pinóquio.live* registrou timestamp ISO exato (`said_at`) e offset em segundos, e *Verifique a Verdade* registrou o minutômetro do debate (`0:07:32`).
2. **Tema (75 ausências):** O *Verifique os Fatos* não preencheu o campo de categorização temática `a` nas checagens ativas.
3. **Fontes (75 ausências):** No *Verifique os Fatos*, nenhuma das 75 checagens preencheu a lista `s` com links externos. As verificações apoiam-se puramente no texto explicativo do parágrafo `v`. *Pinóquio.live* e *Verifique a Verdade* possuem 100% de preenchimento com URLs ativas e referências bibliográficas.
4. **Correção (`e` / 383 ausências):** O campo de errata/correção formal é opcional e não foi acionado em nenhuma checagem durante a transmissão ao vivo nas três plataformas.
5. **Afirmação Resumida (`claim` / 207 ausências):** Apenas o *Pinóquio.live* separa a citação literal (`quote`) da afirmação sintética formal (`claim`). Os demais projetos utilizam a citação literal direta.

Todos os registros possuem justificativa textual completa e veredito claramente atribuído.
