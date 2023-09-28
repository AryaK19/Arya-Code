#include<iostream>
using namespace std;

int main()
{
    int a = 3;
    int &d = a;
    cout<<++d<<endl;
    cout<<a;

    return 0;
}