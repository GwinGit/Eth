#!/usr/bin/env python3

from scapy.all import *

ttl = 1
while True:
	pkg = IP(dst='216.58.209.36', ttl=ttl)/ICMP()
	answer = sr1(pkg)
	
	if answer.type == 0:
		print("----------------------------------------")
		print(f"Successfull Answer using ttl {ttl}")
		exit(0)
	
	if answer.type == 11 and answer.code == 0:
		ttl += 1
	else:
		answer.show()
		print("Something else went wrong!")
		exit(1)

