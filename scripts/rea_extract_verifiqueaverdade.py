import os
import sys
import ssl
import json
import re
import urllib.request
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = 'https://verifiqueaverdade.com.br'
OUTPUT_DIR = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\01_coleta_preservacao_bruta\verifiqueaverdade_com_br'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            data = resp.read()
            return resp.status, dict(resp.headers), data
    except urllib.error.HTTPError as e:
        data = e.read() if e.fp else None
        return e.code, dict(e.headers), data
    except Exception as e:
        return 0, {}, str(e).encode('utf-8')

def main():
    print("=== REA / PASSIVE EXTRACTION: verifiqueaverdade.com.br ===")
    
    # 1. Probing standard web endpoints
    probes = [
        '/',
        '/robots.txt',
        '/sitemap.xml',
        '/sitemap_index.xml',
        '/favicon.ico',
        '/manifest.json',
        '/debates',
        '/debates/',
        '/debates/globo-2026-10-23',
        '/api',
        '/api/health',
        '/api/debates',
        '/api/checks',
        '/_next/data'
    ]
    
    discovered_urls = set()
    inventory = []
    
    for p in probes:
        u = urljoin(BASE_URL, p)
        st, hd, data = fetch_url(u)
        dlen = len(data) if data else 0
        ct = hd.get('Content-Type', '')
        print(f"Probe: {u} -> Status {st}, Size: {dlen:,} bytes, Content-Type: {ct}")
        if st == 200 and data:
            discovered_urls.add(u)
            if 'text' in ct or 'json' in ct or 'xml' in ct:
                txt = data.decode('utf-8', errors='ignore')
                if len(txt) < 1500 and not 'html' in ct:
                    print(f"   [Preview]:\n{txt.strip()}\n")
                    
    # Let's inspect root / HTML thoroughly
    print("\n--- Inspecting Root Page / ---")
    st, hd, root_data = fetch_url(BASE_URL + '/')
    if root_data:
        root_txt = root_data.decode('utf-8', errors='ignore')
        # Extract all href and src
        hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', root_txt)
        srcs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', root_txt)
        
        print(f"Root HREFs found: {len(hrefs)}")
        for h in sorted(set(hrefs)):
            print(f"  href: {h}")
            discovered_urls.add(urljoin(BASE_URL, h))
            
        print(f"Root SRCs found: {len(srcs)}")
        for s in sorted(set(srcs)):
            print(f"  src: {s}")
            discovered_urls.add(urljoin(BASE_URL, s))
            
        # Check Next.js build manifest or script chunks
        chunk_matches = re.findall(r'/_next/static/[a-zA-Z0-9_\-\./]+', root_txt)
        for c in set(chunk_matches):
            discovered_urls.add(urljoin(BASE_URL, c))
            
    # Also inspect /debates/globo-2026-10-23 HTML thoroughly
    print("\n--- Inspecting /debates/globo-2026-10-23 ---")
    st, hd, debate_data = fetch_url(BASE_URL + '/debates/globo-2026-10-23')
    if debate_data:
        deb_txt = debate_data.decode('utf-8', errors='ignore')
        hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', deb_txt)
        srcs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', deb_txt)
        chunk_matches = re.findall(r'/_next/static/[a-zA-Z0-9_\-\./]+', deb_txt)
        for h in set(hrefs):
            if not h.startswith('http') or 'verifiqueaverdade.com.br' in h:
                discovered_urls.add(urljoin(BASE_URL, h))
        for s in set(srcs):
            if not s.startswith('http') or 'verifiqueaverdade.com.br' in s:
                discovered_urls.add(urljoin(BASE_URL, s))
        for c in set(chunk_matches):
            discovered_urls.add(urljoin(BASE_URL, c))

    print(f"\nTotal Discovered Unique URLs on verifiqueaverdade.com.br: {len(discovered_urls)}")
    for u in sorted(discovered_urls):
        print(f"  * {u}")

if __name__ == '__main__':
    main()
