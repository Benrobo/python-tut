
"""
    List
    
    Lists are used to store multiple items in a single variable.

    Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

    Lists are created using square brackets:
"""

print("\n")

alist = [1,2,3,4,5,6,7]

# print(alist)

# Note :- List items are ordered, changeable, and allow duplicate. when we talk about ordered, we meant each time a new item is appended to a list, it get placed at the end of the list.

# Accessing list :- we acn simply make use of either their index position or slicing through the list

b = alist[2]
a = alist[1:4] + alist[:]

# print(a)

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

cubes = [1,8,27,65,125]

cubes[3:4] = [64]

# print(cubes)

# Delete List Elements
# To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know. For example −

copy = alist

# del copy[4]

# copy.remove(4)

# print(copy)

# Append to a list

copy2 = alist

copy2.append(123)

# print(copy2)

# Insert item to list at specified position

copy3 = alist

copy3.insert(4, "benrobo")

# print(copy3)

# Sort and Reverse a list

copy4 = alist

copy4.reverse()

# print(copy4)

# Clear a list using clear() method

copy4.clear()

# print(copy4)



# LOOP THROUGH A LIST :- You can loop through the list items by using a for loop:

newlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# for x in newlist:
#     print(x)
    
# Loop Through the Index Numbers :- using the range() function and len() function

# for x in range(len(newlist)):
#     print(x) # 0,2,3,....n
#     print(newlist[x]) # a,b,c,d...n
    
    
# List Comprehension :- List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


