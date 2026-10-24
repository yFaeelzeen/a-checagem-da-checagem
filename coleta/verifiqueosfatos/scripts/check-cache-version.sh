#!/usr/bin/env bash
# Fails when a file cached by sw.js changed but CACHE_NAME was not bumped.
# Usage: scripts/check-cache-version.sh <base-ref>   (e.g. origin/main)
set -euo pipefail

BASE="${1:?usage: $0 <base-ref>}"

# Prints the entries of ASSETS_TO_CACHE found in the given sw.js content (stdin),
# as repo paths ('./' becomes index.html).
cached_files() {
  sed -n '/ASSETS_TO_CACHE *= *\[/,/\]/p' | grep -o "'[^']*'" | tr -d "'" \
    | sed -e 's#^\./$#index.html#' -e 's#^\./##' | sort -u
}

cache_name() {
  grep -o "CACHE_NAME *= *'[^']*'" | head -1
}

head_list=$(cached_files < sw.js)
base_list=$(git show "$BASE:sw.js" | cached_files)
# Compare the merge-base with the working tree, so uncommitted edits are also checked locally
# (in CI the working tree equals HEAD). Untracked files are included too.
changed=$( { git diff --name-only "$(git merge-base "$BASE" HEAD)"; git ls-files --others --exclude-standard; } )

# Cached files that changed in this branch (including files added to or removed from the list)
touched=$( { echo "$changed" | grep -Fxf <(echo "$head_list"; echo "$base_list") || true; } )
list_diff=$(diff <(echo "$base_list") <(echo "$head_list") || true)

if [ -z "$touched" ] && [ -z "$list_diff" ]; then
  echo "OK: nenhum arquivo cacheado mudou, o CACHE_NAME não precisa ser alterado."
  exit 0
fi

head_name=$(cache_name < sw.js)
base_name=$(git show "$BASE:sw.js" | cache_name)

if [ "$head_name" = "$base_name" ]; then
  echo "::error file=sw.js::O CACHE_NAME não foi alterado, mas arquivos cacheados mudaram."
  echo "Arquivos cacheados alterados:"
  echo "$touched" | sed 's/^/  - /'
  [ -n "$list_diff" ] && echo "A lista ASSETS_TO_CACHE também mudou."
  echo "Atual: $head_name"
  current=$(echo "$head_name" | grep -o "'[^']*'" | tr -d "'")
  if [[ "$current" =~ ^(.*[^0-9])([0-9]+)$ ]]; then
    suggestion="${BASH_REMATCH[1]}$((BASH_REMATCH[2] + 1))"
  else
    suggestion="${current}-2"
  fi
  echo "Altere o CACHE_NAME no sw.js (ex.: $current -> $suggestion) para que quem já instalou o app receba os arquivos novos."
  exit 1
fi

echo "OK: arquivos cacheados mudaram e o CACHE_NAME foi alterado ($base_name -> $head_name)."
