#include<iostream>
using namespace std;

// C++ can figure out which function to run :0 WOW
int add( int a ,int b){
    return a+b;
}
int add(int a,int b , int c){
    return a+b+c;
}

int main()
{
    cout<<"The Sum of 1, 2 is "<<add(1,2)<<endl;
    cout<<"The Sum of 1, 2,3 is "<<add(1,2,3)<<endl;

    return 0;
}