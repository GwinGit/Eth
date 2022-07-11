#!/usr/bin/env python3

from scapy.all import *


def print_pkt(pkt):
	pkt.show()


pkt = sniff(iface="br-8e21ad3a9d02", filter="src host 10.9.0.5 and tcp dst port 23", prn=print_pkt)

