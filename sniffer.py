import time
from scapy.all import sniff, IP, TCP


def prettify(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip = packet[IP]
        tcp = packet[TCP]

        srcip = ip.src
        dstip = ip.dst
        proto = ip.proto

        sport = tcp.sport
        dport = tcp.dport
        timestamp = time.time()

        print("=" * 50)
        print("srcip: {0}".format(srcip))
        print("dstip: {0}".format(dstip))
        print("proto: {0}".format(proto))
        print("sport: {0}".format(sport))
        print("dport: {0}".format(dport))
        print("timestamp: {0}".format(timestamp))
        print("=" * 50)


sniff(count=1, prn=lambda packet: prettify(packet))