#include <stdio.h>

int main() {
    int variableInt = 10;
    char variableChar = 'a';
    double variableDouble = 10.123;

    printf("displaying the value of variableInt: %d\n", variableInt);
    printf("displaying the value of variableChar: %c\n", variableChar);
    printf("displaying the value of double: %.2f\n", variableDouble);

    char* name = "John";

    printf("%i", sizeof(name)/sizeof(char));
}