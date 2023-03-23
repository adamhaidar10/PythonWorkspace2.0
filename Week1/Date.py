from datetime import datetime, timedelta

# get current date/time (ISO 8601 format)
d1 = datetime.now()
print(d1)

# construct a datetime down to the second
d2 = datetime(2020, 12, 4, 14, 56, 53)
print(d2)

# construct a datetime just using a date
d3 = datetime(2018, 7, 19)
print(d3)

# construct a datetime by expanding a tuple to fill in the parameters
t = (2007, 8, 6, 17, 20, 13)
d4 = datetime(*t)
print(d4)

# compare two dates - see if one date is before (earlier than) another date
d5 = datetime(1973, 6, 23)
d6 = datetime(1965, 10, 3)

if d5 < d6:
    print("d5 is earlier than d6")
else:
    print("d6 is earlier than d5")

# check if two dates are equal
d7 = datetime(1965, 10, 3)
if d6 == d7:
    print("d6 and d7 are the same")
else:
    print("d6 and d7 are different")

# find the weekday of a date (0=Monday, 6=Sunday)
w = d7.weekday()
print(w)

# format a date using strftime
# %A weekday in long form (%a = short form)
# %d day of month
# %m month number
# %b, %B month name in short or long form
# %y, %Y year number in 2 or 4 digit form
# %j day number of the year
# %H, %h hour (24 or 12 hour format)
# %M minute
# %S second
print(d4.strftime("%A %d %B %Y, %H:%M:%S which is day %j of the year"))

# use a timedelta to add or subtract from a datetime
d8 = datetime.now()
print(d8)
d9 = d8 - timedelta(hours=1)
print(d9)
d10 = d8 + timedelta(hours=2)
print(d10)

# find the difference between two datetimes in hours or minutes
diff = d10 - d9
print(diff)
diffminutes = diff / timedelta(minutes=1)
print(diffminutes)