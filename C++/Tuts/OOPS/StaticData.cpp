#include <iostream>
using namespace std;
/*
Static is a keyword in C++ used to give special characteristics to an element.
Static elements are allocated storage only once in a program lifetime in static storage area.
And they have a scope till the program lifetime.
*/
class Employee
{
    int id;
    static int count;

public:
    void setData(void)
    {
        cout << "Enter The id of employee no " << count + 1 << endl;
        cin >> id;
        count++;
    }
    void getData(void)
    {
        cout << "The Id of employee No." << count << " is " << id << endl;
    }
    static void getCount(void){
        cout<<"The Value of Count is "<<count<<endl;
    }

};

int Employee ::count; // Defaut Value of Static variable is 0

int main()
{
    Employee arya;
    Employee partha;
    Employee rohandas;
    // arya.id =2 ; // cannot do this as private var
    arya.setData();
    arya.getData();
    Employee :: getCount();

    partha.setData();
    partha.getData();
    Employee :: getCount();

    rohandas.setData();
    rohandas.getData();
    Employee :: getCount();
    return 0;
}