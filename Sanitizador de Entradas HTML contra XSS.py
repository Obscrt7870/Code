import html

def sanitize_user_input(raw_input: str) -> str:
    # Remove ou converte caracteres perigosos (<, >, &, ", ')
    sanitized = html.escape(raw_input.strip())
    return sanitized

if __name__ == "__main__":
    malicious_payload = "<script>alert('XSS Executado!')</script>"
    safe_output = sanitize_user_input(malicious_payload)
    
    print(f"Entrada Bruta:  {malicious_payload}")
    print(f"Entrada Limpa:  {safe_output}")