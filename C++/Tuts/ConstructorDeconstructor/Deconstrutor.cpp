#include<iostream>
using namespace std;

// Destructor never Takes arguments nor does it returns any value
int count = 0;
class num{
    int a = 667;
    friend int main();
    public:
        num(){
            count++;
            cout<<"This is the time when the Construtor is Called For Objects number "<<count<<endl;
        }
        // ~num(){
        //     cout<<"This is the time when the Deconstrutor is Called For Objects number "<<count<<endl;
        //     count--;

        // }
};
int main()
{
    cout<<"We are in the Main Function"<<endl;
    cout<<"Creating First Object n1"<<endl;
    num n1;
    {
        cout<<"Entering The Block"<<endl;
        cout<<"Creating two more objects"<<endl;
        num n2,n3;
        cout<<"Exiting The Block"<<endl;
    }    //// when the block is exited the var (class ) is deconstructed automaticly that is the varialble is removed out of the block
    cout<<"Back to Main"<<endl;
    cout<<n1.a<<endl;

    return 0;
}