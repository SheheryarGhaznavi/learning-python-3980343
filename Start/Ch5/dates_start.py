#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print(f"Today date is {today}")
print('\n')

# print out the date's individual components
print(f"Date component is : {today.day} : {today.month} : {today.year}")
print('\n')

# retrieve today's weekday (0=Monday, 6=Sunday)
print('Today weekday # is :', today.weekday())
days = ["mon", 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print('Today is a',days[today.weekday()])
print('\n')

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print(today)
print('\n')

# Get the current time
print(datetime.time(datetime.now()))