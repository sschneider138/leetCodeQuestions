#include <stdio.h>
#include <stdlib.h>

int* twoSum(int arr[], int goal)
{
    int *returnArr = (int *)malloc(2 * sizeof(int));

    returnArr[0] = 1;
    returnArr[1] = 1;

    return returnArr;
}

int main()
{
    int testArr[] = {1, 2, 3};

    int *myAns = twoSum(testArr, 3);

    printf("here is the printed array: %d, %d\n", myAns[0], myAns[1]);
    free(myAns);
}