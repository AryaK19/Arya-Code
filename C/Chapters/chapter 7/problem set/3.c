# include <stdio.h>

void reverse(int *arr,int len){
    for (int i = 0; i < (len/2); i++)
    { 
        int temp = arr[i];
        arr[i] = arr[len-i-1];
        arr[len-i-1] = temp;
    }
    
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7},len = 7;
    reverse(arr,len);
    for (int i = 0; i < len; i++)
    {
        printf("%d\n",arr[i]);
    }
    
    
    return 0;
}