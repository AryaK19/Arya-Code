# include <stdio.h>

int main()
{   int n;
    int sum = 0;
    printf("Enter a Number: ");
    scanf("%d",&n);
    for(int i = 1; i <= n; i++){
        sum += i;
    }

    printf("The Sum of First %d Natural no. is %d",n,sum);
    
    return 0;
}