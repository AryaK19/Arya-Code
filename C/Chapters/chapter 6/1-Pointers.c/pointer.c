# include <stdio.h>

int main()
{
    int i = 36;
    int *j = &i; // j will store the address of i
    printf("The value of i is %d\n",i);
    printf("The value of i is %d\n",*j);
    printf("The address of i is %d\n",&i);
    printf("The address of i is %d\n",j);
    printf("The value of j is %d\n",*(&j));
    
    // * is used to find the value of a given address
    // & is used to find the address of a given value

    //** is used to find the value of pointer to a pointer of the given address (:o) 

    return 0;
}