import urllib.request, ssl, hashlib

url = 'https://noticias.uol.com.br/confere/ultimas-noticias/2026/10/24/debate-globo-checagem-flavio-lula.ghtm'
headers_variants = [
    {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    },
    {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Referer': 'https://www.google.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

success = False
for idx, h in enumerate(headers_variants):
    print(f'Trying variant {idx+1}...')
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            body = r.read()
            print(f'  Variant {idx+1} SUCCEEDED! Status: {r.status}, Size: {len(body)}')
            with open(r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024\raw_sources\uol_confere.html', 'wb') as f:
                f.write(body)
            success = True
            break
    except Exception as e:
        print(f'  Variant {idx+1} failed: {e}')

if not success:
    print('All simple HTTP requests for UOL failed with 403 Forbidden.')
