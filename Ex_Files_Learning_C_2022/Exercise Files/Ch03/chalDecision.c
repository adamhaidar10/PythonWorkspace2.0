#include <stdio.h>

int main()
{
    int a;


    printf("Enter a number:");
    scanf("%d", &a);

    switch (a)
    {
    case 1:
        printf("Red");
        break;
    
    case 2:
        printf("Green");
        break;
    
    case 3:
        printf("Blue");
    
    default:
        printf("Invalid input");
        break;
    }
    return 0;

}