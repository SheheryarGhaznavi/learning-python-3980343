# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
my_dict = {
  1 : "value 1",
  2 : "value 22",
  "value 3" : "value 33",
  4.3 : 4,
  5 : ["value 1", 1, 3, 4, 5, 6],
}

print(my_dict)


# dictionaries are accessed via keys
print(my_dict[4.3])
print(my_dict["value 3"])
# print(my_dict[:::])


# you can also set dictionary data by creating a new key
my_dict["seven"] = 7777
my_dict["set"] = {1, 2, 4, "random", 3, 3,4, 2.6}
print(my_dict)

# Trying to access a nonexistent key will produce an error
# print(my_dict[7])
print(my_dict["set"])


# To avoid this, you can use the "in" operator to see if a key exists
print(7 in my_dict)
print("Set" in my_dict)
print("set" in my_dict)
print('set' in my_dict)

# You can retrieve all of the keys and values from a dictionary
print(my_dict.keys())
print(my_dict.values())

# You can also iterate over all the items in a dictionary
print(my_dict.items())

for key, value in my_dict.items():
  print(key)
  value = 0
print(value)
