#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
	setbuf(stdout, NULL);
	volatile int t;
  	char buffer[64];
	t = 0;
	printf("Would you like a flag?\n");
	gets(buffer);
	if(t) {
		system("cat /flag.txt");
	}
}
