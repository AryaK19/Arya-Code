#include<iostream>
using namespace std;

int main()
{
    // Basic Example
    int a = 4;
    int* ptr = &a;

    cout<<"The Address of a is "<<(ptr)<<endl;
    
    // new Keyword
    int *p = new int(40);
    float *pt = new float(40.32);
    cout<<"The Value at Adress p is "<<*(p)<<endl;
    cout<<"The Value at Adress pt is "<<*(pt)<<endl;

    int* arr = new int[3];
    arr[0] = 10;
    *(arr+1) = 20;
    arr[2] = 30;
    cout<<"The Value at Adress arr[0] is "<<(arr[0])<<endl;
    cout<<"The Value at Adress arr[1] is "<<(arr[1])<<endl;
    cout<<"The Value at Adress arr[2] is "<<(arr[2])<<endl;
    cout<<endl;

    // delete Operator
    delete arr;
    delete[] arr; // delete a whole arr (just removes so that we can use the var or arr again)
    cout<<"The Value at Adress arr[0] is "<<(arr[0])<<endl;
    cout<<"The Value at Adress arr[1] is "<<(arr[1])<<endl;
    cout<<"The Value at Adress arr[2] is "<<(arr[2])<<endl;

    return 0;
}