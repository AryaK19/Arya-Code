# include <stdio.h>
# include <stdlib.h>

int main()
{
    int *ptr;
    int *ptr2;

    // free() helps to maintain memory as the  memory will increace in each loop if free in not there ......

    ptr = (int *)malloc(6 * sizeof(int));
    for(int i=0;i<600;i++)
    {
        ptr2 = (int *)malloc(60000 * sizeof(int));
        printf("The value of %d element is: ",i+1);
        scanf("%d",&ptr[i]);
        free(ptr2);
    }
    
    printf("\n");
    
    for(int i=0;i<6;i++)
    {
        printf("The value of %d element is: %d\n",i+1,ptr[i]);
    }
    
    return 0;
}
