#include <stdio.h>
#include <string.h>

int main()
{
    // in C a string is an array of characters
    char s1[6] = {'h', 'e', 'l', 'l', 'o'};
    // is is also possible to initialise a string by assigning a value to a pointer to char
    char* s2 = "world";

    char s3[51];
    int n;
    int i;

    printf("Type something...\n");
    gets(s3);
    printf("You typed : %s\n", s3);

    // get the length of the string
    n = strlen(s3);
    printf("length : %d\n", n);

    // print a string one character at a time
    for (i = 0; i < n; i++)
    {
        printf("%d ... %c\n", i, s3[i]);
    }

    // reverse a string
    strrev(s3);
    printf("reversed : %s\n", s3);

    strcpy(s3, "jackdaws");
    printf("copied ... %s\n", s3);

    // concatenating strings : strcat
    // comparing strings : strcmp
    // examine characters : isalpha, isdigit, isupper, islower, isspace, ...
    // convert characters : toupper, tolower

    return 0;
}