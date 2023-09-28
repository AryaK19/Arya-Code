# include <stdio.h>

int main()
{
    int a, b;

    printf("Enter the value of a \n");
    scanf("%d", &a); // what type of object you want and where

    printf("Enter the value of b \n");
    scanf("%d", &b); // what type of object you want and where

    printf("The Sum of %d and %d is %d",a,b,a+b);

    return 0;
}