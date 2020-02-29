import os
import sys
from pwn import *

for i in range(1,256):	
	context.log_level='debug'
	p = process('./dora')
	# p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 8005)
	# p.sendafter('abc123): ', 'tg1799\n')
	p.sendafter('key?\n', str(i))

	p.interactive()


