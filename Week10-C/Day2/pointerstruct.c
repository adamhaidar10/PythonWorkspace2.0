#include <stdio.h>

// create a structure that holds the position of the boat
struct position
{
    float lat;
    float lon;
};

// function declaration uses the struct, so this must go after the struct
int change_position(struct position* b, float new_lat, float new_lon);

int main()
{
    struct position boat;
    int r;

    // create the original position of the boat
    boat.lat = 123.456;
    boat.lon = 234.567;
    printf("original : %f, %f\n", boat.lat, boat.lon);

    // change the position
    // passes the boat's position by reference rather than by value
    // (no new copy of the position is created)
    r = change_position(&boat, 124.345, 235.789);

    // check to make sure the values have been changed
    printf("changed  : %f, %f\n", boat.lat, boat.lon);

    return 0;
}

int change_position(struct position* b, float new_lat, float new_lon)
{
    // note to change the value of a structure that is passed by a pointer, 
    // use the arrow symbol to access the members of the structure
    b->lat = new_lat;
    b->lon = new_lon;
    return 0;
}
