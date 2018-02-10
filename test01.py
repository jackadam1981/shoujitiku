# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018-02-06 18:22
# @Author  : Jackadam
# @Email   :
# @File    : test.py
# @Software: PyCharm
# !/usr/bin/env python3.2
print('hello')
import pcap
pc=pcap.pcap()
for d,b in pc:
    print(d,b)