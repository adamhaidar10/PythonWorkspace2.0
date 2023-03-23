l = [0, 1, 2, 3, 4]

try:
    outfile = open("numbers.txt." , "w")
    for i in range(0, 9):
        print(l[i], file=outfile)
    outfile.close()
except (IndexError, PermissionError):
    print("You are not allowed to write to the file")

print("finished")



try:
    n = 5 / 0
except ZeroDivisionError:
    print("Couldnt do that")

try:
    a = 5 +"Hello"
except TypeError:
    print("couldnt do that")


try:
    n = 5 + "hello"
except Exception as err:
    print(err)