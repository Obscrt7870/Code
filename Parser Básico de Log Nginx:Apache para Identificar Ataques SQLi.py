import re

SQLI_PATTERNS = [
    r"UNION\s+SELECT",
    r"OR\s+1=1",
    r"SLEEP\(",
    r"--",
    r"BENCHMARK\("
]
 
def parse_access_log(log_path: str):
    compiled_patterns = [re.compile(p, re.IGNORECASE) for p in SQLI_PATTERNS]
    
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            for pattern in compiled_patterns:
                if pattern.search(line):
                    print(f"[!] Suspeita de SQLi na linha {line_num}: {line.strip()}")
                    break

if __name__ == "__main__":
    # Exemplo de teste gravando um arquivo rápido
    with open("test_access.log", "w") as f:
        f.writelines([
            '192.168.1.10 - - [20/May/2026] "GET /index.php?id=1 HTTP/1.1" 200 1024\n',
            '192.168.1.50 - - [20/May/2026] "GET /product.php?id=1%20UNION%20SELECT%20null,version() HTTP/1.1" 200 500\n'
        ])
    
    parse_access_log("test_access.log")
