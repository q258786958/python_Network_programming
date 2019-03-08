#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 0003 下午 3:26
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : ARPtest.py
# @Software: PyCharm
# @descrip :
import sys
sys.path.append('/usr/local/python3/lib/python3.7/site-packages/scapy-2.4.2-py3.7.egg/scapy')

from scapy.all import *
if __name__ == '__main__':
    pass
try:
    localmac = '00:50:56:8a:e7:db '
    localip = '192.168.200.15'
    destip = '192.168.200.10'
    ifname = 'ens160'
    ethernet = Ether(src=localmac, dst='FF:FF:FF:FF:FF:FF')
    arp = ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=destip)

    result_raw = srp(ethernet / arp, iface=ifname, timeout=1, verbose=False)
    result = result_raw[0]
    re_arp = result.res[0][1][1]
    print(result.res[0][1][1].fields)
    print(re_arp.fields['hwsrc'])
except Exception:
    pass