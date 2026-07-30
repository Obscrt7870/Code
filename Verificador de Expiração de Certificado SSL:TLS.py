import socket
import ssl
from datetime import datetime

def check_ssl_expiry(hostname: str, port: int = 443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            
            # Formato de data: MMM DD HH:MM:SS YYYY GMT 
            date_fmt = r"%b %d %H:%M:%S %Y %Z"
            not_after = datetime.strptime(cert['notAfter'], date_fmt)
            days_left = (not_after - datetime.utcnow()).days
            
            print(f"[+] {hostname}:{port}")
            print(f"    Validade: {not_after}")
            print(f"    Dias restantes: {days_left}")

if __name__ == "__main__":
    check_ssl_expiry("github.com")
