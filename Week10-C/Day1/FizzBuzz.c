#include <stdio.h>
#include <string.h>

int main()
{
    int i;
    char s[13];

    for (i = 1; i<=105; i++)
    {
        s[0] = '\0';

        if(!(i % 3))
            strcat(s, "Fizz");
        if(!(i % 5))
            strcat(s, "Buzz");
        if(!(i % 7))
            strcat(s, "Meow");

        (strlen(s) == 0) ? printf("%d\n", i) : printf("%s\n", s);
    }

    return 0;
}