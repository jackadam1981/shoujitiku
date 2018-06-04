import pcap  # 安装的是pypcap，本博客有安装方法，不过也比较乱，试试吧。
import dpkt

pc = pcap.pcap()
for timestamp, buf in pc:
    eth = dpkt.ethernet.Ethernet(buf)
    print(eth)
