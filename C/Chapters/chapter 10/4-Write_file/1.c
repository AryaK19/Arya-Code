# include <stdio.h>

int main()
{
    FILE *ptr;
    int num = 23;
    ptr = fopen("GENERETED.txt","w");
    fprintf(ptr,"%d",num);
    fprintf(ptr," Hi my name is arya\n");
    fclose(ptr);
    
    return 0;
}