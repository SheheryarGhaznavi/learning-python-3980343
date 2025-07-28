# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 1000, 100

# conditional flow uses if, elif, else
if x < y :
    print("x is less than y")
elif x > y :
  print("x is greater than y")
else :
      print("x is equal to y")
   


# conditional statements let you use "a if C else b"
result = "x is less than y" if x < y else "x is greater than y" if x > y else "x is equal to y"
print(result)