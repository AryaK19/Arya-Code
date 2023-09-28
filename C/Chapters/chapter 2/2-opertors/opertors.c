# include <stdio.h>

int main()
{
    int x = 2;
    int y = 3;
    printf("The value of 3x - 8y is %d",3*x-8*y);
    printf("The value of  8y / 3x  is %d",8 * y / 3 * x); // (it calculates line by line omggggggg nice....) == 16 not == 4

    printf("The value of  8y / 3x  is %d",(8 * y) / (3 * x)); // now == 4

    
    return 0;
}