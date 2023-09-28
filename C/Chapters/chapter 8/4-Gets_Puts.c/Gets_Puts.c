# include <stdio.h>

int main()
{   // For using strings with spaces use gets()
    // puts() prints the string on the next line
    char s[34];
    printf("Enter Your Name: ");
    gets(s);
    puts(s);
    printf("Your Name is %s",s);
    
    
    return 0;
}