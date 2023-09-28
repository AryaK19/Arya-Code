#include<iostream>
using namespace std;

class Complex{
    int a,b;
    public:
        // creating a Constructor
        // Contructor is a speacial member function with the same name as of the class.
        // It is used to initialize the object of its class
        //It is automatically invoked where a object is created 

        Complex(void); // constructor declaration
        void printNumber(){
        cout<<"Your Complex No is "<<a<<" + "<<b<<"i"<<endl;
    }
};

Complex :: Complex(void)// this is a defult constructor
{
    a= 10;
    b=0;
}

int main()
{
    
    Complex c ;
    c.printNumber();
    return 0;
}

/* Characteristics of Constructors 

1. It should be declared in the public section of the class
2. Do not have retrun types 
3. It can have default arguments
4. We cannot address to there address




*/