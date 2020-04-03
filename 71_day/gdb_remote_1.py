from pwn import *

context.log_level ='debug'

# p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
b = process('./new_brutus')
# p = remote('127.0.0.1', 8000) #local process but connecting over socket

sleep(1)
gdb.attach(b, '')
r = remote('127.0.0.1', 8000)

r.interactive()
# p.sendafter('abc123): ', 'tg1799\n')
# r.sendafter('name?\n', 'asdafgjksgd\n')
# r.sendafter('data\n', 'iugqwwd\n')