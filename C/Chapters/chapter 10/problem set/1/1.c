# include <stdio.h>

int main()
{
    FILE *ptr;
    int a,c,b;
    
    ptr = fopen("s1.txt","r");
    
    fscanf(ptr,"%d %d %d",&a,&b,&c);
    printf("%d ",a);
    printf("%d ",b);
    printf("%d",c);
    
    return 0;
}