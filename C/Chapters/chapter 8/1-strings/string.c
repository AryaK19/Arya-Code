# include <stdio.h>

int main()
{
    // char str[] = {"A","R","Y","A","\0"};
    char str[] = "ARYA";
    char *ptr = str;
    while (*ptr !='\0')
    {
        printf("%c \n",*ptr);
        // printf("%u",ptr);
        ptr++;
    }
    

    
    return 0;
}