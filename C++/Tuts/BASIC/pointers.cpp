#include<iostream>
using namespace std;
int main()
{
    int a = 3;
    int *b ; //  OR  int *b=&a
    b= &a;
    cout<<"The Address of a is : "<<&a<<endl;
    cout<<"The Address of a is : "<<b<<endl;
    cout<<"The Value at Address of a is : "<<*b<<endl;
    // * Dereference Operator
    // & Address of Operator
    cout<<endl;

    // Pointers Arrays
    int marks[4] = {1,2,3,4};
    int *p = marks ;
    cout<<*(p++)<<endl;
    cout<<*p<<endl;
    cout<<"The Value marks[0] : "<<*p<<endl;
    cout<<"The Value marks[1] : "<<*(p+1)<<endl;
    cout<<"The Value marks[2] : "<<*(p+2)<<endl;
    cout<<"The Value marks[3] : "<<*(p+3)<<endl;


    return 0;
}