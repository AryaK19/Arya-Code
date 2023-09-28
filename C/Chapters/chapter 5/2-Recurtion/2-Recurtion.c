# include <stdio.h>

int Factorial(int x){
    if(x == 1 || x == 0){
        return 1;
    }
    else{
        return (x * Factorial(x - 1));
    }
}

int main()
{   
    int n = 0;
    int fac = Factorial(n);
    printf("Factorial of %d is %d\n",n,fac);
    
    return 0;
}