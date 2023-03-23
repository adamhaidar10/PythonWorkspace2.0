phrase = input("Enter a phrase:")
print (phrase)
print (phrase.upper())
print (phrase.lower())
print ("This string has " + str(len(phrase)) + " characters")
print (phrase.replace(" ", "")) 

name = input("Name?")
theme = input("Theme?")
place = input("Location?")
date = input("Date?")
time = input("Time?")
verb = input("Verb?")
animal = input("Animal?")
bodyPart = input("Body part?")
rsvp = input("Contact info?")
print (name.capitalize() + " is having a " + theme + " themed party! It's going to be at " + place + " on " + date + ". Please make sure to show up at " + time + ", or else you will be required to " + verb + " a/an " + animal.capitalize() + " with your " + bodyPart + ". RSVP at " + rsvp + ".")
print (f"{name.capitalize()} is having a {theme} themed party! It's going to be at {place} on {date}. Please make sure to show up at {time}, or else you will be required to {verb} a/an {animal.capitalize()} with your {bodyPart}. RSVP at {rsvp}.")





