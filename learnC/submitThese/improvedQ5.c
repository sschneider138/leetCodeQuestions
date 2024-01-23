#include <stdio.h>

void add(int x, int y, int *c)
{
    *c = x + y;
}

int main()
{
    int foo;
    add(1, 2, &foo);
    printf("%d", foo / 2);
    return 0;
}


