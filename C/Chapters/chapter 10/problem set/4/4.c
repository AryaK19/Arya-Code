# include <stdio.h>
# include <string.h>

typedef struct employee
{
    char name[100];
    float salary;
}emp;


int main()
{
    emp e1;
    FILE *ptr;
    
    printf("Enter Your Name: ");
    gets(e1.name);
    printf("Enter Your Salary: ");
    scanf("%f",&e1.salary);

    ptr = fopen("Employee_Data.txt","w");
    fprintf(ptr,"%s , %.2f\n",e1.name,e1.salary);
    fclose(ptr);
    printf("Your Data Has Been Uploaded");
    
    return 0;
}