import urllib.request

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def analyze_headers(url: str):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            headers = response.info()
            print(f"=== Análise de Cabeçalhos: {url} ===")
            for header in SECURITY_HEADERS:
                if header in headers:
                    print(f"[✓] {header}: {headers[header]}")
                else:
                    print(f"[✗] {header}: ausente")
    except Exception as e:
        print(f"Erro ao acessar URL: {e}")

if __name__ == "__main__":
    analyze_headers("https://github.com")