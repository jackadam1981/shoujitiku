# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-01-18 14:48
# @Author  : Jackadam
# @Email   :
# @File    : listen.py
# @Software: PyCharm
import pcap
import dpkt
def sniffer(tag):
    print('start sniffer')
    pc = pcap.pcap()
    print('read pcap', tag)
    flag = False
    i = 1
    j = 0
    for timestamp, buf in pc:
        print(i)
        i = i + 1
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        if isinstance(ip.data, dpkt.tcp.TCP):
            print('t', i, j)
            tcp = ip.data
            print(tcp.data)
            if i == j + 1:
                end_add = tcp.data
                flag = True
            else:
                try:
                    request = dpkt.http.Request(tcp.data)
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue

                # if request.headers['host'] == tag:
                if tag in request.uri:
                    j = i
                    re_add = request
        if flag == True:
            print('------------')
            re_add.headers['cookie']=re_add.headers['cookie']+str(end_add)[2:-9]
            print(re_add.headers.get('cookie'))
            print(re_add)
            print('------------')
            return re_add


if __name__ == '__main__':
    print('hello world!')
    request = sniffer('/YT_WeiXin/Default?oid=')
    # request = sniffer('www.google.com')
    print('---------')
    print('return all ', request)
    print(type(request))
