#!/usr/bin/env bash
set -euo pipefail

if [[ $EUID -ne 0 ]]; then
   echo "Este script deve ser executado como root." 
   exit 1
fi

echo "[*] Aplicando configurações de hardening..."

# 1. Atualizações do Sistema
apt update && apt upgrade -y

# 2. Desabilitar login SSH como root
sed -i 's/^PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl reload sshd || true

# 3. Habilitar Firewall UFW basico
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp # Mantenha a porta SSH aberta!
ufw --force enable

echo "[+] Hardening basico concluido!"