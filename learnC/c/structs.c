#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[50];
    char major [50];
    int age;
    double gpa;
};

int main() {

    struct Student student1;
    strcpy(student1.name, "John");
    strcpy(student1.major, "Computer Science");
    student1.age = 22;
    student1.gpa = 3.819;

    printf("%s is studying %s. He is %d years old and has a %0.2f gpa", student1.name, student1.major, student1.age, student1.gpa);
    
    return 0;
}