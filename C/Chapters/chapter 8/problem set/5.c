# include <stdio.h>

void hmt(char *str ,char letter){
    char *ptr = str;
    int times = 0;
    while(*ptr != '\0'){
        if (*ptr == letter){
            times++;
        }
        ptr++;
    }
    printf("The Letter '%c' is Repeated %d times",letter,times);
}
int main()
{
    char str[] = "AryaKadam";
    char letter = 'a';
    hmt(str,letter);
    
    return 0;
}