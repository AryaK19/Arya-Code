#include<iostream>
using namespace std;

class Employee
{
    private:
        int a,b,c;
    public:
        int d,e;

        void setData(int a,int b,int c);
        void getData(){
            cout<<"THE Value of a b c is "<<a<<b<<c;
        }
};

void Employee ::setData(int a1 ,int b1,int c1)
{
    a = a1;
    b = b1;
    c = c1;
}

int main()
{
    Employee arya;
    arya.d = 34;
    arya.e = 89;
    arya.setData(1,2,3);
    arya.getData();
    // cout<<arya.a;  //This will show error

    return 0;
}