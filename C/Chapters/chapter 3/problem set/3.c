# include <stdio.h>

int main()
{
    // 92 - 122 = a - z (ASCII VALUES)
    char ch;
    printf("Enter the character:\n");
    scanf("%c",&ch);
    if(ch <= 122 && ch >=92){
        printf("The Letter is a LowerCase Letter");
    }
    else{
        printf("The Letter is a UpperCase Letter");
    }
    return 0;
}