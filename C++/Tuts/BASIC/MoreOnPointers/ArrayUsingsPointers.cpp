#include<iostream>
using namespace std;

class ShopItem{
    int id;
    float price;
    public:
        void setData(int a,float b){
            id = a;
            price = b;
        }
        void getData(void){
            cout<<"Id Of This Item is "<<id<<endl;
            cout<<"Price Of This Item is "<<price<<endl;
        }
};

int main(){
    int size = 3;
    ShopItem *ptr = new ShopItem[size];
    ShopItem *ptrTemp = ptr;
    int p;
    float q;
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter Id and price of item "<< i+1<<endl;
        cin>>p>>q;
        // (*ptr).setData(p, q);
        ptr->setData(p, q);
        ptr++;
    }

    for (int i = 0; i < size; i++)
    {
        cout<<"Item number: "<<i+1<<endl;
        ptrTemp->getData();
        ptrTemp++;
    }
    
    
    return 0;
}
