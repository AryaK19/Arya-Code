# include <stdio.h>
# include <stdlib.h>

int main()
{
    int *ptr,n;
    printf("Enter no. of Integers:\n");
    scanf("%d",&n);
   
    // calloc gives all the element a value that is 0 (and then we can change that ....)
    ptr = (int *)calloc(n , sizeof(int)); // as diff system has diff size..

    for(int i=0;i<n;i++)
    {
        printf("The value of %d element is: ",i+1);
        scanf("%d",&ptr[i]);
    }
    
    printf("\n");
    
    for(int i=0;i<n;i++)
    {
        printf("The value of %d element is: %d\n",i+1,ptr[i]);
    }
    
    return 0;
}