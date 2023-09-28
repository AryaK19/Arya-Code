//(<=,>=,==,!=,<,>)

//to asign aything true in C give it a non zero number(if a = 50)that is if a is true (see not a '==' 5 ) 

# include <stdio.h>

int main()
{
    int age;
    int vipPass = 0;
    vipPass = 1;

    printf("Enter your age\n");
    scanf("%d",&age);
    if((age<=70 && age>=18) ||  vipPass == 1){
        printf("You are above 18 and below 70 , you can Drive\n");
    }
    else if (age == 3){
        printf("You can,t Drive\n");
        printf("Enter a name of a per son iusiui");
        
    }
    
    return 0;
}



