#include<stdio.h>
#include"test.S"

extern void test();

int main() {
    printf("Flag: 0x%x\n", test(0xaeed09cb,0xb7acde91,0xb7facecd));
}
