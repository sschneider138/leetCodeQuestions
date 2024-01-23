#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct employee
{
    int empId;
    char name[100];
    int age;
    char title[100];
    int salary;
};




int main() {

    int empId = 1;
    char name[] = {"John"};
    int age = 23;
    char title[] = "Junior Engineer";
    int salary = 50000;

    FILE* fpointer = fopen("./employees.txt", "w");

    fprintf(fpointer, "Employee: %d, Name: %s, Age: %d, Title: %s, Salary: $%d\n", empId, name, age, title, salary);

    fclose(fpointer);

    return 0;
}