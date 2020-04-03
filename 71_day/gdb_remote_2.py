from pwn import *

context.log_level ='debug'

# p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
# b = process('./new_brutus')
# p = remote('127.0.0.1', 8000) #local process but connecting over socket

gdb_script = '''
set breakpoint pending on 
break main
set breakpoint pending off
set follow-fork-mode child
break handle
continue
'''

p = gdb.debug('./new_brutus', gdb_script)
sleep(1)
# i = raw_input()
# gdb.attach(p, '')
r = remote('127.0.0.1', 8000) #local process but connecting over socket

r.interactive()
# p.sendafter('abc123): ', 'tg1799\n')
# r.sendafter('name?\n', 'asdafgjksgd\n')
# r.sendafter('data\n', 'iugqwwd\n')

# set {int}0x0041320=0x90
# set {int}0x0041321=0x90
# set {int}0x0041322=0x90
# set {int}0x0041323=0x90
# set {int}0x0041324=0x90
# set {int}0x0041325=0x90

