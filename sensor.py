import time
from scapy.all import sniff, IP, TCP
from services import CyberAttackService


cyber_attack_service = CyberAttackService()
sniff(
    iface='enp0s8', store=0,
    filter="ip and tcp and dst host 192.168.56.103",
    prn=lambda packet: cyber_attack_service.create_model(
        source_ip=packet[IP].src, dest_ip=packet[IP].dst,
        source_port=packet[TCP].sport, dest_port=packet[TCP].dport,
        protocol=packet[IP].proto, time=time.time()
    )
)
