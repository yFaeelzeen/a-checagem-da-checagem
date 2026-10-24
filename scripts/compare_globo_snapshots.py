import os
import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

old_file = r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\01_coleta_preservacao_bruta\verifiqueaverdade_com_br\debates\globo-2026-10-23.html'
with open(old_file, 'r', encoding='utf-8', errors='ignore') as f:
    old_html = f.read()

soup_old = BeautifulSoup(old_html, 'html.parser')
cards_old = soup_old.find_all(id=re.compile(r'^b\d+-\d+$'))
old_ids = [c.get('id') for c in cards_old]
print(f"Cards in old local file: {len(old_ids)}")

import urllib.request, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://verifiqueaverdade.com.br/debates/globo-2026-10-23/', headers=headers)
live_html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')
soup_live = BeautifulSoup(live_html, 'html.parser')
cards_live = soup_live.find_all(id=re.compile(r'^b\d+-\d+$'))
live_ids = [c.get('id') for c in cards_live]
print(f"Cards in live site: {len(live_ids)}")

diff = set(live_ids) - set(old_ids)
print(f"New card IDs in live site ({len(diff)}):", sorted(diff))
