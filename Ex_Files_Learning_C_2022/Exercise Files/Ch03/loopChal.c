#include <stdio.h>

int main()
{
    int x;

    for(x=1; x<=20; x++)
        printf("%d\n", x);


    printf("---------------------\n");

    int y;
    y = -10;
    while(y < 11)
    {
        if(y % 2 == 0)
            printf("%d\n", y);
            y++;
    }





    return 0;
}