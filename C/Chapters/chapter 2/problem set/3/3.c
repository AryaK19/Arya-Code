// Step by step evaluation of 3*x/y-z+k

# include <stdio.h>

int main()
{
    int x = 2 , y = 3 , z = 3, k = 1 ;
    int result = 3 * x / y - z + k;
    printf("The value of result is (0) %d\n",result);
    int result_2 = (3 * x) / y - (z + k); 
    printf("The value of result is  %d\n",result_2);
    int result_3 = 3 *(x / y) - (z + k); 
    printf("The value of result is  %d\n",result_3);
    
    return 0;
}