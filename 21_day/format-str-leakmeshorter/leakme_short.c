#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void echo(){
    printf("Give me something short to say: \n");
    fflush(stdout);
    char input_string[10];
    fgets(input_string, 9, stdin);
    input_string[strcspn(input_string, "\n")] = '\x00';
    printf("Holy ");
    printf(input_string);
    printf(", Batman!\n");
}

void challenge(int magic_number){
    char input_string[60];
    fgets(input_string, 59, stdin);
    int user_input = atoi(input_string);
    if(user_input == magic_number){
        printf("You win!! Your number was:\n");
        puts(input_string);
        fflush(stdout);
        system("/bin/sh");
    }else{
        printf("Nope!\n");
    }
}

int main (int argc, char** argv) {
    // To generate a cryptographically secure random number, use libsodium:
    // https://stackoverflow.com/questions/822323/how-to-generate-a-random-int-in-c/39475626#39475626
    // Here we just use a method that's less secure but which doesn't require 
    // installing another library.
    srand(time(NULL)); // initialization
    int a = rand();
    echo();
    printf("Hey, what number am I thinking of? \n");
    fflush(stdout);
    challenge(a);
    return 0;
}