#include <stdio.h>

struct position
{
    float lat;
    float lon;
};

typedef struct
{
    float lat;
    float lon;
} Position;

int main()
{
    struct position p1;
    struct position p2 = {3.4567, 4.5678};

    Position p3 = {5.6789, 6.7899};
    
    

    p1.lat = 1.2345;
    p1.lon = 2.3456;

    printf("...%f, %f...\n", p1.lat, p1.lon);
    printf("...%f, %f...\n", p2.lat, p2.lon);



    return 0;
}