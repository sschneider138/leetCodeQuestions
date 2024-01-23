#include <stdio.h>

void sortArr(int array[], int size)
{
    for (int i = 0; i < size -1 ; i++)
    {
        for (int j = 0; j < size - i -1; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

void printArr(int array[], int arrSize)
{
    for (int i = 0; i < arrSize; i++)
    {
        printf("%d, ", array[i]);
    }
}

int main()
{
    int array[] = {9, 1, 8, 2, 7, 3, 6, 4, 5};
    int arrSize = sizeof(array) / sizeof(int);

    sortArr(array, arrSize);
    printArr(array, arrSize);

    return 0;
}