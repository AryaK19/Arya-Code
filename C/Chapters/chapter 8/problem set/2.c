# include <stdio.h>
# include <string.h>

void slice(char *st ,int m, int n){
    
    int i = 0;
    while(m+i<=n){
        st[i] = st[i+ m -1];
        i++;
    }
    st[i] = '\0';
    
    
}

int main()
{
    char st[] = "AryaKadam";
    
    slice(st, 2, 4);
    printf("%s",st);
    
    return 0;
}