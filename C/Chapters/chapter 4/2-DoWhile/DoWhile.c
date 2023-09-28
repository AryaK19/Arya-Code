# include <stdio.h>

int main()
{
    int i = 0;
    int no;
    printf("Enter the Number: ");
    scanf("%d",&no);

    do{
        i++;
        printf("%d\n",i);
    }while(i < no);
    
    // It checks after running the program(it also runs for at least 1 time)

    // and while loops checks first 
    
    return 0;
}