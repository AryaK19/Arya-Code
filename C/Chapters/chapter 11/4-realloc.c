# include <stdio.h>
# include <stdlib.h>

int main()
{
    int *ptr;
    
    ptr = (int *)malloc(6 * sizeof(int)); 

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
    
    
    // reallocate ptr using realloc()....(this helps to relocate or re make the operator space or to change the operator space)

    // this all is to reduce memory usage  

    ptr = realloc(ptr ,10 * sizeof(int));

    for(int i=0;i<10;i++)
    {
        printf("The value of %d element is: ",i+1);
        scanf("%d",&ptr[i]);
    }
    
    printf("\n");
    
    for(int i=0;i<10;i++)
    {
        printf("The value of %d element is: %d\n",i+1,ptr[i]);
    }


    return 0;
}