#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))


# print today's date
print("\n")
now= datetime.now()
print("Todays is :", now)


# print today's date one year from now
print("\n")
print("In one year it will be :", now + timedelta(days=365))


# create a timedelta that uses more than one argument
print("\n")
print("In two weeks and three days it will be :", now + timedelta(weeks=2, days=3))


# calculate the date 1 week ago, formatted as a string
print("\n")
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

if afd < today :
  print(f"April fool's day is already went by {(today-afd).days} days ago")
  afd = afd.replace(year=today.year+1)

# time_to_afd = afd-today
# print(afd)
print(f"Its just {(afd-today).days} days until April Fools day")
