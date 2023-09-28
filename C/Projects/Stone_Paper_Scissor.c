#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char choose()
{
    int num;
    srand(time(0));
    num = rand() % 3 + 1;

    if (num == 1)
    {
        return 'r';
    }
    else if (num == 2)
    {
        return 'p';
    }
    else if (num == 3)
    {
        return 's';
    }
}

void rules(char you, char comp, int *n)
{

    if (you == comp)
    {
        printf("It's a Tie\n");
    }
    else if (you == 'r' && comp == 's')
    {
        printf("You Won!\n");
        *n = 1;
    }
    else if (you == 'p' && comp == 'r')
    {
        printf("You Won!\n");
        *n = 1;
    }
    else if (you == 's' && comp == 'p')
    {
        printf("You Won!\n");
        *n = 1;
    }
    else
    {
        printf("You Lost...\n");
        *n = 0;
    }
}

int main()
{
    char you, comp;
    int n, run = 1;

    printf("Enter Your Choise(r/p/s): ");
    scanf("%c", &you);
    
    comp = choose();
    printf("Computer Choose: %c\n", comp);
    rules(you, comp, &n);

    return 0;
}