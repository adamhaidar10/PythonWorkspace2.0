for i in range(1, 111):
    s = ""
    if i % 3 == 0:
        s += "Fizz"
    if i % 5 == 0:
        s += "Buzz"
    if i % 7 == 0:
        s += "Meow"
    if s == "":
        s = str(i)

    print (s)