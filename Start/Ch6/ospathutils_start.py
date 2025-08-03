#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#


import os
import time
from datetime import datetime
# from os import path
path = os.path


# Print the name of the OS
print(os.name)

# Check for item existence and type
print("\n")
print("Item exists :", path.exists('text-file.txt'))
print("Item is a file :", path.isfile('text-file.txt'))
print("Item is a directory :", path.isdir('text-file.txt'))

# Work with file paths
print("\n")
print("File Path :", path.realpath('text-file.txt'))
print("File Path :", path.split( path.realpath('text-file.txt') ))

# Get the modification time
print("\n")
file_time = time.ctime( path.getmtime('text-file.txt') )
print(file_time)
# print("File Path :", path.realpath('text-file.txt'))
print(datetime.fromtimestamp( path.getmtime('text-file.txt') ))

# Calculate how long ago the item was modified
print("\n")
td = datetime.now() - datetime.fromtimestamp( path.getmtime('text-file.txt') )
print(F"It has been {td} since the file was modified")
print(f"or, {td.total_seconds()} seconds")

