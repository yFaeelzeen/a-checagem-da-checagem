import os, sys, hashlib, json, time
sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources'

sources = {
    'uol_confere': {
        'name': 'UOL Confere',
        'url': 'https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm',
        'file': 'uol_confere.html',
        'retrieval_method': 'HTTP GET direto com cabeçalho de navegador móvel compatível (iOS Safari)',
        'status_code': 200
    },
    'g1_fato_ou_fake': {
        'name': 'G1 — Fato ou Fake',
        'url': 'https://g1.globo.com/google/amp/fato-ou-fake/eleicoes/noticia/2026/10/23/veja-o-que-e-fato-ou-fake-nas-falas-de-flavio-bolsonaro-e-lula-no-debate-da-globo-no-2o-turno-das-eleicoes-2026.ghtml',
        'file': 'g1_fato_ou_fake.html',
        'retrieval_method': 'HTTP GET direto (versão AMP padrão)',
        'status_code': 200
    },
    'estadao_verifica': {
        'name': 'Estadão Verifica',
        'url': 'https://www.estadao.com.br/amp/estadao-verifica/debate-tv-globo-checagem-tempo-real-ao-vivo/',
        'file': 'estadao_verifica.html',
        'retrieval_method': 'HTTP GET direto (versão AMP padrão)',
        'status_code': 200
    },
    'agencia_lupa': {
        'name': 'Agência Lupa',
        'url': 'https://www.agencialupa.org/checagem/2026/10/23/ao-vivo-checagem-do-ultimo-debate-entre-lula-e-flavio-bolsonaro-no-segundo-turno/',
        'file': 'agencia_lupa.html',
        'retrieval_method': 'HTTP GET direto (WordPress / tema Lupa)',
        'status_code': 200
    }
}

manifest = {}
for k, v in sources.items():
    fp = os.path.join(raw_dir, v['file'])
    sz = os.path.getsize(fp)
    with open(fp, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    manifest[k] = {
        'veiculo': v['name'],
        'url_autorizada': v['url'],
        'arquivo_local': os.path.relpath(fp, r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'),
        'tamanho_bytes': sz,
        'sha256': sha,
        'status_acesso': v['status_code'],
        'metodo_recuperacao': v['retrieval_method'],
        'timestamp_coleta': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    }
    print(f"[{v['name']}] Size: {sz} bytes | SHA256: {sha[:16]}... | Status: {v['status_code']}")

with open(os.path.join(raw_dir, 'manifesto_fontes_autorizadas.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
