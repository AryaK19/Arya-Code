# include <stdio.h>

void main(void)
{
    int i = 34;
    int *ptr = &i;
    printf("The Address of i is %u\n",ptr);
    ptr++; // it adds 4 as 4 is like a unit for a Number / Address......
    ptr = ptr + 1; // it adds 4 as 4 is like a unit for a Number / Address......

    // charecter is of 2 bite in my comp....
    
    printf("Now,The Address of i is %u\n",ptr);
    
    
}