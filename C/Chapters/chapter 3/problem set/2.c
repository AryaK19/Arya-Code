# include <stdio.h>

int main()
{
    int income;
    float tax = 0;

    printf("\n");
    printf("Enter your Income : ");
    scanf("%d",&income);
    printf("\n");

    if (250000 <= income && income < 500000){
        printf("The Income Tax is %f\n",tax + 0.05*(income - 250000));

    }
    else if (500000 <= income && income < 1000000){
        printf("The Income Tax is %f\n",tax + 0.2*(income - 500000));
    }
    else if (1000000 <= income){
        printf("The Income Tax is %f\n",tax + 0.3*(income - 1000000));
    }
    else{
        float tax = 0;
        printf("The Income Tax is %f\n",tax*income);

    }
    
    return 0;
}