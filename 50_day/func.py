import os
import sys

def main():

	num1 = sys.argv[1]
	num2 = sys.argv[2]
	num3 = func(num1,0,0x14)

	print num1, num2, num3
	# return (num3 != num2)

def func(param_1, param_2, param_3):
	a = param_2 + (param_3 - param_2) / 2
	if (param_1 < a):
		b = func(param_1,param_2,(a - 1))
		c = a + b
	else:
		if (a < param_1):
			b = func(param_1,(a + 1),param_3)
			c = a + b
		else:
				c = a
	return c


if __name__ == '__main__':
	main()


#didnt work, too much recursion for python, lol
#run in gdb to see what it does