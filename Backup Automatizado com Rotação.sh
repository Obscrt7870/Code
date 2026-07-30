#!/usr/bin/env bash
set -euo pipefail
 
# Configurações
SOURCE_DIR="${1:-/var/log}"
BACKUP_DIR="${2:-/tmp/backups}"
RETENTION_DAYS=7
TIMESTAMP=$(date +'%Y%m%m_%H%M%S')
ARCHIVE_NAME="backup_${TIMESTAMP}.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "[i] Criando arquivo comprimido de ${SOURCE_DIR}..."
tar -czf "${BACKUP_DIR}/${ARCHIVE_NAME}" -C "$SOURCE_DIR" .

echo "[+] Backup salvo em: ${BACKUP_DIR}/${ARCHIVE_NAME}"

# Limpeza de backups antigos
echo "[i] Removendo backups com mais de ${RETENTION_DAYS} dias..."
find "$BACKUP_DIR" -type f -name "backup_*.tar.gz" -mtime +"$RETENTION_DAYS" -delete

echo "[v] Processo concluído com sucesso!"
