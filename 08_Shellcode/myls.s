section .text
  global _start
    _start:
      ; Store the arguments on stack
      xor  eax, eax 
      push eax          ; Use 0 to terminate the string
      push "la"
      push "ls -"
      mov  edx, esp		; save pointer for argv[2]
      push "-c"
      mov  ecx, esp		; save pointer for argv[1]
      push "/sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[3] = 0
      push edx			; argv[2] points "ls -la"
      push ecx			; argv[1] points "-c"
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]
   
      ; For environment variable 
      xor  edx, edx     ; No env variables 

      ; Invoke execve()
      xor  eax, eax     ; eax = 0x00000000
      mov   al, 0x0b    ; eax = 0x0000000b
      int 0x80
