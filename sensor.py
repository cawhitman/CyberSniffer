from scapy.all import sniff


def pcap_default(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        data_out = {'srcip':'',
                    'dstip':'',
                    'proto':'',
                    'sport':'',
                    'dport':'',
                    'timestamp':''}
        
        ip = packet[IP]
        tcp = packet[TCP]

        data_out['srcip'] = ip.src
        data_out['dstip'] = ip.dst
        data_out['proto'] = ip.proto
  
        data_out['sport'] = tcp.sport
        data_out['dport'] = tcp.dport
        data_out['timestamp'] = time.time()


sniff(iface='enp0s8', store=0, prn=lambda packet: pcap_default(packet))
