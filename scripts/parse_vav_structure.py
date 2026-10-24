import os
import sys
import ssl
import json
import re
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request('https://verifiqueaverdade.com.br/debates/globo-2026-10-23/', headers=headers)
globo_html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')

# Let's inspect how checks are marked up
# Look for article or div elements with id bX-Y
soup = BeautifulSoup(globo_html, 'html.parser')
cards = soup.find_all(id=re.compile(r'^b\d+-\d+$'))
print(f"Total cards matching id=bX-Y in Globo: {len(cards)}")

if cards:
    c = cards[0]
    print("Card 0 id:", c.get('id'))
    print("Card 0 text preview:", c.get_text(separator=' | ', strip=True)[:300])

cards_band = BeautifulSoup(urllib.request.urlopen(urllib.request.Request('https://verifiqueaverdade.com.br/debates/band-2026-10-18/', headers=headers), context=ctx).read().decode('utf-8', errors='ignore'), 'html.parser').find_all(id=re.compile(r'^b\d+-\d+$'))
print(f"Total cards matching id=bX-Y in Band: {len(cards_band)}")
if cards_band:
    print("Band Card 0 id:", cards_band[0].get('id'))
    print("Band Card 0 text preview:", cards_band[0].get_text(separator=' | ', strip=True)[:300])
