#include <stdio.h>
#include <stdio.h>

int main()
{
    char name[9];

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);

    printf("Your name is %s\n", name);

    printf("size of name arr is %lu\n", sizeof(name));

    return 0;
}