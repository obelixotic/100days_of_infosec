from pwn import *

context.log_level='debug'

# p = process('./numerix')
p = remote('url', port)
p.sendafter('abc123): ', 'tg1799\n')
p.sendafter('favoritest number?\n', str(0xdeadbeef)+'\n')
p.sendafter('favorite number?\n', str(0x539)+'\n')
p.sendafter('next one?\n', str(0xc0def001337beef)+'\n')
p.sendafter('One more!\n', str(0xd0d0f0c0)+'\n')

p.interactive()
