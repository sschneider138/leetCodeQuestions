#include <stdio.h>

int main() {

    int luckyNumbers[20] = {0};

    for (int i = 0; i < sizeof(luckyNumbers) / sizeof(int); i++) {
        printf("%d\n",luckyNumbers[i] );
    }
    
    return 0;
}