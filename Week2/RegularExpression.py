import re

# create a list of postcodes
postcodes = ["GU23 8PD", "PE8 2AA", "pe7 8nn", "W1A 1AA"]

# check to see if each postcode is valid
for postcode in postcodes:
    if re.match("[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} [0-9][A-Z]{2}", postcode):
        print("Matched")
    else:
        print("Not matched")

print("-------")

# sometimes we need to use fullmatch rather than match to do exact matching
if re.fullmatch("[A-Z]{0,2}", "ABC"):
    print("Matched")
else:
    print("Not matched")

print("-------")

# extracting data that matches a regular expression from a string
s = "hello 347239723979 this is $%^&*()*&( some *(&(87987 very .... mixed up (&(&(* text"
res = re.findall("[a-z]", s)
print(res)

print("-------")

# compiling a regular expression into a pattern
# using the pattern to search a piece of text
p = re.compile("[0-9]+")
print(type(p))
s = "Order 123 has been completed"
found = p.search(s)
print(found)
print(found.span())
print(found.group())