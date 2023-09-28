# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int main()
{
    int guess,range,num,run = 1,plays = 1;
    printf("Enter Range (1 - x): ");
    scanf("%d",&range);
    printf("\n");
    srand(time(0));
    num = rand() % range + 1 ; // Awesome Maths 

    while(run){

        printf("Enter Your Guess: ");
        scanf("%d",&guess);

        if(guess > num){
            printf("Try a Smaller Number....\n\n");
            plays++;
            continue;
        }
        else if(guess < num){
            printf("Try a Bigger Number....\n\n");
            plays++;
            continue;

        }
        else{
            printf("It is Correct!!!\n");
            if(plays == 1){
            printf("WOW! You got it in %d Try!!!!",plays);
            }
            else{
            printf("You got it in %d Tries",plays);
            }
            break;
        }
        

    }
    
    return 0;
}