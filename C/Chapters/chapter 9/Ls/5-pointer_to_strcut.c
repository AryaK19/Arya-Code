# include <stdio.h>
# include <string.h>

typedef struct employee // typedef to give a nick name to the strut like int 
{
    int code;
    float salary;
    char name[10];

} emp;

void show(emp emp1){
    printf("Code: %d\n",emp1.code);
    printf("Salary: %.3f\n",emp1.salary);
    printf("Name: %s\n",emp1.name);
}

int main()
{
    // struct employee e1;  we use to this 
    
    emp e1;
    emp *ptr;
    ptr = &e1;
    // (*ptr).code = 101; OR you can write :
    // ptr->code = 101; arrow operator means that add a dot ang give a star to the firt word...

    ptr->code = 101;
    ptr->salary = 101.101;
    strcpy(ptr->name, "Arya");
    show(e1);

    
    return 0;
    
}