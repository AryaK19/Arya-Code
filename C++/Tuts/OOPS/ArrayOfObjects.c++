#include <iostream>
using namespace std;

class Employee
{
    int id;
    int salary;

public:
    void setId(void)
    {
        salary = 122;
        cout << "Enter the id of employee ";
        cin >> id;
    }
    void getId(void)
    {

        cout << "The Id of the employee is " << id;
    }
};

int main()
{
    // Employee arya,vedant,partha,lovish;
    // arya.setId();
    // arya.getId();

    Employee fb[4];
    for (int i = 0; i < 4; i++)
    {
        fb[i].setId();
        fb[i].getId();
    }
    return 0;
}