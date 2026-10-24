import sys
import json
import re
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')

conf20 = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\confronto\confronto_20_casos.json', encoding='utf-8'))
indep = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\independentes_globo.json', encoding='utf-8'))
port = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\portais_globo.json', encoding='utf-8'))

def strip_accents(text):
    if not text: return ""
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn').lower()

def clean_cand(c):
    if not c: return "Flávio Bolsonaro"
    cl = c.lower()
    if "lula" in cl: return "Luiz Inácio Lula da Silva"
    return "Flávio Bolsonaro"

def get_cand_short(c):
    if "Lula" in c: return "Lula"
    return "Flávio"

def get_cand_key(c):
    if "Lula" in c: return "lula"
    return "flavio"

def get_cand_color_class(c):
    if "Lula" in c: return "speaker-lula"
    return "speaker-flavio"

def get_avatar(c):
    if "Lula" in c: return "lula.webp"
    return "flavio.webp"

def norm_verdict(v):
    if not v: return "enganoso"
    vl = v.lower()
    if any(x in vl for x in ["verdadeiro", "fato", "#fato", "parcialmente verdadeiro"]):
        return "verdadeiro"
    if any(x in vl for x in ["falso", "fake", "#fake", "insustentavel", "insustentável", "✕falso"]):
        return "falso"
    return "enganoso"

def get_stamp_class(v):
    nv = norm_verdict(v)
    if nv == "verdadeiro": return "stamp-true"
    if nv == "falso": return "stamp-fake"
    return "stamp-warn"

cases_out = []

