# include <stdio.h>

void printTable(int *table,int num){
    printf("The table of %d is :\n",num);
    for(int i = 0; i<10; i++ ){
        table[i] = num*(i+1);
    }
    for(int i = 0; i<10; i++ ){
        printf("%d x %d = %d\n",num,i+1,table[i]);
    }
    printf("\n\n");
}

int main()
{
    int table[3][10];
    printTable(table[0],2);
    printTable(table[1],7);
    printTable(table[2],9);
    
    return 0;
}