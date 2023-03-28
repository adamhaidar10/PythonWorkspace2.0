#include <stdio.h>
#include <limits.h>
#include <math.h>

int main()
{
    
    int n = 5; // an integer
    float f = 1.234; // accurate to 6 dp
    double d = 2.3456789; // accurate to 10 dp
    char c = 'A';  // a single letter
    int a = 97;

    int z,x,y; // can create multiple variables of the same type on one line

    long int l; 
    short int s;

    unsigned int u;   // changes range to 0..4 billion ish
    
    
    // check size and range of different types of variable
    // printf("int takes up: %d\n",sizeof(int));
    // printf("Max int is: %d\n", INT_MAX);
    // printf("Max int is: %d\n", INT_MIN);

    // printf("long int takes up: %d\n",sizeof(long int));
    // printf("Max long int is: %d\n", LONG_MAX);
    // printf("Max long int is: %d\n", LONG_MIN);

    // printf("short int takes up: %d\n",sizeof(short int));
    // printf("Max short int is: %d\n", SHRT_MAX);
    // printf("Max short int is: %d\n", SHRT_MIN);

    // changing from a float to an int just takes of the decimals
    printf("...%d\n", (int)f);

    // changing from a double to a float rounds the double to 6 decimal places.
    printf("...%f\n", (float)d);

    // change from char to int - returns the ASCII number
    printf("...%d\n", (int)c);

    // change from a int to a char - finds the letter accociated with that ASCII key
    printf("...%c\n", (char)a);

    // do some sums
    x = 33;
    y = 7;
    z = 0;

    // add
    z = x + y;

    printf("...%d\n", z);

    // subtract
    z = x - y;

    printf("...%d\n", z);

    // multiply
    z = x * y;

    printf("...%d\n", z);

    // divide
    z = x / y;

    printf("...%d\n", z);

    // modulus
    z = x % y;


    printf("...%d\n", z);

    x = 625;
    z = sqrt(x);
    printf("...%d\n", z);




    return 0;
}