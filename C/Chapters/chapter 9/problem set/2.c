# include <stdio.h>

typedef struct vector
{
    float x ;
    float y ;
}vec;

vec sumVec(vec *v1 , vec *v2)
{
    vec resultant;
    resultant.x = (*v1).x + (*v2).x;
    resultant.y = (*v1).y + (*v2).y;
    return resultant;
}

int main()
{
    vec v1;
    vec *ptr1;
    ptr1 = &v1;
    v1.x = 16;
    v1.y = 13;

    vec v2;
    vec *ptr2;
    ptr2 = &v2;
    v2.x = 12;
    v2.y = -34;

    vec v3;
    v3.x = (sumVec(&v1,&v2)).x;
    v3.y = (sumVec(&v1,&v2)).y;
    
    printf("The sum of the Two vestors is : vec(%.3f,%.3f)\n",v3.x,v3.y);
    
    return 0;
}