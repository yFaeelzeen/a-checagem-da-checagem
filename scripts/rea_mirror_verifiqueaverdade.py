import os
import sys
import ssl
import json
import re
import hashlib
import time
import urllib.request
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = 'https://verifiqueaverdade.com.br'
REPO_ROOT = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem'
DEST_DIR = os.path.join(REPO_ROOT, '01_coleta_preservacao_bruta', 'verifiqueaverdade_com_br')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = resp.read()
            elapsed = time.time() - t0
            return resp.status, dict(resp.headers), data, elapsed, None
    except urllib.error.HTTPError as e:
        data = e.read() if e.fp else None
        elapsed = time.time() - t0
        return e.code, dict(e.headers), data, elapsed, f"HTTPError {e.code}"
    except Exception as e:
        elapsed = time.time() - t0
        return 0, {}, None, elapsed, str(e)

def main():
    print("=== PASSIVE REA MIRROR: verifiqueaverdade.com.br ===")
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Backup earlier snapshot if needed
    old_globo = os.path.join(DEST_DIR, 'debates', 'globo-2026-10-23.html')
    old_globo_backup = os.path.join(DEST_DIR, 'debates', 'globo-2026-10-23_snapshot_inicial_132.html')
    if os.path.exists(old_globo) and not os.path.exists(old_globo_backup):
        with open(old_globo, 'rb') as src, open(old_globo_backup, 'wb') as dst:
            dst.write(src.read())
        print(f"Preservado snapshot original de 132 checagens em: {old_globo_backup}")

    # Core pages to fetch
    core_pages = [
        '/',
        '/metodologia/',
        '/debates/globo-2026-10-23/',
        '/debates/band-2026-10-18/'
    ]
    
    discovered_urls = set()
    for cp in core_pages:
        discovered_urls.add(urljoin(BASE_URL, cp))
        
    # Also discover all assets from core pages
    all_assets = set()
    for cp in core_pages:
        full_u = urljoin(BASE_URL, cp)
        st, hd, data, el, err = fetch(full_u)
        if st == 200 and data:
            html = data.decode('utf-8', errors='ignore')
            # Find refs
            refs = re.findall(r'(?:href|src)=[\'"]([^\'"]+)[\'"]', html)
            for r in refs:
                if r.startswith('#') or r.startswith('data:') or r.startswith('mailto:'):
                    continue
                u = urljoin(full_u, r)
                p = urlparse(u)
                if p.netloc == 'verifiqueaverdade.com.br':
                    discovered_urls.add(u)
                    
    print(f"Total discovered unique URLs on site: {len(discovered_urls)}")
    
    manifest_records = []
    
    for idx, u in enumerate(sorted(discovered_urls)):
        p = urlparse(u)
        path = p.path
        if path.endswith('/') or not path:
            local_rel = path.strip('/') + '/index.html' if path.strip('/') else 'index.html'
        else:
            local_rel = path.lstrip('/')
            
        local_path = os.path.join(DEST_DIR, local_rel.replace('/', os.sep))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        st, hd, data, elapsed, err = fetch(u)
        sz = len(data) if data else 0
        sha = hashlib.sha256(data).hexdigest() if data else ''
        now = datetime.now(timezone.utc).isoformat()
        
        if st == 200 and data:
            with open(local_path, 'wb') as f:
                f.write(data)
            status_desc = 'SALVO'
        else:
            status_desc = f'FALHA ({err})'
            
        manifest_records.append({
            'url': u,
            'path_relativo': local_rel.replace('\\', '/'),
            'status_http': st,
            'tamanho_bytes': sz,
            'sha256': sha,
            'content_type': hd.get('Content-Type', ''),
            'tempo_resposta_s': round(elapsed, 3),
            'timestamp_coleta': now,
            'erro': err or ''
        })
        
        if idx % 20 == 0 or idx == len(discovered_urls) - 1:
            print(f"[{idx+1}/{len(discovered_urls)}] {u} -> Status {st}, {sz:,} bytes ({status_desc})")
            
    # Save manifest
    manifest_json = os.path.join(DEST_DIR, 'inventario_extracao_completa.json')
    with open(manifest_json, 'w', encoding='utf-8') as f:
        json.dump(manifest_records, f, ensure_ascii=False, indent=2)
        
    print(f"\nManifesto salvo com {len(manifest_records)} recursos em: {manifest_json}")

if __name__ == '__main__':
    main()
