#include <iostream>
using namespace std;

int power(int p, int q, int c = 1, int a = 1)
{

    if (c == 1)
    {
        a = p;
    }
    if (c != q)
    {
        p = p * a;
        c++;
        return power(p, q, c, a);
    }

    else
    {
        return p;
    }
}

int main()
{
    cout << power(2, 5);

    return 0;
}