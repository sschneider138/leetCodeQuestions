#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *getName()

{
    char *name = (char *)malloc(5);

    if (name != NULL)
    {
        strcpy(name, "John\n");
    }

    return name;
}

void sayHiToUser(char user[])
{
    printf("Hi there %s", user);
}

void greetUser(char name[])
{
    printf("Hi there! your name was passed in as a parameter and it is: %s", name);
}

int main()
{
    // char *returnedName = getName();
    // printf("my name is %s", returnedName);

    // sayHiToUser("Jacob");

    greetUser(getName());
    return 0;
}