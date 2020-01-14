	global asm4

	section text
asm4:
	push   ebp
	mov    ebp,esp
	push   ebx
	sub    esp,0x10
	mov    dword [ebp-0x10],0x260
	mov    dword [ebp-0xc],0x0
	jmp    .asm4_27
.asm4_23:
	add    dword [ebp-0xc],0x1
.asm4_27:
	mov    edx,dword [ebp-0xc]
	mov    eax,dword [ebp+0x8]
	add    eax,edx
	movzx  eax,byte [eax]
	test   al,al
	jne    .asm4_23
	mov    dword [ebp-0x8],0x1
	jmp    .asm4_138
.asm4_51:
	mov    edx,dword [ebp-0x8]
	mov    eax,dword [ebp+0x8]
	add    eax,edx
	movzx  eax,byte [eax]
	movsx  edx,al
	mov    eax,dword [ebp-0x8]
	lea    ecx,[eax-0x1]
	mov    eax,dword [ebp+0x8]
	add    eax,ecx
	movzx  eax,byte [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	mov    edx,eax
	mov    eax,dword [ebp-0x10]
	lea    ebx,[edx+eax*1]
	mov    eax,dword [ebp-0x8]
	lea    edx,[eax+0x1]
	mov    eax,dword [ebp+0x8]
	add    eax,edx
	movzx  eax,byte [eax]
	movsx  edx,al
	mov    ecx,dword [ebp-0x8]
	mov    eax,dword [ebp+0x8]
	add    eax,ecx
	movzx  eax,byte [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	add    eax,ebx
	mov    dword [ebp-0x10],eax
	add    dword [ebp-0x8],0x1
.asm4_138:
	mov    eax,dword [ebp-0xc]
	sub    eax,0x1
	cmp    dword [ebp-0x8],eax
	jl     .asm4_51
	mov    eax,dword [ebp-0x10]
	add    esp,0x10
	pop    ebx
	pop    ebp
	ret    

