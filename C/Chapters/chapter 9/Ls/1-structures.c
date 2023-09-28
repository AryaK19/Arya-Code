// its like a class in python 
// it is like int ,float,char,etc (see this are some structures which stores a value maybe int ,float,etc ...)
// just as you can make custum functions you can make costum Structures (class) 

# include <stdio.h>
# include <string.h>

// we made a new data type now we can use this (it wasn't this clear in python so thx c ...?  :) )

struct employee
{
    int code;
    char name[10];
    float salary;

};


int main()
{
    int a = 34;
    char b = 'b';
    float c = 34.44;
    struct employee e1;
    // e1.name = "Arya"; ----> won't work
    e1.code = 1119;
    e1.salary = 34.3433;
    strcpy(e1.name, "Arya");

    printf("%d\n",e1.code);
    printf("%.2f\n",e1.salary);
    printf("%s\n",e1.name);

    
    return 0;
}