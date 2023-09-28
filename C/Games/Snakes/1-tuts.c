// kbhit(),rand()
# include <stdio.h>
# include <stdlib.h>
# include <conio.h>

// when key is hit the function returns 1 or else 0 ...

int main()
{
    char ch;
    while(1)
    {
        
        if(kbhit())
        {   
            ch = getch();
            printf("%c",ch); 
        }
        
    }
    
    return 0;
}
