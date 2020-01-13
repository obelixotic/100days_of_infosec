#include <stdio.h>

int asm3(int, int, int);

int main() {
  int ret;

  ret = asm3(0xc264bd5c, 0xb5a06caa, 0xad761175);

  printf("%x\n", ret);
}
