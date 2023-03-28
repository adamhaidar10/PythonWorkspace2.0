#include <stdio.h>

int main ()
{
    int n, x;
    char s[20];

    // printf("Enter two numbers : \n");
    // scanf("%d %d", &n, &x);
    // printf("You entered %d %d\n", n, x);

    printf("Enter your name : ");
    gets(s);
    printf("You entered %s",s);

    return 0;

}