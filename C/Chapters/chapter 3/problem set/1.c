# include <stdio.h>

int main()
{
    int maths,physics,chemistry;
    printf("Enter Marks :\n");
    printf("Maths : ");
    scanf("%d", &maths);
    printf("Physics : ");
    scanf("%d", &physics);
    printf("Chemistry : ");
    scanf("%d", &chemistry);

    if ((maths + physics + chemistry) > 120 && ((maths > 33) || (physics > 33) || (chemistry > 33) )){
        printf("Your Have Passed Away form Devta collage!!");
    }
    else {
        printf("You Failed lol......");
    }
    
    return 0;
}