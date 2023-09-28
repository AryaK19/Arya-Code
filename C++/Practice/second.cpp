#include<iostream>
using namespace std;

void swap(int *a , int *b)
{
    int sum = *a;
    *a=*b;
    *b=sum;
    
}

int main()
{
    int a = 2,b=3;
    swap(&a,&b);
    cout<<a<<b<<endl;
    cout<<a<<b;
    return 0;
}