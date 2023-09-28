# include <stdio.h>
# include <string.h>

struct employee
{
    int code;
    float salary;
    char name[10];

};
int main()
{
    struct employee Arya = {100 , 33344.344 , "Arya"};
    
    printf("Code: %d\n",Arya.code);
    printf("Salary: %.3f\n",Arya.salary);
    printf("Name: %s\n",Arya.name);
    
    
    return 0;
}