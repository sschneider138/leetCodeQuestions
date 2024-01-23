#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char *isPalindromic(int num)
{
    if (num < 0)
    {
        return "false";
    }

    char numStr[99];
    sprintf(numStr, "%d", num);

    int start = 0;
    int end = (strlen(numStr) - 1);

    if (strlen(numStr) % 2 == 0)
    {
        while (start != end)
        {
            if (numStr[start] == numStr[end])
            {
                start++;
                end--;
            }
            else
            {
                return "false";
            }
        }
    }

    else
    {
        while (start < end)
        {
            if (numStr[start] == numStr[end])
            {
                start++;
                end--;
            }
            else
            {
                return "false";
            }
        }
    }
    return "true";
}

int main()
{
    char *a = isPalindromic(1011);
    printf("%s", a);
}