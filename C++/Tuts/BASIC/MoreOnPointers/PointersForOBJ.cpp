#include<iostream>
using namespace std;

class Complex{
    int real,imaginary;
    public:
        void getData(){
            cout<<"The Real Part is "<<real<<endl;
            cout<<"The imaginary Part is "<<imaginary<<endl;
        }
        void setData(int a , int b){
            real = a;
            imaginary = b;
        }
};

int main()
{
    Complex c1;
    Complex *ptr = &c1; // OP....
    (*ptr).setData(23,15);
    (*ptr).getData();

    Complex *p = new Complex;
    // (*p).setData(1,2);  // is exactly same as 
    p->setData(1,2);
    // (*p).getData(); // is exactly same as/////
    p->getData();
    Complex *p = new Complex[4]; // made an arr of Complex Numbers
     

    return 0;
}