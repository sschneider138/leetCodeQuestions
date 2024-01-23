#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    // create vars
    printf("printing variables:\n");
    int age = 30;
    double gpa = 3.4;
    char grade = 'A';
    printf("%d\n", age);
    printf("%f\n", gpa);
    printf("%c\n", grade);
    printf("\n");

    // create pointers for vars
    printf("printing variables' memory addresses:\n");
    int *pAge = &age;
    double *pGpa = &gpa;
    char *pGrade = &grade;
    printf("%p\n", pAge);
    printf("%p\n", pGpa);
    printf("%p\n", pGrade);
    printf("\n");

    // dereference pointers for vars
    // when you dereference a pointer, the variable is now whatever is stored at the memory address that the pointer is pointing to
    printf("printing dereferenced pointers:\n");
    printf("%d\n", *pAge);
    printf("%f\n", *pGpa);
    printf("%c\n", *pGrade);
    printf("\n");

    return 0;
}