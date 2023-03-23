# ---------- If, Elif, Else ----------
print("-------------------------------------------\n-------------------------------------------")
print("CONDITIONS, LOOPS AND FLOW IN PYTHON")

colour = "green"

def check_colour():
    if colour == "green":
        print("Correct colour")
    elif colour == "blue":
        print("Paint the blue, green")
    else:
        print("Wrong colour, paint green")
        
check_colour()
colour = "blue"
check_colour()
colour = "red"
check_colour()

print("-------------------------------------------\n-------------------------------------------")
# ---------- For Loops ----------

list = ['Apple', 'Orange', 'Banana', 'Pear', 'Mango'] # List of length 5

# Iterate through each item in the list
# Useful for iterating through lists of varying/unknown size
for number in list:
    print(number) # Output 'Apple', 'Orange', 'Banana', 'Pear', 'Mango'


# Iterating through a set range of numbers
# Useful for iterating a set number of times

# You can supply an index to a list to retrieve a specific item from the list
# E.g list[0] will return the first value from the list: 'Apple'
# We can use this to iterate through a range of numbers and return the corresponding position in a list

for i in range(0, 5):
    print(i) # The index 'i' will be 0, 1, 2, 3, 4
    print(list[i]) # Output 'Apple', 'Orange', 'Banana', 'Pear', 'Mango'


# Can also use the len() function to iterate through a list
for i in range(len(list)):
    print(i) # The index 'i' will be 0, 1, 2, 3, 4
    print(list[i]) # Output 'Apple', 'Orange', 'Banana', 'Pear', 'Mango'

# Nested for loops

nested_list = [['Apple', 1], ['Orange', 2], ['Banana', 3], ['Pear', 4], ['Mango', 5]]

for list in nested_list:
    for item in list:
        print(item)

print("-------------------------------------------\n-------------------------------------------")
# ---------- While Loops ----------

a = 0
while a < 15:
    a += 1
    if a%2 != 0:
        print(f"Odd number {a}")
    elif a%3 == 0 and a%4 == 0:
        continue   # No action with number 12
    else:
        print(a)
else:
    print("Finished")
        

# pass, continue, break


print("-------------------------------------------\n-------------------------------------------")
#nested loops
print("Add every number in the second list to each number in the first list")
nums1 = [0, 1, 2, 3]
nums2 = [2, 5, 8, 5]

for i in range(len(nums1)) :
    for j in range(len(nums2)) :
        nums1[i] += nums2[j]

        
print(nums1)

print("-------------------------------------------\n-------------------------------------------")
#Two conditions with AND
a = 1
b = 2

if a == 1 and b == 2:
    print("Both conditions have been met")
else:
    print("Both conditions have not been met")

#Two conditions with OR
a = 1 
b = 4

if a == 1 and b == 2:
    print("Both conditions have been met")
elif a == 1 or b == 2:
    print("One condition has been met")
else:   
    print("Both conditions are incorrect")

