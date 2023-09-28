# include <stdio.h>
# include <stdlib.h>

int main()
{
    int *ptr;
   
    //size of operator in C
    printf("The size of int on this pc is %d\n",sizeof(int));
    printf("The size of char on this pc is %d\n",sizeof(char));
    printf("The size of float on this pc is %d\n",sizeof(float));

    // malloc = memory allocation
    ptr = malloc(6 * 4); // 4 becase memory of a int is 4 bites
    ptr = (int *)malloc(6 * sizeof(int)); // as diff system has diff size..

    for(int i=0;i<6;i++)
    {
        printf("The value of %d element is: ",i+1);
        scanf("%d",&ptr[i]);
    }
    
    printf("\n");
    
    for(int i=0;i<6;i++)
    {
        printf("The value of %d element is: %d\n",i+1,ptr[i]);
    }
    
    return 0;
}