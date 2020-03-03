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
	solution3.append(target[i]/256)
	solution3.append(target[i]%256)

print solution3


# 0x8: 11296
# 0x5: 21019
# 0x4: 32569
# 0x9: 33057
# 0x2: 34057 //34045
# 0x1: 36427 //36415
# 0x6: 42047
# 0x3: 49014
# 0x7: 49455

# num2 + (num1*0x100) == 11296
# 296  +  110*256   == 11296
# but also num1<256 && num2<256
# also do them in order
# so 256*a + b = _____
