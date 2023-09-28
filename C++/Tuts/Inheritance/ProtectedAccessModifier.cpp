#include<iostream>
using namespace std;

class Base{
    private:
        int b;
    protected: // it is just like private but can be inherited
        int a = 9;
};

/*
For a Protected member :
                            Public derivation       Private derivation      Protected derivation
    1. private members        Not Inherited           Not inherited             Not Inherited
    2. Public members         Public                  Private                   Protected
    3. Protected members      Protected               Private                   Protected
*/

class Derived : protected Base{
    public:
        int c =0;
        void printA(void){
            cout<<a<<endl;
        }
};

int main()
{
    Base b;
    Derived c;
    // cout<<b.a<<endl; // Won't Print as Protected (private)
    // cout<<b.b<<endl; // Ofcourse (private)
    cout<<c.c<<endl;
    c.printA(); //  Can Print As it is inherited as protected in derived class
    

    

    return 0;
}