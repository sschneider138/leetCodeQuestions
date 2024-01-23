#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double cubeNum(double num);

int main()
{
    double test = 3;
    double cubedTest = cubeNum(test);
    printf("Your number was %f and your cubed number is %f", 3.0, cubeNum(3));
    return 0;
}

double cubeNum(double num)
{
    return pow(num, 3);
}
