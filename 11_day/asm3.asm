  global asm3

  section text
asm3:
  push ebp
  mov ebp, esp
  xor eax, eax
  mov ah, [ebp+0x09]
  shl ax, 0x10
  sub al, [ebp+0xd]
  add ah, [ebp+0xf]
  xor ax, word [ebp+0x10]
  pop ebp
  ret
