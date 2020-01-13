asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x35d			/*compare value at ebp+0x8 (ie arg0 -> 0x53e) with 0x35d*/
	<+10>:	jg     0x512 <asm1+37>							/*if greater then jump --> yes 0x53e is greater than 0x35d*/
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x133
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xb
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xb
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x53e		/*compare value at ebp+0x8 (0x53e) with 0x53e*/
	<+44>:	jne    0x523 <asm1+54>							/*if not equal, jump, else go to next instruction*/
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]			/*move (copy) value at ebp+0x8 (ie 0x53e) into eax*/
	<+49>:	sub    eax,0xb											/*subtract 0xb from eax -> 0x53e-0xb = 0x533*/
	<+52>:	jmp    0x529 <asm1+60>							/*jump to instruction 60*/
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xb
	<+60>:	pop    ebp													/*pop before returning eax*/
	<+61>:	ret																	/*return value at eax as per calling converntion */

/*
what does asm1(0x53e) return?
answer: 0x533
flag: pcioCTF{0x533}
*/
