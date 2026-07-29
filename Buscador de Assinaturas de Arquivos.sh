#!/usr/bin/env bash
set -euo pipefail

FILE="${1:-}"

if [[ -z "$FILE" || ! -f "$FILE" ]]; then
    echo "Uso: $0 <arquivo>"
    exit 1
fi

HEX_HEADER=$(head -c 8 "$FILE" | xxd -p | tr 'a-z' 'A-Z')

echo "Arquivo: $FILE"
echo "Header Hex (8 bytes): $HEX_HEADER"

case "$HEX_HEADER" in
    89504E470D0A1A0A*) echo "[+] Tipo detectado: Imagem PNG" ;;
    FFD8FF*)           echo "[+] Tipo detectado: Imagem JPEG" ;;
    25504446*)         echo "[+] Tipo detectado: Documento PDF" ;;
    504B0304*)         echo "[+] Tipo detectado: Arquivo ZIP / Office moderno (.docx, .xlsx)" ;;
    7F454C46*)         echo "[+] Tipo detectado: Executável Linux ELF" ;;
    4D5A*)             echo "[+] Tipo detectado: Executável Windows PE (EXE/DLL)" ;;
    *)                 echo "[-] Assinatura não mapeada no script." ;;
esac