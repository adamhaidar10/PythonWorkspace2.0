#include <stdio.h>
#include <stdbool.h>

struct details
{
    char * name;
    char * address;
    char * city;
    char * postcode;
};
int changeName(struct details* b, char new_name[30]);
int changeAddress(struct details* b, char new_address[30]);
int changeCity(struct details* b, char new_city[30]);
int changePostcode(struct details* b, char new_postcode[30]);

int main()
{
    char decision;
    int option;
    bool changes = true;

    char name[30];
    char address[30];
    char city[30];
    char postcode[30];

    struct details person1;
    
    printf("Enter your name: \n");
    gets(name);
    person1.name = name;

    printf("Enter your street address: \n");
    gets(address);
    person1.address = address;

    printf("Enter your city: \n");
    gets(city);
    person1.city = city;

    printf("Enter your postcode: \n");
    gets(postcode);
    person1.postcode = postcode;


    printf("\nYour details are:\nName: %s\n Address: %s\nCity: %s\nPostcode: %s\n", person1.name, person1.address, person1.city, person1.postcode);

    while(changes == true)
    {
        printf("Would you like to change any of these details (Y/N)\n");
        scanf("%c", &decision);

        if (decision == 'Y' || decision == 'y')
        {
            printf("\nwhich details would you like to change? Please select a number: \n");
            printf("1. Name\n2. Address\n3. City\n4. Postcode\n");
            scanf("%d", &option);
            getchar();

            switch (option)
            {
                case 1:
                    printf("\nEnter your name: ");
                    gets(name);
                    changeName(&person1, name);
                    break;
            
                case 2:
                    printf("\nEnter your address: ");
                    gets(address);
                    changeAddress(&person1, address);
                    break;
            
                case 3:
                    printf("\nEnter your city: ");
                    gets(city);
                    changeCity(&person1, city);
                    break;
            
                case 4:
                    printf("\nEnter your postcode: ");
                    gets(postcode);
                    changePostcode(&person1, postcode);
                    break;
            }
            printf("\nYour details are:\nName: %s\n Address: %s\nCity: %s\nPostcode: %s\n", person1.name, person1.address, person1.city, person1.postcode);
        }
        else
        {
            changes = false;
        }
    }
    return 0;
    
};

int changeName(struct details* b, char new_name[30])
{
    b->name = new_name;
    return 0;
};

int changeAddress(struct details* b, char new_address[30])
{
    b->address = new_address;
    return 0;
};

int changeCity(struct  details* b, char new_city[30])
{
    b->city = new_city;
    return 0;
};

int changePostcode(struct details* b, char new_postcode[30])
{
    b->postcode = new_postcode;
    return 0;
};

