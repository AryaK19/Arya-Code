#include<iostream>
using namespace std;

void wrongswap(int a,int b)
{
    int temp = a;
    a=b;
    b=temp;
}
void swap(int *a,int *b)
{
    int temp = *a;
    *a=*b;
    *b=temp;
}
void swapByReference(int &a,int &b)
{
    int temp = a;
    a=b;
    b=temp;
}

int main()
{
    int a = 3 , b= 5;
    cout<<a<<b<<endl;
    // swap(&a,&b);
    swapByReference(a,b);
    cout<<a<<b<<endl;

    return 0;
}