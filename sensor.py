import time
from scapy.all import sniff, IP, TCP
from models import CyberAttack
from dbsession import DBSession
 

def pcap_default(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP): 
        db_session = DBSession()
        ip = packet[IP]
        tcp = packet[TCP]

        cyber_attack = CyberAttack(source_ip=ip.src, dest_ip=ip.dst,
                                   source_port=tcp.sport, dest_port=tcp.dport,
                                   protocol=ip.proto, time=time.time())
        db_session.db_connect()
        db_session.db_update(cyber_attack)


class Sensor():
    iface = None
    store = None
    prn = None


    def start_sniffing(self):
        sniff(iface=self.iface, store=self.store, prn=self.prn)

    
    def __init__(self, iface='enp0s8', store=0, prn=lambda packet: pcap_default(packet)):
        self.iface = iface
        self.store = store
        self.prn = prn


sens = Sensor()
sens.start_sniffing()
