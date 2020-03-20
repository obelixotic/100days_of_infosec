import random

node = {
	"a": {"node":"a", "val":227, "left":"c", "right":"g"},
	"b": {"node":"b", "val":505, "left":"e", "right":"d"},
	"c": {"node":"c", "val":1128, "left":"d", "right":"g"},
	"d": {"node":"d", "val":531, "left":"i", "right":"d"},
	"e": {"node":"e", "val":289, "left":"f", "right":"h"},
	"f": {"node":"f", "val":937, "left":"a", "right":"f"},
	"g": {"node":"g", "val":410, "left":"j", "right":"a"},
	"h": {"node":"h", "val":314, "left":"a", "right":"j"},
	"i": {"node":"i", "val":866, "left":"j", "right":"b"},
	"j": {"node":"j", "val":710, "left":"j", "right":"d"}
}

for i in range(100):
	sum = 9595
	# print('\n'+str(sum))
	print('\n'+"iteration: ", i)

	path = [node["a"]]
	sum = sum - path[-1]["val"]
	print(path[-1]["node"], str(sum))

	while sum >=0:
		if (sum != 0):
			r = random.random()
			if r<0.5:
				next = path[-1]["left"]
				dir = "left"
			else:
				next = path[-1]["right"]
				dir ="right"

			path.append(node[next])
			sum = sum - path[-1]["val"]
			print(path[-1]["node"], str(sum), str(dir))
		elif (sum == 0):
			print("YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYAY")
			break

#possible solutions
#[0xe3, 0x1f9, 0x468, 0x213, 0x121, 0x3a9, 0x19a, 0x13a, 0x362, 0x2c6]
#(a227, b505,  c1128,  d531,  e289,  f937,  g410,  h314,  i866,  j710

# a [c,g]
# b [e,d]
# c [d,g]
# d [i,d]
# e [f,h]
# f [a,f]
# g [j,a]
# h [a,j]
# i [j,b]
# j [j,d]

#iteration:  51
# a 9368
# c 8240 left
# d 7709 left
# i 6843 left
# b 6338 right
# d 5807 right
# d 5276 right
# d 4745 right
# i 3879 left
# j 3169 left
# d 2638 right
# d 2107 right
# d 1576 right
# i 710 left
# j 0 left
# YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYA
# SOLVE : LLLRRRRLLRRRLLL

# LLLLRRRRLLRRRLL - a c d  i  [j]
# LLLRRRRRLLRRRLL - a c d [d]
# LLLLRRRRLLRRRLL - a c d  i   d???
# LLLLRRRRLLRRRLL

# iteration:  79
# a 9368
# c 8240 left
# d 7709 left
# d 7178 right
# i 6312 left
# j 5602 left
# d 5071 right
# d 4540 right
# i 3674 left
# b 3169 right
# d 2638 right
# d 2107 right
# i 1241 left
# j 531 left
# d 0 right
# YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYA
# 
# iteration:  38
# a 9368
# c 8240 left
# d 7709 left
# d 7178 right
# d 6647 right
# i 5781 left
# b 5276 right
# d 4745 right
# i 3879 left
# j 3169 left
# d 2638 right
# d 2107 right
# d 1576 right
# i 710 left
# j 0 left
# YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYA
# 
# iteration:  31
# a 9368
# c 8240 left
# d 7709 left
# d 7178 right
# i 6312 left
# j 5602 left
# d 5071 right
# d 4540 right
# d 4009 right
# i 3143 left
# j 2433 left
# d 1902 right
# d 1371 right
# i 505 left
# b 0 right
# YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYA
# 
# iteration:  28
# a 9368
# c 8240 left
# d 7709 left
# i 6843 left
# j 6133 left
# d 5602 right
# d 5071 right
# d 4540 right
# d 4009 right
# i 3143 left
# j 2433 left
# d 1902 right
# i 1036 left
# b 531 right
# d 0 right
# YAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYA
# 
# 
# 
# 
# 
# 
# 