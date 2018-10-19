import pcap
for ts, pkt in pcap.pcap():
    print (ts, pkt)