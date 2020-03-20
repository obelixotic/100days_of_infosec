from pwn import *

p = process('./labyrinth')

context.log_level = 'debug'

p.sendafter('through?\n', 'LLLRRRRLLRRRLLL\n')

p.interactive()