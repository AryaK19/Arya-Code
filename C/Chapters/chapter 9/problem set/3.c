# include <stdio.h>

typedef struct complex
{
    int real ;
    int imaginary;
}comp;

void display(comp c,int i)
{
    printf("The Value of Real part of %d num is : %d\n" ,i,c.real);
    printf("The Value of Imaginary of %d num part is : %di\n\n" ,i,c.imaginary);
}
 

int main()
{
    comp cono[5];
    for(int i = 0 ; i < 5 ; i++)
    {
        printf("Enter the Value of Real part for %d num: ",i+1);
        scanf("%d",&cono[i].real);
        
        printf("Enter the Value of Imaginary part for %d num: ",i+1);
        scanf("%d",&cono[i].imaginary);
    }
    for(int i = 0 ; i < 5 ; i++)
    {
        display(cono[i],i);
    }
    
    return 0;
}