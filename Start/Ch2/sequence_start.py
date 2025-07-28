# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
my_list = [0, 1, 'this is string', 3.2, False]
print( len(my_list) )

# to access a member of a sequence type, use []
print( my_list[2] )
print( my_list[-1] )
my_list[1] = 'updated value'
print( my_list[0] )
# my_list[5] = 10


# add a list to another list
my_list2 = [1, 2, 3, 4, 5, 6]
print( my_list )
print( my_list2 )
print( my_list + my_list2 )

my_str = 'This is a String for test'
print( my_str[11] )

# use slices to get parts of a sequence
print( my_list[1:7:3] )
print( my_list[-1::-1] )

# you can use slices to reverse a sequence
print( my_list[::-1] )


# Tuples are like lists, but they are immutable
print("tuple")
my_tuple = (my_list, 2, 3, 'this is tring', 5)
print(my_tuple[1])
# my_tuple[1] = 2
print(my_tuple)

# Sets are also sequences, but they contain unique values
my_set = {1, 2, 3, 'this is tring', 5, 4, 4, 3, 2.3, 1.2}
print(my_set)
# print(my_set[2])


# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in my_list)
# print(1 in my_str)
print(1 in my_tuple)
print(1 in my_set)
