# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0


# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together

try :
  x = 10 / 0

except : 
  print("Error occurred")
  
print("\n")

# You can also catch specific exceptions

try :

  answer = input("please input some number to divide ite by 10 : ")
  answer = int(answer)
  print(10/answer)

except ZeroDivisionError as e :
  print("Error Occurred", e)

except ValueError as e :
  print("Error Occurred", e)

finally:
  print("Finally Error Occurred")
