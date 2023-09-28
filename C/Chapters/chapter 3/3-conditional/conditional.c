# include <stdio.h>

int main()
{
    int a;
    printf("Enter a \n");
    scanf("%d",&a);

    // one liner or ternary
    (a<5)? printf("%d is less than 5\n",a) : printf("%d is more than 5\n",a);
   
    if (a<5){printf("%d is less than 5\n",a);}
    else{printf("%d is more than 5\n",a);}
    
    
    return 0;
}

