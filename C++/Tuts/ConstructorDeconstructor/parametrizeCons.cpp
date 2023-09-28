#include<iostream>
using namespace std;

// It is Just a constructor with argumenst

class Complex{
    int a,b;
    public:

        Complex(int x,int y); 
        void printNumber(){
        cout<<"Your Complex No is "<<a<<" + "<<b<<"i"<<endl;
    }
};
Complex :: Complex(int x,int y)// this is a paramitrized constructor
{
    a= x;
    b=y;
}



int main()
{
    //Implict call
    Complex c(4,5);
    c.printNumber();

    // Explicit call
    Complex a = Complex(7,0);
    
    a.printNumber();
    return 0;
}
