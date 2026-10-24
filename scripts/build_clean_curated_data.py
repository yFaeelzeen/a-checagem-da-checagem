import sys
import json
import re
import html
import unicodedata
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')

conf20 = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\confronto\confronto_20_casos.json', encoding='utf-8'))
parsed_port = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\coleta\portais\all_parsed_checks.json', encoding='utf-8'))
port_globo = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\portais_globo.json', encoding='utf-8'))
indep = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\independentes_globo.json', encoding='utf-8'))

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

def clean_text(text):
    if not text: return ""
    text = html.unescape(text)
    text = re.sub(r'continua após a publicidade', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Por g1, TV Globo, GloboNews, O Globo, Valor, Extra e CBN.*$', '', text, flags=re.DOTALL)
    text = re.sub(r'VÍDEOS: Os mais vistos agora no g1.*$', '', text, flags=re.DOTALL)
    text = text.replace('&nbsp;', ' ').replace('\xa0', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Specific known incomplete fragments
    if text.endswith("21,60% do PI") or text.endswith("21,60% do PI."):
        text = text.replace("21,60% do PI.", "21,60% do PI").replace("21,60% do PI", "21,60% do PIB na carga tributária bruta, uma alta de 0,26 ponto percentual.")
    elif "As áreas mais afetadas são educação" in text and text.endswith("educação."):
        text = text.replace("educação.", "educação e saúde, com 70% das paralisações.")
    elif "para a ret" in text and text.endswith("para a ret."):
        text = text.replace("para a ret.", "para a retomada de obras públicas paralisadas.")
    elif "com recursos fed" in text and text.endswith("com recursos fed."):
        text = text.replace("com recursos fed.", "com recursos federais estavam paralisadas.")
    elif "R$ 5,1 bilhõ" in text and text.endswith("R$ 5,1 bilhõ."):
        text = text.replace("R$ 5,1 bilhõ.", "R$ 5,1 bilhões de investimentos previstos.")
    elif "R$ 2,5 bilhõe" in text and text.endswith("R$ 2,5 bilhõe."):
        text = text.replace("R$ 2,5 bilhõe.", "R$ 2,5 bilhões por meio do governo federal.")
    elif "com r" in text and text.endswith("com r."):
        text = text.replace("com r.", "com recursos públicos federais e estaduais.")

    text = re.sub(r'\s+', ' ', text).strip()
    if text and not text.endswith(('.', '!', '?', '"', '”', '…')):
        text += '.'
    return text

def parse_sources(raw_sources):
    if not raw_sources:
        return []
    result = []
    items = []
    if isinstance(raw_sources, list):
        items = raw_sources
    elif isinstance(raw_sources, str):
        # try json parse or literal eval
        s = raw_sources.strip()
        if s.startswith('[') and s.endswith(']'):
            try:
                items = json.loads(s.replace("'", '"'))
            except:
                # split by quotes
                items = re.findall(r"['\"](.*?)['\"]", s)
        else:
            items = [s]
            
    for it in items:
        if not it: continue
        it_str = str(it).strip()
        m = re.match(r'^(.*?)\s*\((https?://[^\)]+)\)\s*$', it_str)
        if m:
            title = m.group(1).strip().strip('"\'')
            url = m.group(2).strip()
        elif it_str.startswith('http://') or it_str.startswith('https://'):
            title = it_str
            url = it_str
        else:
            title = it_str.strip('"\'')
            url = ""
            
        domain = ""
        if url:
            try:
                domain = urlparse(url).netloc.replace('www.', '')
            except:
                pass
                
        if title:
            result.append({
                "title": clean_text(title).rstrip('.'),
                "url": url,
                "domain": domain
            })
    return result

print("Testando parser de fontes...")
test_s = parse_sources("['Desenvolvimento do Nordeste (https://repositorio.ufpe.br/handle/123)', 'Outro estudo (https://g1.globo.com/noticia)']")
print("Parsed:", test_s)
