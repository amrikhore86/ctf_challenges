#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int pin, i;
    for (i = 0; i < 3; i++) {
        printf("Enter 4-digit PIN: ");
        if (scanf("%d", &pin) != 1) {
            printf("Invalid input\n");
            return 1;
        }
        if (pin == 3769) {
            char flag[] = "Q1N7UGluX0F1dGhlbnRpY2F0ZWR9";
            printf("Flag: %s\n", flag);
            return 0;
        } else {
            printf("Incorrect PIN\n");
        }
    }
    printf("Access denied\n");
    return 1;
}
