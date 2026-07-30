import socket
import struct
 
def parse_ip_header(data):
    # Formato do cabeçalho IP: 20 bytes iniciais
    ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
    version_ihl = ip_header[0]
    version = version_ihl >> 4
    ttl = ip_header[5]
    protocol = ip_header[6]
    src_ip = socket.inet_ntoa(ip_header[8])
    dst_ip = socket.inet_ntoa(ip_header[9])
    return version, ttl, protocol, src_ip, dst_ip

def main():
    # Funciona em interfaces RAW (requer permissão de Root/SUDO)
    try:
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        print("[*] Escutando pacotes TCP no nível de IP...")
        while True:
            packet, addr = raw_socket.recvfrom(65535)
            version, ttl, proto, src, dst = parse_ip_header(packet)
            print(f"[IP] {src} -> {dst} | TTL: {ttl} | Protocolo: {proto}")
    except PermissionError:
        print("[-] Erro: Execute este script como superusuário (root/sudo).")

if __name__ == "__main__":
    main()
