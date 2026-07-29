from scapy.all import rdpcap, IP, TCP, UDP

def analyze_pcap(pcap_file: str):
    print(f"[*] Analisando arquivo: {pcap_file}")
    packets = rdpcap(pcap_file)
    
    conversations = set()
    for pkt in packets:
        if IP in pkt:
            proto = "TCP" if TCP in pkt else ("UDP" if UDP in pkt else "OUTRO")
            sport = pkt.sport if (TCP in pkt or UDP in pkt) else 0
            dport = pkt.dport if (TCP in pkt or UDP in pkt) else 0
            conversations.add((pkt[IP].src, sport, pkt[IP].dst, dport, proto))

    for src, sp, dst, dp, pr in list(conversations)[:15]:
        print(f"[{pr}] {src}:{sp} ---> {dst}:{dp}")

if __name__ == "__main__":
    print("RequerScapy instalado (`pip install scapy`) e um arquivo .pcap válido.")