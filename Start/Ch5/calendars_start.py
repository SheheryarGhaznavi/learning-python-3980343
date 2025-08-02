#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SATURDAY)
the_str = c.formatmonth(206,1,0,0)
print(the_str)

# create an HTML formatted calendar
print("\n")
hc = calendar.HTMLCalendar(calendar.SATURDAY)
the_str = hc.formatmonth(206,1)
print(the_str)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
print("\n")
for i in c.itermonthdays(2026,8) :
  print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("\n")
for name in calendar.month_name :
  print(name)


print("\n")
for day in calendar.day_name :
  print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("\n")
print("Team meetings will be on :")

for m in range(1,13) :

  cal = calendar.monthcalendar(2026, m)
  week_one = cal[0]
  week_two = cal[1]

  print(week_one)

  if week_one[calendar.FRIDAY] :
    meet_day = week_one[calendar.FRIDAY]
  else :
    meet_day = week_two[calendar.FRIDAY]

  print(f"{calendar.month_name[m]} : {meet_day}")