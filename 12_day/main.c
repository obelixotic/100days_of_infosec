#include <stdio.h>

int asm4(String);

int main() {
	int ret;

	ret = asm4("picoCTF_fdb55");

	printf("%x\n", ret);
}