#include <stdio.h>

int main()
{
    int a = 0;
    while (a < 100)
    {
        // printf("Hello\n");
        a += 1;
        if (a % 2 == 0)
        {
            printf("%d\n", a);
        }
    }

    return 0;
}