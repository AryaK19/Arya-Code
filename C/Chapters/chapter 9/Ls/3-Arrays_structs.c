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
    struct employee facebook[100];

    facebook[0].code = 1119;
    facebook[0].salary = 100.45;
    strcpy(facebook[0].name, "ARYA");
    
    facebook[1].code = 1123119;
    facebook[1].salary = 130.45;
    strcpy(facebook[1].name, "Sumit");
    
    facebook[2].code = 1123119;
    facebook[2].salary = 10023.45;
    strcpy(facebook[2].name, "laksjajsnu");
    
    return 0;
}