
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

# Example :- Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name. Normally, you would have to do this using a for loop shown below

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for i in fruits:
#     if "a" in i:
#         newlist.append(i)

# print(newlist)

# With list comprehension you can do all that with only one line of code:

# Syntax 
# list = [expression for item in iterable if condition == True]
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

newlist2 = [item for item in fruits if "a" not in item]

# print(newlist2)

# Without if

newlist2 = [x for x in fruits]

# print(newlist2)

# using range() function to create an iterable

newlist2 = [x for x in range(100) if x%3 == 0]

# print(newlist2)

# Set the outcome in a list

newlist2 = [x.upper() for x in fruits]

# print(newlist2)

# You can set the outcome to whatever you like:

newlist2 = ["ben" for x in fruits]

# print(newlist2)

newlist2 = [x if x != "banana" else "orange" for x in fruits]

# print(newlist2)

"""
    The statement above is
    
    'Return the item if it is not banana, if it is banana return orange'
"""


# SORTING LIST

thislist = [100, 50, 65, 82, 23]

# Ascending order

thislist.sort()
# print(thislist)

# Descending order :- use the keyword argument reverse = True:

thislist.sort(reverse=True)
# print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort()
# print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

def sortfunc(n):
    # Sort the list based on how close the number is to 50:
    return abs(n - 50)

sortedlist = [100, 50, 65, 82, 23]
sortedlist.sort(key=sortfunc)

# print(sortedlist)

# Perform a case-sensitive test before sorting

thislist = thislist
thislist.sort(key=str.lower)
# print(thislist)



# Copy a List

# You cant simply makie use of list2 = list1 and think you have already copied the list1 into list2. You only copied the reference copy of list1, so anything changed in list2 would reflect in list1.

list1 = [1,2,3,4,5]

# list2 = list1
# list2[3] = "benrobo"

# print(list2, end="\n") # [1, 2, 3, 'benrobo', 5]
# print(list1, end="\n") # [1, 2, 3, 'benrobo', 5]

# There are numbers of ways to copy a list. one of those ways is making use of the copy() method in python

list3 = list1.copy()

list3[3] = "benrobo"

# print(list3, end="\n") # [1, 2, 3, 'benrobo', 5]
# print(list1, end="\n") # [1, 2, 3, 4, 5]

# Another way to make a copy is to use the built-in method list().

list4 = list(list1)

list4[3] = "benrobo"

# print(list4, end="\n") # [1, 2, 3, 'benrobo', 5]
# print(list1, end="\n") # [1, 2, 3, 4, 5]

# Join Two Lists

# There are several ways to join, or concatenate, two or more lists in Python. One of the easiest ways are by using the + operator.

# 1 using " + " operator

l1 = [1,2,3,45]
l2 = ['a','b', 'c']

# print(l1 + l2) # [1, 2, 3, 45, 'a', 'b', 'c']

# 2 using "for loop" operator

# for x in l2:
    # l1.append(x)

# print(l1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

l1.extend(l2)
print(l1)