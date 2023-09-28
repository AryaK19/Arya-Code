#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

int width = 50, height = 24, gameNotOver;

int x, y, fruitx, fruity, score;

int flag;
int tailx[50],taily[50];
int countTail = 0;

void setup()
{
    gameNotOver = 1;
    x = width / 2;
    y = height / 2;
    srand(time(0));
    fruitx = rand() % (width - 2) + 1;
    fruity = rand() % (height - 2) + 1;
    score = 0;
}

void draw()
{
    system("cls");
    printf("SCORE : %d\n", score);
    for (int i = 0; i < height; i++)
    {
        printf("Q");
        for (int j = 0; j < (width - 2); j++)
        {
            if (i > 0 && i < (height - 1))
            {
                if (i == y && j == (x - 1))
                {
                    printf("O");
                }
                else if (i == fruity && j == fruitx)
                {
                    printf("@");
                }
                else
                {
                    int ch = 0;
                    for(int k=0;k<countTail;k++)
                    {
                        if(i == taily[k] && j == tailx[k])
                        {
                            printf("o");
                            ch = 1;
                        }
                    }
                    if(ch==0)
                    {
                        printf(" ");
                    }
                }

            }
            else
            {
                printf("Q");
            }
        }
        printf("Q\n");
    }
    printf("Enter x to Quit");
}

void input()
{
    if (kbhit())
    {
        flag = 5;
        switch (getch())
        {
        case 'w':
            flag = 1;
            break;
        case 'a':
            flag = 2;
            break;
        case 's':
            flag = 3;
            break;
        case 'd':
            flag = 4;
            break;
        case 'x':
            gameNotOver = 0;
            break;
        }
    }
}



void makeLogic()
{

    int prevx=tailx[0];
    int prevy=taily[0];
    int prev2x,prev2y;
    tailx[0]=x-1;
    taily[0]=y;

    for(int i=1; i<countTail;i++)
    {
        prev2x = tailx[i];
        prev2y = taily[i];
        tailx[i] = prevx; 
        taily[i] = prevy; 
        prevx = prev2x;
        prevy = prev2y;
    }

    switch (flag)
    {
    case 1:
        y--;
        break;
    case 2:
        x--;
        break;
    case 3:
        y++;
        break;
    case 4:
        x++;
        break;
    case 5:
        break;
    default:
        break;
    }
    if ((x - 1) == fruitx && y == fruity)
    {
        score+=10;
        srand(time(0));
        fruitx = rand() % (width - 2) + 1;
        fruity = rand() % (height - 2) + 1;
        countTail++;
    }
    else if (x-1 < 0 || y < 0 || x > width || y > height-1)
    {
        gameNotOver = 0;
    }
    for(int i = 0;i<countTail;i++)
    {
        if(x-1 == tailx[i] && y == taily[i])
        {
            gameNotOver = 0;
        }
    }
}

int main()
{
    setup();
    while (gameNotOver)
    {
        draw();
        input();
        makeLogic();
        
    }

    return 0;
}