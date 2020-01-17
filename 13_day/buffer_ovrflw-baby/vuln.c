#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  //puts("Running the segfault handler.\n");
  //fprintf(stdout, "%s\n", flag);  
  fprintf(stdout, "%s\n", flag);
  fflush(stdout);
  exit(1);
}

void vuln(){
  char buf[16];
  gets(buf);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  fflush(stdout);
  puts("Please enter your string: ");
  fflush(stdout);
  vuln();
  return 0;
}
