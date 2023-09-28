# include <stdio.h>

void Times_10(int *a){
    *a = *a*10;
}

int main()
{
    int a = 2;
    printf("The value of variable a is %d\n",a);
    Times_10(&a);
    printf("Now the value of variable a is %d\n ",a);
    
    return 0;
}