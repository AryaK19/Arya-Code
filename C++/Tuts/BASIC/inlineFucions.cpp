#include<iostream>
using namespace std;

// int product(int a , int b)
// {
//     return a*b;
// }

//this function is the fastest bacause it executes at compile time and is really fast , 
// it stores the value 
//but dont use it for like a big function

inline int product(int a , int b)  
{
    return a*b;
}



int main()
{
    int a,b;
    cout<<"Enter the value of a and b"<<endl;
    cin>>a>>b;
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);
    cout<<"The Product of a and b is "<<product(a,b);

    return 0;
}