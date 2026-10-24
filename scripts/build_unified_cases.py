import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

conf20 = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\confronto\confronto_20_casos.json', encoding='utf-8'))
indep = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\independentes_globo.json', encoding='utf-8'))
port = json.load(open(r'C:\Users\RAFAE\Downloads\a-checagem-da-checagem\dados\portais_globo.json', encoding='utf-8'))

print(f"Conf20: {len(conf20)}")
print(f"Indep: {len(indep)}")
print(f"Port: {len(port)}")
