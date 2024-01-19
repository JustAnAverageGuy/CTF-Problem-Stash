#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void init() {
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);
}

void win() {
	system("cat /flag.txt");
}

int main(int argc, char **argv) {
	init();
	volatile int (*t)();
  	char buffer[64];
	t = 0;
	fgets(buffer,0x50,stdin);
	if(t) {
		system("cat /fake_flag.txt");
		t();
	}
}
