#ip:141.225.60.143


from scapy.all import *

ans = raw_input("Enter target IP : ")
ip = IP()
ping = ICMP()
ip.dst = ans
reply = sr1(ip/ping)
if reply.ttl < 65:
    os = "Linux Box"
else:
    os = "Windows Box"

print "Operating System is: %s" %os

