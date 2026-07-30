# 🛡️ Cybersecurity & Dev Toolkit

Uma coleção prática e modular de scripts em **Python** e **Bash** voltados para **Segurança da Informação, Redes, Forense Computacional, Automação Defensiva (Blue Team) e Administração de Sistemas**.

Projetado para auditores de segurança, profissionais de TI e entusiastas que buscam ferramentas leves, sem dependências desnecessárias e prontas para uso em linha de comando (CLI).

---

## 🛠️ Requisitos e Pré-requisitos
* Python: 3.9+
* Bash: Shell Unix/Linux padrão
* PHP: 7.4+

### Instalação de Dependências Python
```
pip install cryptography aiohttp scapy bcrypt Pillow dnspython
```


## 🚀 Como Executar os Scripts

### 🌐 Reconhecimento & OSINT

* Validador de Registros SPF:DMARC.py
```
python "Validador de Registros SPF:DMARC.py"
```
* Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py
```
python "Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py"
```
* Extrator de Subdomínios via Certificate Transparency Logs.sh
```
chmod +x "Extrator de Subdomínios via Certificate Transparency Logs.sh"
./"Extrator de Subdomínios via Certificate Transparency Logs.sh" exemplo.com
```
* Verificador de Expiração de Certificado SSL:TLS
```
python "Verificador de Expiração de Certificado SSL:TLS"
```
* Extrator de Cabeçalhos de Segurança HTTP.py
```
python "Extrator de Cabeçalhos de Segurança HTTP.py"
```
### 🔍 Forense & Análise
* Calculador de Hashes Criptográficos para Triagem Forense.py
```
python "Calculador de Hashes Criptográficos para Triagem Forense.py" arquivo.ext
```
* Extrator de Strings LSB em Imagens.py
```
python "Extrator de Strings LSB em Imagens.py"
```
* Extrator de Metadados de Imagens.py
```
python "Extrator de Metadados de Imagens.py"
```
* Buscador de Assinaturas de Arquivos.sh
```
chmod +x "Buscador de Assinaturas de Arquivos.sh"
./"Buscador de Assinaturas de Arquivos.sh" arquivo
```
* Parser Básico de Log Nginx:Apache para Identificar Ataques SQLi.py
```
python "Parser Básico de Log Nginx:Apache para Identificar Ataques SQLi.py"
```
## 🛰️ Redes & Auditoria
* Port Scanner Assincrono.py
```
python "Port Scanner Assincrono.py"
```
* Sniffer Básico de Pacotes RAW.py
```
sudo python "Sniffer Básico de Pacotes RAW.py"
```
* Parser de Arquivo PCAP.py
```
python "Parser de Arquivo PCAP.py"
```
* Monitor de Dispositivos Ativos em Rede Local.py
```
python "Monitor de Dispositivos Ativos em Rede Local.py"
```
* Monitor de Conexões de Rede em Tempo Real.sh
```
chmod +x "Monitor de Conexões de Rede em Tempo Real.sh"
./"Monitor de Conexões de Rede em Tempo Real.sh"
```
## 🔐 Criptografia & Autenticação
* Ferramenta de criptografia simétrica de arquivos.py
```
python "Ferramenta de criptografia simétrica de arquivos.py" encrypt arquivo.xlsx arquivo.novacrypt "SuaSenha"
python "Ferramenta de criptografia simétrica de arquivos.py" decrypt arquivo.novacrypt restaurado.xlsx "SuaSenha"
```
* Criptografia de Arquivos AES-GCM.py
```
python "Criptografia de Arquivos AES-GCM.py"
```
* Gerador e Verificador de Hash BCRYPT.py
```
python "Gerador e Verificador de Hash BCRYPT.py"
```
* Validador de Estrutura e Assinatura JWT.py
```
python "Validador de Estrutura e Assinatura JWT.py"
```
## 🛡️ Defesa, SysAdmin & Automação (Blue Team)
* Monitor de Integridade de Arquivos.py
```
python "Monitor de Integridade de Arquivos.py"
```
* Script Hardening Inicial de Servidor Linux.sh
```
chmod +x "Script Hardening Inicial de Servidor Linux.sh"
sudo ./"Script Hardening Inicial de Servidor Linux.sh"
```
* Sanitizador de Entradas HTML contra XSS.py
```
python "Sanitizador de Entradas HTML contra XSS.py"
```
* Bloqueador Automático de IPs via Log de Falhas SSH.sh
```
chmod +x "Bloqueador Automático de IPs via Log de Falhas SSH.sh"
sudo ./"Bloqueador Automático de IPs via Log de Falhas SSH.sh"
```
* Backup Automatizado com Rotação.sh
```
chmod +x "Backup Automatizado com Rotação.sh"
./"Backup Automatizado com Rotação.sh" /var/log /tmp/backups
```
* Sanitizador e Formatador de Logs JSON.php
```
php "Sanitizador e Formatador de Logs JSON.php"
```

## 🗂️ Estrutura do Repositório

```text
.
├── 🌐 Reconhecimento & OSINT
│   ├── check_spf_dmarc.py       # Validador de registros SPF/DMARC contra e-mail spoofing
│   ├── dir_fuzzer.py            # Fuzzer assíncrono de diretórios web (aiohttp)
│   ├── crt_subdomains.sh        # Coletor de subdomínios via Certificate Transparency (crt.sh)
│   ├── check_ssl_expiry.py      # Verificador de expiração de certificados SSL/TLS
│   └── check_security_hdrs.py   # Analisador de cabeçalhos HTTP de segurança (HSTS, CSP, etc.)
│
├── 🔍 Forense & Análise
│   ├── calc_hashes.py           # Calculador simultâneo de hashes (MD5, SHA1, SHA256)
│   ├── lsb_stego.py             # Extrator de mensagens ocultas LSB em imagens PNG
│   ├── magic_bytes.sh           # Identificador de formato real via assinaturas hex (Magic Bytes)
│   └── sqli_log_parser.py       # Parser de logs Nginx/Apache para detecção de SQL Injection
│
├── 🛰️ Redes & Auditoria
│   ├── async_port_scanner.py    # Scanner de portas TCP ultra-rápido via asyncio
│   ├── raw_packet_sniffer.py    # Sniffer leve de pacotes RAW IP/TCP
│   ├── pcap_analyzer.py         # Parser e resumidor de capturas PCAP (Scapy)
│   ├── async_ping_sweep.py      # Monitor de hosts ativos na rede local via ICMP
│   └── active_conns.sh          # Monitor de conexões ativas e processos em tempo real
│
├── 🔐 Criptografia & Autenticação
│   ├── file_encryptor.py        # Criptografia simétrica de arquivos com PBKDF2 + AES-GCM (Fernet)
│   ├── bcrypt_manager.py        # Gerador e validador de hashes de senhas com bcrypt
│   ├── aes_gcm_crypto.py        # Criptografia de dados AES-256-GCM com validação de tag
│   └── jwt_inspector.py         # Inspector/Decoder de tokens JWT sem validação de chave
│
└── 🛡️ Defesa & Automação (Blue Team)
    ├── file_integrity_fim.py    # FIM (File Integrity Monitor) baseado em hashes SHA256
    ├── linux_hardening.sh       # Script de endurecimento e configuração inicial de servidores Linux
    ├── xss_sanitizer.py         # Sanitizador de entradas string/HTML contra XSS
    ├── ssh_bruteforce_block.sh  # Script de mitigação automatizada contra força bruta SSH
    ├── backup_rotator.sh        # Automação de backups com compressão e retenção configurável
    └── json_logger.php          # Logger PHP estruturado em JSON para auditorias de sistema
