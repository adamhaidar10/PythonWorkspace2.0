import random #importing a library 

#Prints the words individually 
s = "hello"

for i in range(0, len(s)):
    print(s[i])

#Same as above but simplified
for c in s:
    print(c)

#Nested loop
h = "hello"

for a in h:
    for h in a:
        print(a, h)

#While loop
i = 1

while i <= 10:
    print(i)
    i += 1
print("finished")

x = random.randint(1, 100)
print(x)
while x <= 50:
    print(x)
    x += 1
print("finished")

#Lists 
l = ["Shihab", "Uddin", "Test"]

print(l[1])
print(l[-1])
for name in l:
    print(name)

#adding something to the list
l.append("Testing")
print(l[3])
print(l)

#Placing a new item in the list
l.insert(2, "Mr")
print(l)

l.remove("Shihab")
print(l)

#Length of list
print(len(l))

#Sorting a list
l.sort()
print(l)

#Sorting a list and assigning it to a new variable
s = sorted(l)
print(s)

#Check if a thing is in the list
if "Shihab" in l:
    print("Shihab is in the list")

#Dictionary with keys
my_credit_card = {"Cardnumber" : 12341234,
                  "cardtype" : "Visa",
                  "cardexpire" : 3}
print(my_credit_card["cardexpire"])

for s in my_credit_card.values():
    print(s)

# create dictionaries for employees in a company
alice = {"name" : "Alice Smith",
         "address" : "1 Main Road",
         "emp_id" : 123131321,
         "title" : "software engineer"}

bob = {"name" : "Bob Jones",
       "address" : "99 High Street",
       "emp_id" : 49238749827,
       "title" : "project manager"}

jim = {"name" : "Jim Jimson",
       "address" : "33 Long Road",
       "emp_id" : 234242334,
       "title" : "graphic designer"}

# create a list of dictionaries
employees = [alice, bob, jim]
print(employees)

# print the name of employee 1
print(employees[1]["name"])

# print the names of all employees
for employee in employees:
    print(employee["name"])