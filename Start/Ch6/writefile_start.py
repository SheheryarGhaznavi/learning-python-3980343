# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
file = open("text-file.txt", "w+")
print(file.write("this is first data"))
print(file.write("\n"))
print(file.write("this is second data"))
print(file.close())
print("\n")

# Open the file for appending text to the end
file = open("text-file.txt", "a+")

# write some lines of data to the file
print(file.write("\nthis is third data"))
print(file.write("\n"))
print(file.write("this is second 2 data"))


# close the file when done
print(file.close())
