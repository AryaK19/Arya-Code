# include <stdio.h>
int sum(int a,int b);

int main()
{
    int a = 4,b = 8;

    printf("The value of %d + %d is %d\n",a,b,sum(a,b));
    
    return 0;
}

int sum(int a,int b){
    return a+b;
}