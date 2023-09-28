# include <stdio.h>
# include <string.h>

int main()
{
    char str1[34];
    char str2[34];
    printf("Enter string 1: ");
    scanf("%s",&str1);

    fflush(stdin);
    printf("Enter string 2: ");
    scanf("%s",&str2);
    for(int i = 0; i < strlen(str1); i++){ 
        printf("%c",(str1[i]));
    }
    
        printf(" and ");
    for(int i = 0; i < strlen(str1); i++){ 
        printf("%c",(str2[i]));
    }
        printf("\n");

    
    int val = strcmp(str1,str2);

    if(val == 0){
        printf("The Strings are equal");
    }
    else{
        printf("The Strings are Unequal");
    }

    
    return 0;
}