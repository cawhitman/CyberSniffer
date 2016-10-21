import time
from scapy.all import sniff, IP, TCP
from services import CyberAttackService


class Sensor(object):

    def __init__(self, callback, iface='enp0s8', store=0):
        self.iface = iface
        self.store = store
        self.callback = callback

    def start_sniffing(self):
        sniff(iface=self.iface, store=self.store, prn=self.callback)


service = CyberAttackService()


def pcap_default(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip = packet[IP]
        tcp = packet[TCP]

        service.create_model(source_ip=ip.src, dest_ip=ip.dst,
                             source_port=tcp.sport, dest_port=tcp.dport,
                             protocol=ip.proto, time=time.time())

sens = Sensor(callback=lambda packet: pcap_default(packet))
sens.start_sniffing()
