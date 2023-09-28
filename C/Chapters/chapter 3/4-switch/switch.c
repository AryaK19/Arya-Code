# include <stdio.h>

int main()
{   
    int rating;
    printf("Enter your rating (1-5)\n");
    scanf("%d",&rating);
    switch(rating){
        case 1:
            printf("*");
            break;
        case 2:
            printf("**");
            break;
        case 3:
            printf("***");
            break;
        case 4:
            printf("****");
            break;
        case 5:
            printf("*****");
            break;
        default:
            printf("invalid rating!!");


    }
    
    
    return 0;
}