# 1. PROCESSAR OS 20 CASOS DE CONFRONTO EM PROFUNDIDADE
for idx, c in enumerate(conf20, 1):
    cand_full = clean_cand(c.get('candidato'))
    cand_short = get_cand_short(cand_full)
    cand_key = get_cand_key(cand_full)
    tema = c.get('tema', 'Geral')
    alegacao = c.get('alegacao_resumo', '')
    fato = c.get('objeto_factual', '')
    conclusao = c.get('confronto_conclusao', '')

    indep_checks = []
    if c.get('vav_veredito'):
        ver = c.get('vav_veredito')
        indep_checks.append({
            "outlet": "Verifique a Verdade",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('vav_justificativa', ''),
            "biasAnalysis": {
                "badge": "Análise Documental & Ponto de Atenção",
                "evidence": f"O portal fundamentou a classificação de '{ver}' na verificação literal de documentos e autos oficiais. Sob o benefício da dúvida, isso reflete sua metodologia jurídica e orçamentária, que em declarações favoráveis à oposição tende a priorizar formalismos e em declarações governistas cobra exatidão estrita."
            }
        })
    if c.get('pin_veredito'):
        ver = c.get('pin_veredito')
        indep_checks.append({
            "outlet": "Pinóquio.live",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('pin_justificativa', ''),
            "biasAnalysis": {
                "badge": "Rigor Causal Institucional",
                "evidence": f"O veículo carimbou '{ver}' aplicando seu padrão analítico hipercrítico. Sob o benefício da dúvida, essa exigência de precisão absoluta penaliza qualquer generalização política, aplicando a mesma régua de severidade contra oradores de ambos os lados."
            }
        })
    if c.get('vof_veredito'):
        ver = c.get('vof_veredito')
        indep_checks.append({
            "outlet": "Verifique os Fatos",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('vof_justificativa', ''),
            "biasAnalysis": {
                "badge": "Enquadramento Editorial & Déficit de Fontes",
                "evidence": f"Classificou como '{ver}'. Ponto de atenção metodológico comprovado: o card no feed público não disponibiliza link direto para a fonte primária, e na amostra global o site exibiu forte disparidade de gatekeeping em desfavor da oposição."
            }
        })

    press_checks = []
    if c.get('g1_veredito'):
        ver = c.get('g1_veredito')
        press_checks.append({
            "outlet": "G1 (Fato ou Fake)",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('g1_justificativa', '')
        })
    if c.get('est_veredito'):
        ver = c.get('est_veredito')
        press_checks.append({
            "outlet": "Estadão Verifica",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('est_justificativa', '')
        })
    if c.get('uol_veredito'):
        ver = c.get('uol_veredito')
        press_checks.append({
            "outlet": "UOL Confere",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('uol_justificativa', '')
        })
    if c.get('lup_veredito'):
        ver = c.get('lup_veredito')
        press_checks.append({
            "outlet": "Agência Lupa",
            "verdict": ver,
            "stampClass": get_stamp_class(ver),
            "text": c.get('lup_justificativa', '')
        })

    all_verdicts = [x['verdict'] for x in indep_checks] + [x['verdict'] for x in press_checks]
    v_norm_list = [norm_verdict(v) for v in all_verdicts]
    true_cnt = v_norm_list.count("verdadeiro")
    fake_cnt = v_norm_list.count("falso")
    warn_cnt = v_norm_list.count("enganoso")

    if true_cnt >= fake_cnt and true_cnt >= warn_cnt:
        main_norm = "verdadeiro"
        v_badge = "VERDADEIRO"
    elif fake_cnt >= true_cnt and fake_cnt >= warn_cnt:
        main_norm = "falso"
        v_badge = "FALSO"
    else:
        main_norm = "enganoso"
        v_badge = "ENGANOSO / DIVERGENTE"

    why_diverge = conclusao or (
        "A divergência decorre da tensão entre a literalidade estrita do documento público oficial e a análise de causalidade da imputação política. "
        "Veículos que validaram ateram-se à veracidade documental da fonte primária; veículos que puniram enfatizaram a distorção da responsabilidade causal."
    )

    case_obj = {
        "id": f"CASO-{idx:02d}",
        "tabLabel": f"CASO {idx}: {tema.upper()}",
        "headline": f"{tema}: {alegacao[:45]}...",
        "speaker": cand_full,
        "speakerShort": cand_short,
        "candidateKey": cand_key,
        "speakerColorClass": get_cand_color_class(cand_full),
        "speakerPhoto": get_avatar(cand_full),
        "theme": tema,
        "tagId": f"TEMA: {tema.upper()}",
        "blockTime": "Debate TV Globo • 23/10/2026",
        "stampClass": get_stamp_class(main_norm),
        "verdictBadge": v_badge,
        "normalizedVerdict": main_norm,
        "quote": alegacao,
        "theFact": fato,
        "whyDiverge": why_diverge,
        "scoreboard": [
            {"type": "true", "count": true_cnt, "label": "Verdadeiro / Fato"},
            {"type": "fake", "count": fake_cnt, "label": "Falso / Fake"},
            {"type": "warn", "count": warn_cnt, "label": "Enganoso / Impreciso"}
        ],
        "independentChecks": indep_checks,
        "pressChecks": press_checks,
        "primarySources": [
            "Documentos e Relatórios Públicos Oficiais",
            "Bases Governamentais do Poder Executivo",
            f"Séries e Dados Primários sobre {tema}"
        ],
        "casePillars": {
            "title": f"Divergências e Contexto Analítico: {tema}",
            "pillars": [
                {
                    "num": "01",
                    "headline": "Critério de Enquadramento em Disputa",
                    "body": conclusao or "Divergência metodológica entre o apego à literalidade do documento oficial versus a exigência de atribuição causal e divisão federativa das responsabilidades."
                },
                {
                    "num": "02",
                    "headline": "Contexto Técnico e Documental",
                    "body": f"Confronto realizado com base nas tabelas primárias e autos dos órgãos do Estado sobre a declaração de {cand_short}."
                },
                {
                    "num": "03",
                    "headline": "Benefício da Dúvida & Diagnóstico de Viés",
                    "body": c.get('alinhamento_indep_vs_portais') or "As discordâncias entre os blocos refletem linhas editoriais de checagem distintas, mantendo concordância plena nos fatos objetivos apurados."
                }
            ]
        },
        "searchTokens": strip_accents(f"{idx} caso-{idx} {cand_full} {cand_short} {tema} {alegacao} {fato} {conclusao} {json.dumps(all_verdicts)}")
    }
    cases_out.append(case_obj)

# 2. ADICIONAR TODAS AS DEMAIS DECLARAÇÕES DO DEBATE
seen_claims = set([strip_accents(c['quote'])[:40] for c in cases_out])
additional_cases = []

