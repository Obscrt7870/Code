# 🛡️ Cybersecurity & Dev Toolkit

Uma coleção prática e modular de scripts em **Python**, **Bash** e **PHP** voltados para **Segurança da Informação, Redes, Forense Computacional, Automação Defensiva (Blue Team) e Administração de Sistemas**, utilizando exatamente os nomes dos arquivos do repositório.

---

## 🗂️ Estrutura de Arquivos

```text
.
├── Backup Automatizado com Rotação.sh
├── Bloqueador Automático de IPs via Log de Falhas SSH.sh
├── Buscador de Assinaturas de Arquivos.sh
├── Calculador de Hashes Criptográficos para Triagem Forense.py
├── Criptografia de Arquivos AES-GCM.py
├── Extrator de Cabeçalhos de Segurança HTTP.py
├── Extrator de Metadados de Imagens.py
├── Extrator de Strings LSB em Imagens.py
├── Extrator de Subdomínios via Certificate Transparency Logs.sh
├── Ferramenta de criptografia simétrica de arquivos.py
├── Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py
├── Gerador e Verificador de Hash BCRYPT.py
├── Monitor de Conexões de Rede em Tempo Real.sh
├── Monitor de Dispositivos Ativos em Rede Local.py
├── Monitor de Integridade de Arquivos.py
├── Parser Básico de Log Nginx:Apache para Identificar Ataques SQLi.py
├── Parser de Arquivo PCAP.py
├── Port Scanner Assincrono.py
├── README.md
├── Sanitizador de Entradas HTML contra XSS.py
├── Sanitizador e Formatador de Logs JSON.php
├── Script Hardening Inicial de Servidor Linux.sh
├── Sniffer Básico de Pacotes RAW.py
├── Validador de Estrutura e Assinatura JWT.py
├── Validador de Registros SPF:DMARC.py
└── Verificador de Expiração de Certificado SSL:TLS
```

---

## 🛠️ Requisitos e Pré-requisitos

* **Python:** 3.9+
* **Bash:** Shell Unix/Linux padrão
* **PHP:** 7.4+

### Instalação de Dependências Python
```bash
pip install cryptography aiohttp scapy bcrypt Pillow dnspython
```

---

## 🚀 Como Executar os Scripts

### 🌐 Reconhecimento & OSINT

* **Validador de Registros SPF:DMARC.py**
  ```bash
  python "Validador de Registros SPF:DMARC.py"
  ```
* **Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py**
  ```bash
  python "Fuzzer:Buster de Diretórios Web HTTP:HTTPS.py"
  ```
* **Extrator de Subdomínios via Certificate Transparency Logs.sh**
  ```bash
  chmod +x "Extrator de Subdomínios via Certificate Transparency Logs.sh"
  ./"Extrator de Subdomínios via Certificate Transparency Logs.sh" exemplo.com
  ```
* **Verificador de Expiração de Certificado SSL:TLS**
  ```bash
  python "Verificador de Expiração de Certificado SSL:TLS"
  ```
* **Extrator de Cabeçalhos de Segurança HTTP.py**
  ```bash
  python "Extrator de Cabeçalhos de Segurança HTTP.py"
  ```

---

### 🔍 Forense & Análise

* **Calculador de Hashes Criptográficos para Triagem Forense.py**
  ```bash
  python "Calculador de Hashes Criptográficos para Triagem Forense.py" arquivo.ext
  ```
* **Extrator de Strings LSB em Imagens.py**
  ```bash
  python "Extrator de Strings LSB em Imagens.py"
  ```
* **Extrator de Metadados de Imagens.py**
  ```bash
  python "Extrator de Metadados de Imagens.py"
  ```
* **Buscador de Assinaturas de Arquivos.sh**
  ```bash
  chmod +x "Buscador de Assinaturas de Arquivos.sh"
  ./"Buscador de Assinaturas de Arquivos.sh" arquivo
  ```
* **Parser Básico de Log Nginx:Apache para Identificar Ataques SQLi.py**
  ```bash
  python "Parser Básico de Log Nginx:Apache para Identificar Ataques SQLi.py"
  ```

---

### 🛰️ Redes & Auditoria

* **Port Scanner Assincrono.py**
  ```bash
  python "Port Scanner Assincrono.py"
  ```
* **Sniffer Básico de Pacotes RAW.py**
  ```bash
  sudo python "Sniffer Básico de Pacotes RAW.py"
  ```
* **Parser de Arquivo PCAP.py**
  ```bash
  python "Parser de Arquivo PCAP.py"
  ```
* **Monitor de Dispositivos Ativos em Rede Local.py**
  ```bash
  python "Monitor de Dispositivos Ativos em Rede Local.py"
  ```
* **Monitor de Conexões de Rede em Tempo Real.sh**
  ```bash
  chmod +x "Monitor de Conexões de Rede em Tempo Real.sh"
  ./"Monitor de Conexões de Rede em Tempo Real.sh"
  ```

---

### 🔐 Criptografia & Autenticação

* **Ferramenta de criptografia simétrica de arquivos.py**
  ```bash
  python "Ferramenta de criptografia simétrica de arquivos.py" encrypt arquivo.xlsx arquivo.novacrypt "Senha123!"
  python "Ferramenta de criptografia simétrica de arquivos.py" decrypt arquivo.novacrypt restaurado.xlsx "Senha123!"
  ```
* **Criptografia de Arquivos AES-GCM.py**
  ```bash
  python "Criptografia de Arquivos AES-GCM.py"
  ```
* **Gerador e Verificador de Hash BCRYPT.py**
  ```bash
  python "Gerador e Verificador de Hash BCRYPT.py"
  ```
* **Validador de Estrutura e Assinatura JWT.py**
  ```bash
  python "Validador de Estrutura e Assinatura JWT.py"
  ```

---

### 🛡️ Defesa, SysAdmin & Automação (Blue Team)

* **Monitor de Integridade de Arquivos.py**
  ```bash
  python "Monitor de Integridade de Arquivos.py"
  ```
* **Script Hardening Inicial de Servidor Linux.sh**
  ```bash
  chmod +x "Script Hardening Inicial de Servidor Linux.sh"
  sudo ./"Script Hardening Inicial de Servidor Linux.sh"
  ```
* **Sanitizador de Entradas HTML contra XSS.py**
  ```bash
  python "Sanitizador de Entradas HTML contra XSS.py"
  ```
* **Bloqueador Automático de IPs via Log de Falhas SSH.sh**
  ```bash
  chmod +x "Bloqueador Automático de IPs via Log de Falhas SSH.sh"
  sudo ./"Bloqueador Automático de IPs via Log de Falhas SSH.sh"
  ```
* **Backup Automatizado com Rotação.sh**
  ```bash
  chmod +x "Backup Automatizado com Rotação.sh"
  ./"Backup Automatizado com Rotação.sh" /var/log /tmp/backups
  ```
* **Sanitizador e Formatador de Logs JSON.php**
  ```bash
  php "Sanitizador e Formatador de Logs JSON.php"
  ```

---

## ⚠️ AVISO LEGAL / DISCLAIMER
Estes scripts destinam-se exclusivamente a fins educacionais, de pesquisa e auditoria de segurança autorizada. O uso indevido contra alvos sem permissão explícita é ilegal.

## 📜 Licença
Distribuído sob a licença MIT.
