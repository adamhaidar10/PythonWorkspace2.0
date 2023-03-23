from math import sqrt


def anagrams(text1, text2):
    if sorted(text1.replace(" ", "").lower()) == sorted(text2.replace(" ","").lower()):
        print("they are anagrams")
    else: 
        print("they are not anagrams")

print(anagrams("stone", "note"))



#quadratic equation
def solve_equations(a, b, c):

    x = (-b + sqrt((b*b) - 4 * a * c)) / (2 * a)
    y = (-b - sqrt((b*b) - 4 * a * c)) / (2 * a)
    print(x)
    print(y) 

solve_equations(-3, 3, 1)
 
    