#include <stdio.h>
#include <stdlib.h>

int check_key(int key) {
    if (((key - 149) * 3) % 99 == 0) {
        return 1;
    }
    return 0;
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    int key, return_value;
    printf("Enter Key: ");
    scanf("%d", &key);
    return_value = check_key(key);
    if (return_value == 1) {
        puts("Correct Key! Now Keygen Me.");

       
        FILE *file = fopen("/flag.txt", "r");
        if (file != NULL) {
            char buffer[1000]; 
            if (fgets(buffer, sizeof(buffer), file) != NULL) {
                printf("Here is your flag: %s", buffer);
            } else {
                puts("COPS{fake_flag}");
            }
            fclose(file);
        } else {
            puts("Error opening flag.txt");
        }
    } else {
        puts("Wrong Key!");
    }

    return 0;
}
