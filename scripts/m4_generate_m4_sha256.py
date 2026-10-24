import os, sys, hashlib

out_dir = r'C:\Users\RAFAE\Downloads\dossie_auditoria_quatro_fontes_20261024'

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

sha_lines = []
for root, dirs, files in os.walk(out_dir):
    for fn in sorted(files):
        if fn == '09_SHA256_ARTEFATOS.txt':
            continue
        full_p = os.path.join(root, fn)
        rel_p = os.path.relpath(full_p, out_dir)
        sha_lines.append(f'{hash_file(full_p)}  {rel_p}')

out_sha_file = os.path.join(out_dir, '09_SHA256_ARTEFATOS.txt')
with open(out_sha_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines))

print(f'Wrote 09_SHA256_ARTEFATOS.txt with {len(sha_lines)} artifact hashes.')
