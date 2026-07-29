#!/usr/bin/env bash
set -euo pipefail

DOMAIN="${1:-example.com}"
echo "[*] Buscando subdomínios para: ${DOMAIN} via crt.sh..."

curl -s "https://crt.sh/?q=%25.${DOMAIN}&output=json" | \
jq -r '.[].name_value' 2>/dev/null | \
sed 's/\*\.//g' | \
sort -u