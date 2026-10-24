import os, sys, hashlib

base_dir = r'C:\Users\RAFAE\Downloads\dossie_confronto_independentes_vs_portais_20261024'

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

sha_lines = []
for root, dirs, files in os.walk(base_dir):
    for fn in sorted(files):
        if fn == 'SHA256_CONFRONTO_ARTEFATOS.txt':
            continue
        full_p = os.path.join(root, fn)
        rel_p = os.path.relpath(full_p, base_dir)
        sha_lines.append(f"{hash_file(full_p)}  {rel_p}")

out_sha_file = os.path.join(base_dir, 'SHA256_CONFRONTO_ARTEFATOS.txt')
with open(out_sha_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines))

print(f"Hashes salvos em {out_sha_file}: {len(sha_lines)} arquivos.")
