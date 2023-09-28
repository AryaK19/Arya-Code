#include<iostream>
using namespace std;

class  complex{
    int a , b;
    public:
        void setNumber(int n1 , int n2){
            a = n1;
            b = n2;
        }
        // below line makes it so that the fuction (non class function can access privte parts
        friend complex sumComplex(complex o1,complex o2);
        void printNumber(){
            cout<<"Your number is "<<a<<" + "<<b<<"i"<<endl;
        }
};

complex sumComplex(complex o1,complex o2){
    complex o3;
    o3.setNumber(o1.a + o2.a , o2.b + o2.b);
    return o3;
}

int main()
{
    complex c1, c2 , sum;
    c1.setNumber(1,4);
    c1.printNumber();

    c2.setNumber(5,8);
    c2.printNumber();

    sum = sumComplex(c1,c2);
    sum.printNumber();

    return 0;
}

/* 
    Propertise of Friend Functions 
1.ot in scope of class
2.since it is not in the scope of the class ,it cannot be called from the object of the class .c1.sumComplex == Invalid
3. can be invokan with out the help of any object 
4.usually contains the objects as arguments a
5. cam be declared inside a public or a private section of the class 
6.It cannot assecs the member directly my thier name and need object to access any member
*/
