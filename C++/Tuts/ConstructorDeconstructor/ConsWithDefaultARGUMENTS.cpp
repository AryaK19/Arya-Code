#include<iostream>
using namespace std;

class Simple{
    int data1;
    int data2;
    public:
        Simple(int a, int b=9){
            data1 = a;
            data2 = b;
        }
        void printNumber()
    {
        cout << "Your Data is " << data1 <<" AND "<<data2<< endl;
    }
};

int main()
{
    Simple a(2,5);
    a.printNumber();
    Simple b(2,4);
    Simple c(2);
    c.printNumber();

    c = b;
    c.printNumber();

    return 0;
}