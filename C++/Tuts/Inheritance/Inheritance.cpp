#include<iostream>
using namespace std;

// Base Class ......
class Employee{
    public:
        int id;
        float salary = 0.0;
        Employee(){}
        Employee(int i){
            id = i;
            salary = 34.0;
        }

};

//SYNTAX of Derived Class
/*
class {{derived-class-name}} : {{visibility-mode}} {{base-class-name}}
{
    class members/methods/etc.....
}

Notes 
1. Default visibility mode is private
2. Public Visisbility Mode : Public members of the base Class becomes Public memberes of derived class 
3. Private Visisbility Mode : Public members of the base Class becomes Private memberes of derived class 
4. Private members are never inherited
*/

// Creating a Programmer class derived from Employee Base Class 
class Programmer : Employee{
    public:
    Programmer(int inpId){
        id = inpId;
    }
    int languageCode = 9;
    void getData(){
        cout<<id<<endl;
    }
};

// Public Derived Class 

// class Programmer : public Employee{
//     public:
//     Programmer(int inpId){
//         id = inpId;
//     }
//     int languageCode = 9;
//     void getData(){
//         cout<<id<<endl;
//     }
// };



int main()
{
    Employee arya(1) ,  partha;
    cout<<arya.salary<<endl;
    cout<<partha.salary<<endl;
    Programmer skillF(3);
    cout<<skillF.languageCode<<endl;
    skillF.getData();
    // cout<<skillF.id<<endl; This will give error as the default id is Private

    return 0;
}