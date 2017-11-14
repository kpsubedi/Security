Discovery Tools
===============
1. Passive 
2. Active


Layer 2 discovery
*****************
# arping <target address>
# arping 192.168.10.15

Send one packet count, c = 1

# arping 192.168.10.15 -c 1

Wireshark
=========
Filter out only arp packets

eth.type == 0x0806

Using NMAP
==========
# nmap -PR -sn 192.168.10.1-254

# netdiscover -r 192.168.10.0/24 

Passive discovery using -p switch

# netdiscover -p -r 192.168.10.0/24

Layer 3 Discovery
******************
# fping -h
# fping -a -c 2 192.168.10.20

# fping -a -c 2 192.168.10.1 192.168.10.254

# cat > iplist.org
192.168.10.20
192.168.10.15

# fping -f /root/iplist.org

# hping3 -h

# hping3 -1 192.168.10.20

# hping3 -1 192.168.10.20 -c 1

using ping we can build ping swepper.
# ping -c 1 192.168.10.20
# ping -c 1 102.168.10.200

Notice "bytes from" in ping response.
# ping -c 1 192.168.10.20 | grep "bytes from"

# ping -c 1 192.168.10.200 | grep "bytes from"

# ping -c 1 192.168.10.20 | grep "bytes from" | cut -d " " -f4
# ping -c 1 192.168.10.20 | grep "bytes from" | cut -d " " -f4 | cut -d":" -f1

#!/bin/bash

for i in $(seq 1 20); do
ping -c 1 192.168.20.$i | grep "bytes from" | cut -d" " -f 4 | cut -d":" -f1 &
done


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

