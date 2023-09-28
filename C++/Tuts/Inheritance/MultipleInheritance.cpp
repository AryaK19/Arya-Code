#include<iostream>
using namespace std;

/* 
Syntax fro Inheriting in multiple inheritance

class DerivedC :visibility -mode base1 , visibility -mode base2 
{
    Class body of class "DerivedC" 
};
*/

class Base1{
    protected:
        int base1int;
    public:
        void set_base1int(int b){
            base1int = b;
        }
};

class Base2{
    protected:
        int base2int;
    public:
        void set_base2int(int b){
            base2int = b;
        }
};

class Derived : public Base1,public Base2
{
    public:
        void show(){
            cout<<"The value of Base1 is "<<base1int<<endl;          
            cout<<"The value of Base2 is "<<base2int<<endl;          
            cout<<"The Sum of these values is "<<base1int + base2int<<endl;          
        }
};

// The inherited Derived Class will Look some thing like this
/*
Data Members :
    base1int -- protected
    base2int -- protected
    base2int -- protected
Members Functions:
    set_base1int -- public
    set_base2int -- public
    show         -- public

*/
int main()
{
    Derived arya;
    arya.set_base1int(2);
    arya.set_base2int(9);
    arya.show();

    return 0;
}