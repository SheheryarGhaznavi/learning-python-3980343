# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mystr2 = "This is another string"
mybool = True

# We can display the content of a variable using the print() function
print(myint)
print(mystr)

# Operators are used to perform operations on variables
print("\n")
print(myint + myfloat)
print(myint * myfloat)
print(myint / myfloat)
print(myint % 2.5)

print(mystr + mystr2)
print(mystr, mystr2)
print(mystr * 2)

# Logical and comparison operators 
print("\n")
print(myint == 10)
print(myint != 10)
print(myint > 10)
print(myint < 10)

print("\n")
print(myint > 9 and myint < 11)
print(myint > 10 or myint < 11)
print(not(myint > 10 or myint < 11))

# re-declaring a variable works
myint = 'abc'
print("\n")
print(myint)