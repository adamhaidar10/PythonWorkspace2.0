#include <stdio.h>
#include <string.h>

int main()
{
    char fullname[64];
    char first[32];
    char second[32];
    

    printf("Enter your first name: ");
    fgets(first, 32, stdin);
    printf("Enter your second name: ");
    fgets(second, 32, stdin);
    
    strcpy(fullname, first);
    strcat(fullname, second);
    
    
    printf("%s", fullname);

    return 0;
}