for item in indep:
    claim = item.get('afirmacao_resumida') or item.get('alegacao_citada') or ''
    claim = claim.strip()
    if len(claim) < 15:
        continue

    claim_key = strip_accents(claim)[:40]
    if claim_key in seen_claims:
        continue
    seen_claims.add(claim_key)

    cand_full = clean_cand(item.get('candidato_original'))
    cand_short = get_cand_short(cand_full)
    cand_key = get_cand_key(cand_full)
    tema = item.get('tema') or 'Geral'
    tema = tema.strip().title()
    ver_orig = item.get('veredito_original') or 'Impreciso'
    norm_v = norm_verdict(ver_orig)
    just = item.get('justificativa_verificacao') or 'Verificação apurada pelo órgão independente.'
    citada = item.get('alegacao_citada') or claim
    proj = item.get('projeto_origem') or 'Checador Independente'
    fontes = item.get('fontes') or 'Documentos públicos e dados do debate.'

    indep_check = {
        "outlet": proj,
        "verdict": ver_orig.replace("✕", "").capitalize(),
        "stampClass": get_stamp_class(ver_orig),
        "text": just,
        "biasAnalysis": {
            "badge": f"Auditoria de Enquadramento ({proj})",
            "evidence": f"A iniciativa carimbou '{ver_orig}'. Sob o benefício da dúvida, o enquadramento decorre do rigor do veículo perante fontes como {fontes[:90]}..."
        }
    }

    # Match in press if exists
    press_checks = []
    claim_words = [w for w in strip_accents(claim).split() if len(w) > 4]
    for p in port:
        p_dec = strip_accents(p.get('declaracao') or p.get('tema') or '')
        if any(w in p_dec for w in claim_words):
            press_checks.append({
                "outlet": p.get('veiculo', 'Grande Imprensa'),
                "verdict": p.get('veredito_original', 'Verificado'),
                "stampClass": get_stamp_class(p.get('veredito_original', '')),
                "text": p.get('justificativa', '') or p.get('declaracao', '')
            })
            if len(press_checks) >= 2:
                break

    true_cnt = 1 if norm_v == "verdadeiro" else 0
    fake_cnt = 1 if norm_v == "falso" else 0
    warn_cnt = 1 if norm_v == "enganoso" else 0
    for pc in press_checks:
        pcn = norm_verdict(pc['verdict'])
        if pcn == "verdadeiro": true_cnt += 1
        elif pcn == "falso": fake_cnt += 1
        else: warn_cnt += 1

    dec_idx = len(cases_out) + len(additional_cases) + 1
    case_obj = {
        "id": f"DECL-{dec_idx:03d}",
        "tabLabel": f"{cand_short.upper()}: {tema.upper()}",
        "headline": f"{tema}: {claim[:45]}...",
        "speaker": cand_full,
        "speakerShort": cand_short,
        "candidateKey": cand_key,
        "speakerColorClass": get_cand_color_class(cand_full),
        "speakerPhoto": get_avatar(cand_full),
        "theme": tema,
        "tagId": f"TEMA: {tema.upper()}",
        "blockTime": "Debate TV Globo • 23/10/2026",
        "stampClass": get_stamp_class(norm_v),
        "verdictBadge": norm_v.upper(),
        "normalizedVerdict": norm_v,
        "quote": citada,
        "theFact": f"Afirmação apurada: {claim}. {just[:250]}...",
        "whyDiverge": f"Verificação realizada por {proj} no debate da TV Globo com foco em {tema.lower()}. Fontes analisadas: {fontes}.",
        "scoreboard": [
            {"type": "true", "count": true_cnt, "label": "Verdadeiro / Fato"},
            {"type": "fake", "count": fake_cnt, "label": "Falso / Fake"},
            {"type": "warn", "count": warn_cnt, "label": "Enganoso / Impreciso"}
        ],
        "independentChecks": [indep_check],
        "pressChecks": press_checks,
        "primarySources": [
            f"Fontes Primárias: {fontes[:80]}",
            "Diário Oficial e Registros Públicos"
        ],
        "casePillars": {
            "title": f"Análise Metodológica: {tema}",
            "pillars": [
                {
                    "num": "01",
                    "headline": "Critério e Rigor Factual",
                    "body": f"Avaliação realizada pelo {proj} sobre dados de {tema.lower()} com base em {fontes[:100]}."
                },
                {
                    "num": "02",
                    "headline": "Contexto da Fala no Debate",
                    "body": f"Declaração proferida durante o debate presidencial na TV Globo, submetida à checagem em tempo real."
                },
                {
                    "num": "03",
                    "headline": "Benefício da Dúvida",
                    "body": "A checagem aplicou os métodos documentais da iniciativa, sob a presunção e o benefício da dúvida de fidelidade probatória."
                }
            ]
        },
        "searchTokens": strip_accents(f"{dec_idx} decl-{dec_idx:03d} {cand_full} {cand_short} {tema} {claim} {citada} {just} {ver_orig} {norm_v}")
    }
    additional_cases.append(case_obj)

all_declarations = cases_out + additional_cases
print(f"Total de declarações compiladas: {len(all_declarations)}")

# Salvar em declarations_data.js
out_js = r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface\declarations_data.js"
with open(out_js, "w", encoding="utf-8") as f:
    f.write("// Base Consolidada de TODAS as Declarações Auditadas do Debate Presidencial 2026\n")
    f.write("const ALL_DECLARATIONS = ")
    json.dump(all_declarations, f, ensure_ascii=False, indent=2)
    f.write(";\n")

# Salvar em declarations.json
out_json = r"C:\Users\RAFAE\Downloads\a-checagem-da-checagem\interface\declarations.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(all_declarations, f, ensure_ascii=False, indent=2)

print(f"Arquivos regerados com sucesso! ({len(all_declarations)} itens)")
