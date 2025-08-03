#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
file  = open('text-file.txt', "r")

if file.mode == "r" :
  # contents = file.read()
  # print(contents)
  # print("\n")
  content_lines = file.readlines()
  
  for line in content_lines : 
      print(line)

    # use the read() function to read the entire file
