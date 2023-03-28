#include <stdio.h>

int main()
{
    int n = 4;

    // normal if statement
    /*
    if (n == 5)
    {
        printf("Yes\n");
    }
    else if (n == 3)
    {
        printf("No\n");        
    }
    else
    {
        printf("Maybe\n");        
    }
    */


    /*
    switch (n)
    {
        case 3:
            printf("Three\n");
            break;
        case 4:
            printf("Four\n");
            break;
        case 5:
            printf("Five\n");
            break;
        default:
            printf("None of the above\n");
    }
    */


    // for loop
    /*
    for (int i = 1; i <= 10; i++)
    {
        printf("...%d\n", i);
    }
    */

    // while loop
    // condition is checked at the beginning of the loop
    // that might mean that the loop is never executed
    // (if the expression is already false at the beginning)
    /*
    n = 10;
    while (n > 0)
    {
        printf("...%d\n", n);
        n--;
    }
    */

    // do loop
    // always executed at least once
    // the expression is checked after the loop has executed
    n = 10;
    do
    {
        printf("...%d\n", n);
        n--;
    }
    while (n > 10);



    return 0;
}