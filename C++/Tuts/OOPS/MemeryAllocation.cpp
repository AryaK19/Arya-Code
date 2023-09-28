#include<iostream>
using namespace std;

class Shop
{
    int itemId[100];
    int itemPrice[100];
    int counter;
    public:
        void initCounter(void){counter = 0;}
        void getPrice(void);
        void setPrice(int a);
        void displayPrice(void);
};

void Shop :: setPrice(int a){
    while(counter<a){
        cout<<"Enter Id of Your item no "<<counter+1<<endl;
        cin>>itemId[counter];
        cout<<"Enter Price of Your item no "<<counter+1<<endl;
        cin>>itemPrice[counter];
        counter++;
    };
}

void Shop :: displayPrice(void){
    for(int i = 0;i<counter;i++){
        cout<<"The Price of Item with Id "<<itemId[i]<<" is "<<itemPrice[i]<<endl;
    }
}

int main()
{
    Shop dukaan ;
    dukaan.initCounter();
    dukaan.setPrice(3);
    dukaan.displayPrice();

    return 0;
}