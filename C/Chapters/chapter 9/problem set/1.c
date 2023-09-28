# include <stdio.h>

typedef struct vector
{
    float x ;
    float y ;
}vec;

int main()
{
    vec velocity;
    velocity.x = 12.3;
    velocity.y = 12.3;
    printf("X dim is %f\n",velocity.x);
    printf("Y dim is %f",velocity.y);
    
    return 0;
}