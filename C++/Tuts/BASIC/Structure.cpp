#include<iostream>
using namespace std;

typedef struct employee
{
    //DATA//
    int eId;
    char favChar;
    float salary;
}ep;

union money
{
    //DATA//

    //It only gives the Higest bit as the memory and does not givw three diff values of memory

    int rice;
    char car;
    float pounds;
};




int main()
{
    // ep Partha;
    // union money m1;
    // struct employee arya;
    // arya.eId = 1;
    // arya.favChar = 'A';
    // arya.salary = 10000000000000000;
    // cout<<arya.eId<<endl<<arya.favChar<<endl<<arya.salary<<endl;

    // // can only keep one value for one integers
    // m1.rice = 34;
    // m1.car = 'c';
    // cout<<m1.car<<endl; 

    enum meal{a,s,d,f}; // it gives 0,1,2,3,4... values if enum used 
    cout<<a<<endl<<s<<endl<<d<<endl<<f;
    meal m1 = a;
    cout<<endl<<m1;
    return 0;
}