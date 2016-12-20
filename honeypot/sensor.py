import time

from scapy.all import sniff, IP, TCP, TCP_SERVICES

from honeypot.configs import SENSOR_IP
from honeypot.services import CyberAttackService

TCP_REVERSE = dict((TCP_SERVICES[k], k) for k in TCP_SERVICES.keys())

cyber_attack_service = CyberAttackService()


def handle_packet(packet):
    source_ip = packet[IP].src
    dest_ip = packet[IP].dst
    source_port = packet[TCP].sport
    dest_port = packet[TCP].dport

    try:
        service = TCP_REVERSE[packet[TCP].dport]
    except:
        service = "unknown"

    if cyber_attack_service.list_models(source_ip=source_ip, dest_ip=dest_ip, source_port=source_port, time=int(time.time())).count() == 0:
        cyber_attack_service.create_model(
            source_ip=source_ip, dest_ip=dest_ip,
            source_port=source_port, dest_port=dest_port,
            service=service, time=int(time.time())
        )

sniff(
    iface='enp0s8', store=0,
    filter="ip and tcp and dst host " + SENSOR_IP,
    prn=handle_packet
)
