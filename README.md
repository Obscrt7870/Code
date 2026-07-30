# 🛡️ Cybersecurity & Dev Toolkit

Uma coleção prática e modular de scripts em **Python** e **Bash** voltados para **Segurança da Informação, Redes, Forense Computacional, Automação Defensiva (Blue Team) e Administração de Sistemas**.

Projetado para auditores de segurança, profissionais de TI e entusiastas que buscam ferramentas leves, sem dependências desnecessárias e prontas para uso em linha de comando (CLI).

---

## 🛠️ Requisitos e Pré-requisitos
* Python: 3.9+
* Bash: Shell Unix/Linux padrão
* PHP: 7.4+

### Instalação de Dependências Python

`pip install cryptography aiohttp scapy bcrypt Pillow dnspython`


## 🚀 Como Executar os Scripts

###🌐 Reconhecimento & OSINT

* Validador de Registros SPF:DMARC.py
`python "Validador de Registros SPF:DMARC.py"`

* Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py
`python "Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py"`

* Extrator de Subdomínios via Certificate Transparency Logs.sh
```
chmod +x "Extrator de Subdomínios via Certificate Transparency Logs.sh"
./"Extrator de Subdomínios via Certificate Transparency Logs.sh" exemplo.com
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
