from pwn import *

text = []
x = [1096770097,
1952395366,
1600270708,
1601398833,
1716808014,
1734305381,
828716089,
895562083]

for value in x:
    text.append(p32(value, endian='big'))

flag="".join(text)
print("picoCTF{"+flag+"}")
