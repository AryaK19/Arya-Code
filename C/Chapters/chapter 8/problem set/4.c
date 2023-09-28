# include <stdio.h>

void decrypt(char *c){
    char *ptr = c;
    while(*ptr != '\0'){
        *ptr = *ptr - 1;
        ptr++;
    }
}

int main()
{
    char c[] = "Bszb";
    decrypt(c);
    printf("Decrypted String is : %s",c);
    
    return 0;
}