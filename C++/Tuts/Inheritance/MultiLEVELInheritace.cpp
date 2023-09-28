#include<iostream>
using namespace std;

class Student{
    protected:
        int roll_number;
    public:
        void set_RollNumber(int);
        void get_RollNumber(void);

};

void Student :: set_RollNumber(int r){
    roll_number = r;
}

void Student :: get_RollNumber(void){
    cout<<"The roll Number is "<<roll_number<<endl;;
}

class Exam : public Student{
    protected:
        float maths;
        float physics;
    public:
        void set_marks(float,float);
        void get_marks(void);
};

void Exam :: set_marks(float m1 , float m2){
    maths = m1;
    physics = m2;
}
void Exam :: get_marks(){
    cout<<"The marks Obtained in Maths are : "<<maths<<endl;
    cout<<"The marks Obtained in Physics are : "<<physics<<endl;
    
}

class Result : public Exam{
    float percentage;
    public:
        void display_result(){
            get_RollNumber();
            get_marks();
            cout<<"Your result is "<<(maths+physics)/2<<"%"<<endl;
        }
};

int main()
{
    /*
    Notes:
        If we are inheriting B from A and C from B :[ A ---> B ---> C ]
        1. A is the Class for B and B is the base class for c
        2. A ---> B ---> C  is called Multilevel inheritance and it is the inheritance Path
    */
    Result arya;
    arya.set_RollNumber(43);
    arya.set_marks(90.0,94.4);
    arya.display_result(); 

    return 0;
}