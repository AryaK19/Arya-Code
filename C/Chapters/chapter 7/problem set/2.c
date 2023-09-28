// # include <stdio.h>

// int main()
// {
//     int table[10],n=5;
//     for(int i = 0; i < 10; i++){
//         table[i] = n*(i+1);
//     }
//     for(int i = 0; i < 10; i++){
//         printf("5 x %d = %d\n",(i+1),table[i]);
//     }
    
//     return 0;
// }


#include<stdio.h>

int main()
{
    int table[10],n =5;
    for (int i=0 ; i <10;i++)
    {
        table[i]=n*(i+1);
        printf("%d x %d = %d\n",n,(i+1),table[i]);
    }

    return 0;
}