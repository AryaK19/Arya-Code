#include<iostream>
#include<math.h>



using namespace std;
/*

Create 2 classes:
    1. SimpleCalculater - Takes input of 2 numbers using utility function and performs +,-,*,/
    2. ScientificCalculator  - Takes input of 2 numbers using utility function and performs any four scientific operation of your choice

    Create another class Hybridcalculator and inherite using this 2 class
    Q1. What type of Inheritance are you using?
    Q2. Which mode of Inheritance are you using? 
    Q3. Create an object of HybrideCalculator and display result of simple and simple and scientific calculator.
    Q4. How is Code reusability implemented?

*/ 
class SimpleCalculator{
    int a,b;
    
    public:
    int operation;
        void takeInpt(void){
            cout<<"Enter 2 Values to Calculate : "<<endl;
            cin>>a>>b;
            cout<<"What You Want To Do \n1.Add \n2.Subtract \n3.Multiply \n4.Divide "<<endl;
            cin>>operation;
            run(operation);
        }
    
        int add(int a ,int b){
            return a+b;
        }
        
        int subtract(int a ,int b){
            return a-b;
        }
        
        int multiply(int a ,int b){
            return a*b;
        }
        
        int divide(int a ,int b){
            return a/b;
        }
        
        void run(int);
        
};

void SimpleCalculator::run(int operation)
{
    if (operation == 1){cout<<a<<" + "<<b<<" = "<<add(a,b)<<endl;};
    if (operation == 2){cout<<a<<" - "<<b<<" = "<<subtract(a,b)<<endl;};
    if (operation == 3){cout<<a<<" x "<<b<<" = "<<multiply(a,b)<<endl;};
    if (operation == 4){cout<<a<<" / "<<b<<" = "<<divide(a,b)<<endl;};
}

class ScintificCalculator{
    int inpt;
    
    
    public:
    int operation;
        float Operation(){
            cout<<"Enter a Number(x) To Calculate : ";
            cin>>inpt;
            cout<<"Which Function To perform [sin,cos,tan,sqrt]: ";
            cin>>operation;
            
            if (operation == 1){
                
                return sin(inpt);
            }
            if (operation == 2){
                return cos(inpt);
            }
            if (operation == 3){
                return tan(inpt);
            }
            if (operation == 4){
                return sqrt(inpt);
            }
            
        }  

};


int main()
{
    SimpleCalculator cal;
    cal.takeInpt();
    return 0;
}