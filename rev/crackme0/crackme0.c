#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	setbuf(stdout, NULL);
	char *buff;
	while(1){
		printf("Enter flag > ");
		fgets(buff, 100, stdin);
		if(strcmp(buff, "COPS{pl41nt3xt_fl4g}\n") == 0) {
			printf("Congratulations! You got the flag!\n");
			break;
		}
		else {
			printf("You lose! Try again!\n");
			continue;
		}
	}
	return 0;
}
