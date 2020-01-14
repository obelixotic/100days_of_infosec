
all: a.out

asm4.o:
	nasm -o asm4.o -f elf asm4.asm

a.out: asm4.o
	gcc -m32 -o a.out asm4.o main.c
	rm asm4.o

clean:
	rm a.out
