#include <stdio.h>

int main()
{ // This is not a best method to solve the prime no thing ......

    int n;
    int x = 0;
    printf("Enter the no.: ");
    scanf("%d", &n);

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            printf("%d is not a prime no.", n);
            x = 0;
            break;
        }
        else
        {
            x = 1;
        }
    }
    if(x == 1 || n==2 || n==1)
    {
        printf("%d is prime no.", n);
    }

    return 0;
}