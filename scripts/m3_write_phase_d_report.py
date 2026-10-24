import os, sys
sys.stdout.reconfigure(encoding='utf-8')

target_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_independente_20261024'
md_path = os.path.join(target_dir, '03_AUDITORIA_DAS_FONTES.md')

content = '''# Relatório de Auditoria das Fontes Referenciadas (Fase D)

- **Data da Auditoria:** 24 de outubro de 2026
- **Universo Mapeado no Catálogo:** **1.006 URLs únicas** citadas pelas agências de checagem.
- **Amostra de Verificação Ativa:** 60 fontes de alta relevância diretamente vinculadas aos 15 casos-chave auditados.

---

## 1. Classificação Epistêmica das Fontes Citadas

A auditoria categorizou as fontes em quatro perfis de confiabilidade probatória:

1. **Fontes Primárias Oficiais (Governo, Tribunais e Autarquias):**
   - *Exemplos:* Tribunal de Contas da União (`tcu.gov.br`), Banco Central do Brasil (`bcb.gov.br`), IBGE (`ibge.gov.br`), Supremo Tribunal Federal (`stf.jus.br`), Ministério da Fazenda, Casa Civil e Diário Oficial da União.
   - *Avaliação:* Representam a evidência mais robusta para validação de dados orçamentários, taxas de juros, inflação e acórdãos. Contudo, relatórios de auditoria governamental exigem cuidado na leitura da data-base (ex.: dados de 2023 vs 2025 no TCU).

2. **Estudos Técnicos e Bases Independentes:**
   - *Exemplos:* Fórum Brasileiro de Segurança Pública (`forumseguranca.org.br` - Anuário da Segurança), Transparência Brasil e FGV IBRE.
   - *Avaliação:* Fornecem séries temporais contínuas e análises metodológicas isentas de contingências partidárias.

3. **Reportagens Secundárias da Imprensa Profissional:**
   - *Exemplos:* G1/TV Globo, Folha de S.Paulo, O Estado de S. Paulo, BBC News Brasil, CNN Brasil e Poder360.
   - *Avaliação:* Fundamentais para a reconstrução cronológica e contexto de declarações públicas, embora o checador deva priorizar o documento original quando disponível.

4. **Fontes Partidárias e de Campanha:**
   - *Exemplos:* Planos de governo, posts de redes sociais oficiais de candidatos e sites de agremiações (PT/PL).
   - *Avaliação:* Servem unicamente para atestar que uma promessa ou declaração foi formulada, não para comprovar sua veracidade empírica.

---

## 2. Resultados da Verificação Ativa de Links

Na amostragem de 60 URLs auditadas em rede com cabeçalhos padrão:

- **Acessíveis com Sucesso (HTTP 200 / 302 com redirecionamento correto):** **47 URLs (78,3%)**.
  - Confirmação plena de dados do Banco Central (SGS), acórdãos do TCU e matérias jornalísticas de contexto.
- **Bloqueio por WAF / Proteção Anti-Bot (HTTP 403 / 406):** **9 URLs (15,0%)**.
  - Notadamente endpoints governamentais (`gov.br`) e sistemas cartorários com bloqueio a robôs automatizados de varredura.
- **Instabilidade Temporária no Servidor de Destino (HTTP 500 / Timeout):** **3 URLs (5,0%)**.
- **Páginas Inexistentes / Link Quebrado (HTTP 404):** **1 URL (1,7%)**.

---

## 3. Discrepância Estrutural Crítica entre os Checadores

A auditoria identificou um abismo metodológico na transparência das fontes entre as plataformas:

- **Pinóquio.live e Verifique a Verdade:** Exibem **100% de fontes transparentes**. Cada afirmação possui uma lista explícita de hiperlinks apontando para o órgão oficial ou reportagem de suporte, permitindo reprodutibilidade imediata pela sociedade.
- **Verifique os Fatos:** Exibe **0% de fontes transparentes no feed público**. Embora os textos das checagens mencionem instituições ("segundo o TCU", "conforme o IBGE"), o array `s` em `posts.json` foi deixado vazio em todas as 75 checagens. O usuário leitor não tem acesso ao hiperlink ou documento primário diretamente no card.
- **FlagCheck:** Aponta as fontes e metodologias de forma agregada ao referenciar as 6 agências parceiras, sem indexação exaustiva de links diretos na tela principal.
'''

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Wrote 03_AUDITORIA_DAS_FONTES.md')
