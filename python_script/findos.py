#scapy

>>> IP()
>>> ip = IP()
>>> ip.display()

>>> ip.dst = "192.168.15.20"

To verify the changes were made:
>>> ip.display()

create an ICMP object which is ping
>>> ping = ICMP()
>>> ping.display()

Send one packet to Window System.

>>> window = sr1(ip/ping)

>>> window.display()

set the destination IP to linux machine
>>> ip.dst = "192.168.15.22"
>>> linux = sr1(ip/ping)

>>> linux.display()

Window starts ttl value to 128 and linux start to 64. In each router it will decrement by 1.

>>> exit()




#ip:141.225.60.143


from scapy.all import *

ans = raw_input("Enter target IP : ")
ip = IP()
ping = ICMP()
ip.dst = ans
reply = sr1(ip/ping)
if reply.ttl < 65:
    os = "Linux Operating System"
else:
    os = "Windows Operating System"

print "Operating System is: %s" %os

