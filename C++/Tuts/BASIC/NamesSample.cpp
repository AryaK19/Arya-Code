#include<iostream>
// using namespace std;  this is a names space ....

namespace Sample{
    int a;
    int sum(int x, int y){
        return(x+y);

    }
}
int sum(int x, int y){
        return(x+y);
}

int main()
{
    Sample :: a = 5;
    int x = Sample :: sum(5,9);
    std :: cout<<"The Sum is "<<x;  // if the using namespace std is not used we have to write this....
    int y = sum(2,3);
    std :: cout<<y;
    // so to differensiate it from a function namespace is used

    return 0;
}