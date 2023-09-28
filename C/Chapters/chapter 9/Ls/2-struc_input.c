# include <stdio.h>
# include <string.h>

struct employee
{
    int code;
    char name[10];
    float salary;

};


int main()
{
    struct employee e1;
    e1.code;
    e1.name;
    e1.salary;

    printf("Enter Code: ");
    scanf("%d",&e1.code);
    
    printf("Enter Name: ");
    scanf("%s",e1.name);
    
    printf("Enter Salary: ");
    scanf("%f",&e1.salary);
    
    printf("Code: %d\n",e1.code);
    printf("Name: %s\n",e1.name);
    printf("Salary: %.3f\n",e1.salary);
    return 0;
}