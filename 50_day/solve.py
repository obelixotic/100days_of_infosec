import os
import sys
from pwn import *

e = ELF('bridge_of_death')

data = e.section('.data')
# print data[0]
forestOfEwing = data[32:]

target = []
search = [1,2,3,4,5,6,7,8,9]
solution3 = []

for j in range(len(search)):
	for i in range(len(forestOfEwing)):
		if forestOfEwing[i]==chr(search[j]):
			print "0x"+str(search[j])+": "+ str(i)
			target.append(i)
print target

for i in range(len(target)):
	solution3.append(str(target[i]/256))
	solution3.append(str(target[i]%256))
print solution3

s='\n'
s=s.join(solution3)
print s


context.log_level='debug'
#p = process('./bridge_of_death')
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 8005)
p.sendafter('abc123): ', 'tg1799\n')
p.sendafter('name?\n', 'My name is Sir Lancelot ofCamelot.\n')
p.sendafter('quest?\n', '2\n17\n')
p.sendafter('swallow?\n', s)

p.interactive()
