import dns.resolver

def check_email_security(domain: str):
    print(f"=== Analisando Domínio: {domain} ===")
    
    # Checar SPF
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        spf_found = False
        for rdata in answers:
            txt = rdata.to_text()
            if "v=spf1" in txt:
                print(f"[+] SPF Encontrado: {txt}")
                spf_found = True
        if not spf_found:
            print("[-] Nenhuma política SPF configurada.")
    except Exception as e:
        print(f"[-] Erro ao buscar SPF: {e}")

    # Checar DMARC
    try:
        dmarc_domain = f"_dmarc.{domain}"
        answers = dns.resolver.resolve(dmarc_domain, 'TXT')
        for rdata in answers:
            print(f"[+] DMARC Encontrado: {rdata.to_text()}")
    except Exception:
        print("[-] Nenhum registro DMARC encontrado.")

if __name__ == "__main__":
    check_email_security("example.com")