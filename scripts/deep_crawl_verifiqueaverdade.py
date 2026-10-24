import os
import sys
import ssl
import json
import re
import urllib.request
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = 'https://verifiqueaverdade.com.br'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch(url):
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

# Let's inspect /debates/band-2026-10-18/ and /metodologia/
urls_to_inspect = [
    'https://verifiqueaverdade.com.br/',
    'https://verifiqueaverdade.com.br/debates/globo-2026-10-23/',
    'https://verifiqueaverdade.com.br/debates/band-2026-10-18/',
    'https://verifiqueaverdade.com.br/metodologia/'
]

all_discovered = set(urls_to_inspect)
visited_pages = set()
page_links = {}

for u in urls_to_inspect:
    st, hd, data = fetch(u)
    print(f"Inspecting {u} -> Status {st}, {len(data):,} bytes")
    if st == 200 and data:
        html = data.decode('utf-8', errors='ignore')
        # find all hrefs and srcs
        hrefs = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
        srcs = re.findall(r'src=[\'"]([^\'"]+)[\'"]', html)
        
        found = set()
        for ref in hrefs + srcs:
            if ref.startswith('#') or ref.startswith('mailto:') or ref.startswith('tel:'):
                continue
            full = urljoin(u, ref)
            p = urlparse(full)
            if p.netloc == 'verifiqueaverdade.com.br' or not p.netloc:
                clean_url = f"{p.scheme}://verifiqueaverdade.com.br{p.path}"
                if p.query:
                    clean_url += f"?{p.query}"
                found.add(clean_url)
                all_discovered.add(clean_url)
        page_links[u] = found

print("\n--- Summary of Internal Pages & Routes ---")
pages = [u for u in all_discovered if not any(u.endswith(ext) for ext in ['.js', '.css', '.svg', '.png', '.jpg', '.ico', '.json'])]
for p in sorted(set(pages)):
    print("Page:", p)

print(f"\nTotal Discovered Assets on verifiqueaverdade.com.br: {len(all_discovered)}")
