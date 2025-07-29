# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function

def helloFunc() :
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

# helloFunc()

# function that takes parameters
def helloFunc(greeting) :
  print("hello world!")
  name = input("What is your name? ")
  print(greeting, name)

# helloFunc("Nice to meet you too,")

# function that returns a value

def multiplyFunc(x) :
  return x*x*x

print(multiplyFunc(2))

# function with default value for an parameter

def helloFunc(greeting, name = None) :
  print("hello world!")

  if name == None :
    name = input("What is your name? ")
  print(greeting, name)

# helloFunc("Nice to meet you too,", 'Ahmed')
# helloFunc(name = 'Ahmed 2', greeting = "Nice to meet you too,")


# function with variable number of parameters

def multiParamFunc(*params) :

  result = 0
  for d in params :
    result += d

  return result

print(multiParamFunc(2,2,2,2,3,3,3,3,4))