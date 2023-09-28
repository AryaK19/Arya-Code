#include<iostream>
using namespace std;

bool prime(int n){
    if (n==1){
        return true;
    }
    else if (n==2){
        return true;
    }
    else {
    for(int i =2;i<n;i++){
        
        if(n%i == 0){
            return false;
            break;
        }
        if (n%i !=0){
            
            return true;
        }
    }
    }
}

int main()
{
    int n;
    cin>>n;
    cout<<"Is prime : "<<prime(n);

    return 0;
}