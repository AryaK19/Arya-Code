# include <stdio.h>

void swap(int *a ,int *b);
void wrong_swap(int a ,int b);


int main()
{
    int a = 3 ,b = 4;
    printf("The value of a and b is %d and %d\n",a,b);

    wrong_swap(a,b);// Will not work due to call by value  
    swap(&a,&b);// Will work bc of call by reference
    printf("Now the value of a and b is %d and %d\n",a,b);
    
    return 0;
}

void wrong_swap(int a ,int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
    
}

void swap(int *a,int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;



}