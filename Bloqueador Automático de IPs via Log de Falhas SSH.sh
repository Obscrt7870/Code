#!/usr/bin/env bash
set -euo pipefail
 
LOG_FILE="/var/log/auth.log"
THRESHOLD=5

if [[ ! -f "$LOG_FILE" ]]; then
    LOG_FILE="/var/log/secure" # RedHat/CentOS
fi

if [[ ! -f "$LOG_FILE" ]]; then
    echo "[-] Arquivo de log de autenticação não localizado."
    exit 1
fi

echo "[*] Identificando IPs com falhas repetidas no SSH..."

# Extrai IPs com mais de $THRESHOLD tentativas frustradas
grep "Failed password" "$LOG_FILE" | awk '{print $(NF-3)}' | sort | uniq -c | while read -r count ip; do
    if [[ "$count" -ge "$THRESHOLD" ]]; then
        echo "[!] Bloqueando IP suspeito ($count falhas): $ip"
        iptables -A INPUT -s "$ip" -j DROP 2>/dev/null || true
    fi
done
