# include <stdio.h>

typedef struct date
{
    int year;
    int month;
    int date;
}date;


int main()
{
    date date;
    printf("Enter the Year :");
    scanf("%d",&date.year);
    printf("Enter the Month :");
    scanf("%d",&date.month);
    printf("Enter the Date :");
    scanf("%d",&date.date);
    
    printf("DATE : %d/%d/%d",date.date,date.month,date.year);
    
    return 0;
}