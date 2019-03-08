import sys
sys.path.append('/usr/local/python3/lib/python3.7/site-packages/scapy-2.4.2-py3.7.egg/scapy')
from scapy.all import *
import time
import struct
import random
import sys
import re
import optpars
send_time = time.time()
time_in_bytes = struct.pack('>d', send_time)
ipl = IP(dst='192.168.200.10', ttl=60)
icmpl = ICMP(id=50, seq=60)

ping_one_reply = sr1(IP(dst='192.168.200.10', ttl=60)/icmpl/time_in_bytes, timeout = 1, verbose=False)
print(ping_one_reply.getlayer(ICMP).fields)
#产生一个ICMP echo request数据包，scapy默认类型为echo request，数据部分为2进制编码后的时间