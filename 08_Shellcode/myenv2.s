section .text
  global _start
    _start:
	  BITS 32
	  jmp short two
    one:
 	  pop ebx
 	  xor eax, eax
 	  mov [ebx+12], al				; /usr/bin/env0
 	  mov [ebx+13], ebx				; /usr/bin/env0/usr
 	  mov [ebx+17], eax				; /usr/bin/env0/usr0000
 	  mov [ebx+21], dword "a=11"	; /usr/bin/env0/usr0000a=11
 	  mov [ebx+25], al				; /usr/bin/env0/usr0000a=110
 	  mov [ebx+26], dword "b=22"	; /usr/bin/env0/usr0000a=110b=22
 	  mov [ebx+30], al				; /usr/bin/env0/usr0000a=110b=220
 	  lea ecx, [ebx+21]
 	  mov [ebx+32], ecx
 	  lea ecx, [ebx+26]
 	  mov [ebx+36], ecx
 	  mov [ebx+40], eax
 	  lea ecx, [ebx+13] 
 	  lea edx, [ebx+32]
 	  mov al,  0x0b
 	  int 0x80
    two:
 	  call one
 	  db '/usr/bin/env*AAAABBBBCCCC*DDDDnrrrrrrrrrrrrrrrrrrrhhhhhhhhhhhhrrrrrrrr'
