def celcius(temp):
    c = (temp - 32) * (5/9)
    print(f"{c} °C")


def fahrenheiht(temp):
    f = (temp * 9 / 5) + 32
    print(f"{f} °F")


# celcius(7)
# fahrenheiht(8)

def converter():
    while True:
        print("Choose an option: ")
        print("1: F to C")
        print("2: C to F")
        print("3: Exit")
        options = input()

        if options == "1":
            temp = int(input("Please enter temperature in Fahrenheit: "))
            celcius(temp)
        if options == "2":
            temp1 = int(input("Please enter temperature in Celcius: "))
            fahrenheiht(temp1)
        elif (options == "3"):
            # exit
            print("Exiting the app")
            break


converter()

