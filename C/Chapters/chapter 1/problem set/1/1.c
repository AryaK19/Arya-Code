# include <stdio.h>

int main()
{

    float length,breath;
    printf("Enter the Length of the Rectangle ");
    scanf("%f",&length);

    printf("Enter the Breath of the Rectangle ");
    scanf("%f",&breath);

    printf("The Area of the Rectangle with Length %f and Breath %f is  %f",length,breath,length*breath);

    return 0;
}
