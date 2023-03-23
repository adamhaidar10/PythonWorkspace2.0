from datetime import datetime

# start out with a dictionary of presidents and their birthdays
presidents = {"Lyndon B Johnson": (1908, 8, 27),
              "Richard Nixon": (1913, 1, 9),
              "Gerald Ford": (1913, 7, 14),
              "Jimmy Carter" : (1924, 10, 1),
              "Ronald Reagan" : (1911, 2, 6),
              "George H W Bush" : (1924, 6, 12),
              "Bill Clinton" : (1946, 8, 19),
              "George W Bush": (1946, 7, 6),
              "Barack Obama": (1961, 8, 4),
              "Donald Trump": (1946, 6, 14),
              "Joe Biden" : (1942, 11, 20)}

# loop around each president
for president in presidents:
    # look at their birthday
    birthday = datetime(*presidents[president])
    # turn it into a readable format
    formattedbirthday = birthday.strftime("%d %B %Y")

    # display the name and the birthday
    s = f"{president}, born on {formattedbirthday}"

    # is the birthday on a monday?
    if birthday.weekday() == 0:
        s = s + " : born on a Monday"

    # display the output
    print(s)

    def hello(firstname, lastname):
        print(f"Hello {firstname} {lastname}")


def add_tax(amount, rate):
    total = amount + ((amount * rate) / 100)
    return total

# a function can return a list
def n():
    l = [1, 2]
    return l


print(add_tax(100, 20))
print(add_tax(15, 15))
print(add_tax(25, 20))
print(add_tax(30, 12))
print(add_tax(1000, 40))

print(n())