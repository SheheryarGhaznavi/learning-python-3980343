
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now  = datetime.now()

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("The current year is : %y"))
print(now.strftime("%a, %d %B, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print("\n")
print(now.strftime("Locale Date & Time is : %c"))
print(now.strftime("Locale Date is : %x"))
print(now.strftime("Locale Time is : %X"))



#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print("\n")
print(now.strftime("The current time is : %I:%M:%S %p"))
print(now.strftime("The current time is : %H:%M:%S %p"))
