#include <stdio.h>
#include <string.h>
void enc(char* str) {
    for (int i = 0; str[i] != '\0'; ++i) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = (str[i] - 'a' + 9) % 26 + 'a';
        } else if (str[i] >= 'A' && str[i] <= 'Z') {
            str[i] = (str[i] - 'A' + 9) % 26 + 'A';
        }
    }
}
int main() {
   const char res[] = "LXYB{rJJvlaJLtnm149}";
    char inp[1000];  
    char mod[20];
    printf("Enter the password: ");
    scanf("%s", inp);
    strcpy(mod, inp);
    enc(mod);
    if (strcmp(res, mod) == 0) {
        printf("Correct password!\n");
    } else {
        printf("Wrong password!\n");
    }
    return 0;
}
