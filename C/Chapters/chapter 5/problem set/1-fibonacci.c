#include <stdio.h>

// 0 1 1 2 3 5 8 13 21 35......(adding previous no.s)

int fibonacci(int n)
{
    int ans;
    if (n == 1)
    {
        return 0;
    }
    else if (n == 2)
    {
        return 1;
    }
    else
    {
        ans = fibonacci(n - 1) + fibonacci(n - 2);
        return ans;
    }
}

int main()
{
    int n = 5, fibo;
    fibo = fibonacci(n);
    printf("%dth Number in Fibonacci sequence is %d\n", n, fibo);
    return 0;
}