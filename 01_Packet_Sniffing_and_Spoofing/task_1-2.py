#!/usr/bin/env python3

from scapy.all import *


def print_pkt(pkt):
	pkt.show()


ip = IP()
ip.dst = '10.9.0.5'
ip.src = '10.9.0.6'
icmp = ip/ICMP()

icmp.show()
send(icmp)

