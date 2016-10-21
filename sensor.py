import time
from scapy.all import sniff, IP, TCP
from services import CyberAttackService

"""
class Sensor(object):

    def __init__(self, callback, filter=None, iface='enp0s8', store=0):
        self.callback = callback
        self.iface = iface
        self.store = store
        self.filter = filter

    def start_sniffing(self):
        sniff(iface=self.iface, store=self.store, prn=self.callback)

    def handle_packet(self, packet):
        if packet.haslayer(IP) and packet.haslayer(TCP):
            ip = packet[IP]
            tcp = packet[TCP]






def pcap_default(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip = packet[IP]
        tcp = packet[TCP]
        
        if ip.dst == '192.168.56.103':
            service.create_model(source_ip=ip.src, dest_ip=ip.dst,
                                 source_port=tcp.sport, dest_port=tcp.dport,
                                 protocol=ip.proto, time=time.time())

"""

cyber_attack_service = CyberAttackService()
sniff(
    iface='enp0s8', store=0,
    filter="proto ip and proto tcp and dst host 192.168.56.103",
    prn=lambda packet: cyber_attack_service.create_model(
        source_ip=packet[IP].src, dest_ip=packet[IP].dst,
        source_port=packet[TCP].sport, dest_port=packet[TCP].dport,
        protocol=packet[IP].proto, time=time.time()
    )
)
