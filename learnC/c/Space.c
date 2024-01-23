#include <stdio.h>
#include <stdlib.h>


int main() {
    int lucky = 23;
    printf("Value: %i \n", lucky);
    printf("Address: %p \n", &lucky);

    char *str = malloc(6);
    str[0] = 'H';
    str[1] = 'E';
    str[2] = 'L';
    str[3] = 'L';
    str[4] = 'O';
    str[5] = '\0';

    for ( int i = 0; i < 6; i++)  {
        printf("%c", str[i]);
    }

    if (!str) {
        printf("memory free");
    } else {
        printf("memory not free");
    }
    free(str);


    return 0;
}