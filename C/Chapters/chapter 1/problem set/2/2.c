# include <stdio.h>

int main(){
    float cel;
    printf("Enter the value in celsius ");
    scanf("%f",&cel);

    float far = (cel*9/5)+32;

    printf("Enter the value of %f Celsius is %f Fahrenheit",cel,far);

    return 0;
}