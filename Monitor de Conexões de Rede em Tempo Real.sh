#!/usr/bin/env bash
# Monitora novas conexões ativas na máquina local
set -euo pipefail

echo "[*] Monitorando conexões estabelecidas (Pressione Ctrl+C para sair)..."
echo "------------------------------------------------------------------"

ss -tupn state established | awk 'NR>1 {print $4 " -> " $5 " | Processo: " $6}'