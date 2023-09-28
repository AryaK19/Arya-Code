# include <stdio.h>
# include <string.h>

int main()
{   // It return 0 if both the strings are equal 
    // while comparing if the eskai values [(they are no.s assign to letters and no.s ,etc)]  of the first string is grater then it   will retrun 1 else -1

    char st1[45] = "Hello ";
    char *st2 = "ARYA";
    int val = strcmp(st1,st2);
    printf("The val is %d",val);

    
    return 0;
}