# include <stdio.h>

int main()
{
    FILE *ptr;
    int num,num1;
    ptr = fopen("sample.txt","r");
    fscanf(ptr,"%d",&num);
    fscanf(ptr,"%d",&num1);
    
    fclose(ptr);

    printf("%d ",num);
    printf("%d ",num1);
    
    return 0;
}