import os, sys, urllib.request, ssl, time, hashlib, json
sys.stdout.reconfigure(encoding='utf-8')

urls = {
    'uol_confere': 'https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm',
    'g1_fato_ou_fake': 'https://g1.globo.com/google/amp/fato-ou-fake/eleicoes/noticia/2026/10/23/veja-o-que-e-fato-ou-fake-nas-falas-de-flavio-bolsonaro-e-lula-no-debate-da-globo-no-2o-turno-das-eleicoes-2026.ghtml',
    'estadao_verifica': 'https://www.estadao.com.br/amp/estadao-verifica/debate-tv-globo-checagem-tempo-real-ao-vivo/',
    'agencia_lupa': 'https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/'
}

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

results = {}

for name, u in urls.items():
    t_start = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    print(f'Probing {name}: {u}')
    req = urllib.request.Request(u, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            content = resp.read()
            status = resp.status
            final_url = resp.geturl()
            sz = len(content)
            sha = hashlib.sha256(content).hexdigest()
            out_file = os.path.join(raw_dir, f'{name}.html')
            with open(out_file, 'wb') as f:
                f.write(content)
            results[name] = {
                'url': u, 'status': status, 'final_url': final_url,
                'size': sz, 'sha256': sha, 'saved_file': out_file,
                'error': None, 'time': t_start
            }
            print(f'  -> [OK {status}] Size: {sz} bytes, SHA: {sha[:16]}...')
    except urllib.error.HTTPError as e:
        results[name] = {
            'url': u, 'status': e.code, 'final_url': getattr(e, 'url', u),
            'size': 0, 'sha256': None, 'saved_file': None,
            'error': str(e), 'time': t_start
        }
        print(f'  -> [HTTP {e.code}] {e}')
    except Exception as e:
        results[name] = {
            'url': u, 'status': 'ERROR', 'final_url': u,
            'size': 0, 'sha256': None, 'saved_file': None,
            'error': str(e), 'time': t_start
        }
        print(f'  -> [ERR] {e}')

with open(os.path.join(raw_dir, 'probe_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
