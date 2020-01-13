asm3:
	<+0>:	push   ebp						;function prologue
	<+1>:	mov    ebp,esp					;function prologue
	<+3>:	xor    eax,eax					;eax = 0
	<+5>:	mov    ah,BYTE PTR [ebp+0x9] 	;move bd into ah
	<+8>:	shl    ax,0x10					;ah = bd thus, ax = 0xbd00 
											;bit shift left = 0xbd000000
	<+12>:	sub    al,BYTE PTR [ebp+0xd] 	;0 - 6c = -6c => -108
											;-108 => 2's complement = ff94
											;thus, al = 94
	<+15>:	add    ah,BYTE PTR [ebp+0xf] 	;ah = b5
	<+18>:	xor    ax,WORD PTR [ebp+0x10] 	;ax = b594
											;ebp+0x10 = 1175 (lil endian)
											;b594^1175 = a4e1
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret

Notes: 
Arguments get stored in reverse order due to little endian format 
ie least significant bit first

<<Memory Stack>>
-----------
75 11 76 ad  => ebp+0x10 0x11 0x12 0x13
aa 6c a0 b5  => ebp+0xc  0xd  0xe  0xf
5c bd 64 c2  => ebp+0x8  0x9  0xa  0xb
ret add 	 => ebp+0x4
ebp			 => 0
-----------

<<Registers>>
|	  	|	  	|	ah	|	al	|
|		|		|	    ax		|
|			   eax				|