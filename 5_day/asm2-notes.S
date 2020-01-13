asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] /*ebp+12 is arg1 ie 0x15*/
	<+9>:	mov    DWORD PTR [ebp-0x4],eax /*copy 0x15 ebp-0x4*/
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] /*ebp+0x8 is arg0 ie 0xc*/
	<+15>:	mov    DWORD PTR [ebp-0x8],eax /*copy 0xc to ebp-0x8*/
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1 /*0x15+0x1=0x16 or 21+1=22*/
	<+24>:	add    DWORD PTR [ebp-0x8],0xaf /*0xc+0xaf=0xbb or 12+175=187*/
	<+31>:	cmp    DWORD PTR [ebp-0x8],0xa3d3 /*12,41939*/
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4] /*21+240=261*/
	<+43>:	leave
	<+44>:	ret

/*
41939-12=41927
41927/175=239
+1 to cross is so 240
21+240=261
or 0x105
flag 0x105
*/

/*
What does asm2(0xc,0x15) return?
asnwer: 0x105
flag: pcioCTF{0x105}
*/
