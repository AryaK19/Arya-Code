#include<iostream>
using namespace std;

class Number{
    int a = 0;
    public:
        Number(){}
        Number(int num){
            a = num;
        }
        // When No Copy constructor is found Compiler will add copy constructor to the class automaticly
        // so comenting the below line Would work too
        Number(Number &obj){
            cout<<"Copy Constructor Called"<<endl;
            a = obj.a;
        }
        void display(){
            cout<<"The Number for this object is "<<a<<endl;
        }
};

int main()
{
    Number x,y,z(45),z2;
    z.display();
    x.display();
    // if i want a var ,z1 exactly resumbel as z or x or  y ( By Copy Constructor)
    Number z1(z);
    
    z1.display(); // this will invoke copy constructor
    
    // z2 = z;// this will not invoke copy constructor

    Number z3 = z;
    z3.display();

    // so have to assing while the number is been made 

    return 0;
}