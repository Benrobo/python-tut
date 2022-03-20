
"""
    Tuples
    
    Tuples is one of the built-in data types in python. It is immutable and can alos store multiple items of different datatypes.
    
    A tuple is a collection which is ordered and unchangeable.
    
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
    
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""

print("")

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# print(thistuple)

# Length of tuple

# print(len(thistuple))


# Creating Tuple
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Valid tuple

tp1 = ("ben",)
# print(type(tp1)) # tuple

# Invalid tuple

tp2 = ("ben")
# print(type(tp2)) # string

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

tp3 = tuple(("ben", "ben"))
# print(tp3, type(tp3))

# Access Tuples

tp4 = thistuple[0]
# print(tp4) # apples



# Slicing tuples

tp5 = thistuple[2:3]

# print(tp5) # ("csdcs",)


# Updating Tuple :- we can update a tuple using list comprehension method

tp6 = [x if x != "banana" else "changed" for x in thistuple]
# print(tp6)

# Delete a tuple

tup7 = tuple(thistuple)

# print(tup7)
# del tup7
# print(tup) # Error: tup7 is not defined. because it has been deleted

# Changing Tuple :- by default, tuple is unchangable, but we can still change a tuple if converted to a list

tup8 = tuple(thistuple)

l1 = list(tup7)

l1[3] = "benrobo"

# print(tup8, l1)

# Add Item to tuple :- by simply converting it to a list

l1.append("benrobo-8.2")

# print(l1)


# Adding Tuple to Tuple

tup9 = tuple(thistuple)
addtup = ("facebook",)

tup9 += addtup

# print(tup9) # ('apple', 'banana', 'cherry', 'apple', 'cherry', 'facebook')


# PACKING & UNPACKING.

# When we create a list or tuple and assigned that list or tuple to a variable, we are packing it to a variable. we can also Unpack / Destructure the values from the variables

tup10 = ("apple", "banana")

(red,yellow) = tup10

# print(red, yellow) # apple banana

# Using Asterisk*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# print(green) # apple
# print(yellow) # banana
# print(red) # ['cherry', 'strawberry', 'raspberry']



# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

# print(green) # apple
# print(tropic) # ['mango', 'papaya', 'pineapple']
# print(red) # cherry



# LOOP A TUPLE

newtop = tuple(fruits)

# For

# for i in newtop:
#     print(i)


# While

i = 0

# while i < len(newtop):
#     print(newtop[i])
#     i += 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
# print(tuple3)

# Multiply Tuples

newtop = tuple1 * 2

print(newtop) # ('a', 'b', 'c', 'a', 'b', 'c')



"""
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    
    Set is a collection which is unordered and unindexed. No duplicate members.
    
    Dictionary is a collection which is ordered* and changeable. No duplicate members.
"""