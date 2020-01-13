
all: a.out

asm3.o:
	nasm -o asm3.o -f elf asm3.asm

a.out: asm3.o
	gcc -m32 -o a.out asm3.o main.c

clean:
	rm a.out asm3.o 
