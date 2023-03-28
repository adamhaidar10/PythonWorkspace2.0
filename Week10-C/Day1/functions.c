#include <stdio.h>
#include "functionlibrary.h"

// declaration of the function
int square(int n);
int rf(int n);

// main function is traditionally the first function that appears in the file
int main()
{
    // printf("...%d\n", square(5));
    // printf("...%d\n", cube(6));

    int n;
    n = rf(99);

    return 0;
}

// implementation of the function declared above
int square(int n)
{
    int res;
    res = n * n;
    return res;
}



int rf(int n)
{
    int x;
    if (n >0)
    {
        printf("...%d\n", n);
        x = rf(n - 1);
    }
    else
    {
        printf("The end");
    }
}




