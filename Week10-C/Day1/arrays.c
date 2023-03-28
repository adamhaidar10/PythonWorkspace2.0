#include <stdio.h>

int main()
{
    int a1[3];
    int a2[3] = {11, 22, 33}; // can initialise arrays at the time they are created

    char s[11] = {'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'};


    // assign values to array
    // arrays are zero indexed
    a1[0] = 5;
    a1[1] = 99;
    a1[2] = 76;


    // access elements of a arrray
    printf("...%d\n", a1[1]);

    // assign a value to a position outside of the array this can have unintended consequences  
    a1[3] = 111;
    printf("...%d\n", a1[3]);
    
    
    printf("...%d\n", a1[9]);

    printf("...%c\n", s[10]);

    printf("...%s", s);






    return 0;
}