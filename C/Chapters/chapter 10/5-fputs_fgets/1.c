# include <stdio.h>

int main()
{  //  for reading a file lette  by letter 

    FILE *ptr,*ptr2;
    ptr = fopen("sample.txt","r");
    
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));
    printf("%c",fgetc(ptr));


    ptr2 = fopen("put.txt","w");
    fputc('c',ptr2);
    fclose(ptr2);
    fclose(ptr);

    return 0;
}