#include<iostream>
using namespace std;
int sum(int a ,int b); // Fuction Prototype (tell at start the function is there in end or can write the function it self in the start...,,see the g() Fuction)
int sum(int,int); // Fuction Prototype (tell at start the function is there)

// Function only takes value not the actual variable,so cant change directly

int main()
{
    cout<<sum(1,3);
    g();
    return 0;
}



int sum(int a ,int b)
{
    int sum = a+ b ;
    return sum; 
}
void g()
{
    cout<<"HI";
}