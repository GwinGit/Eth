#!/usr/bin/env python3

from scapy.all import *


def spoof_echo_reply(pkt):
	if pkt[ICMP].type != 8:
		return

	ip = IP()
	ip.ihl = pkt[IP].ihl
	ip.src = pkt[IP].dst
	ip.dst = pkt[IP].src
	
	icmp = ICMP()
	icmp.type = 0
	icmp.id = pkt[ICMP].id
	icmp.seq = pkt[ICMP].seq
	
	data = pkt[Raw].load
	
	response = ip/icmp/data
	send(response)


sniff(iface="br-8e21ad3a9d02", filter="icmp and src host 10.9.0.5", prn=spoof_echo_reply)

