#include <stdio.h>

void table_txt(int n)
{
    FILE *ptr;
    char file_name[100];
    char table[100];

    sprintf(file_name, "Table_of_%d.txt", n);

    ptr = fopen(file_name, "r");
    

    if (ptr != NULL)
    {
        printf("The Table already Exites...");
    }
    else
    {
        ptr = fopen(file_name, "w");
        for (int i = 1; i <= 10; i++)
        {
            if(i!=10)
            {
            fprintf(ptr, "%d x %d = %d\n", n, i, n * i);
            }
            else
            {
            fprintf(ptr, "%d x %d = %d", n, i, n * i);
            }
        }
        printf("The Table Made");
    }

    fclose(ptr);
}

int main()
{
    int n;
    printf("Table of: ");
    scanf("%d", &n);

    table_txt(n);

    return 0;
}