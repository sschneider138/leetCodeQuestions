#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    int nums[3][3] =
        {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}};

    for (int i = 0; i < sizeof(nums[i]) / sizeof(int); i++)
    {
        for (int j = 0; j < sizeof(nums[j]) / sizeof(int); j++)
        {
            printf("%d, ", nums[i][j]);
        }
        printf("\n");
    }

    printf("size of the 2d array is: %d", sizeof(nums) / sizeof(int));
    printf("size of the 2d array is: %d", sizeof(nums[0]) / sizeof(int));
    return 0;
}