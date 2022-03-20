
"""
    Set
    
    Sets are used to store multiple items in a single variable.

    Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

    A set is a collection which is both unordered and unindexed.

    Sets are written with curly brackets.
    
    Set items are unordered, unchangeable, and do not allow duplicate values.
"""

print("")

thisset = {"apple", "banana", "cherry"}

# print(type(thisset)) # <class 'set'>


# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

"""
    Unchangeable
    
    Sets are unchangeable, meaning that we cannot change the items after the set has been created.

    Once a set is created, you cannot change its items, but you can add new items.
"""

# Duplicates Not Allowed

sets = {'a','b','c','a'}

# print(sets) # {'a', 'b', 'c'}

# Length of Sets

# print(len(sets))

# SET CONSTRUCTORS

newsets = set(sets)

# print(newsets)

# Access Items

# You cannot access items in a set by referring to an index or a key. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

set1 = set(sets)

# for x in set1:
#     print(x)


# ADD ITEMS TO SET
# Once a set is created, it cant be changed. you can only make use of the add() method for adding items to a sets.

set2 =  {"apple", "orange", "banana", "pineapple"}

set2.add("guava")

# print(set2)

# Adding items from another set into a new set :- use the update() method

nset = set(set2)
tropical = {"pineapple", "mango", "papaya"}

nset.update(tropical)

# print(nset) # {'guava', 'mango', 'papaya', 'banana', 'orange', 'apple', 'pineapple'}


"""
    Add Any Iterable
    
    The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).`
"""

nset2 = set(set2)
names = ['ben', "benawad", "benaiah"]

nset2.update(names)

# print(nset2)


"""
    Remove Item
    
    To remove an item in a set, use the remove(), or the discard() method.
"""

# Remove()

# If the item to remove doesnt exist, an error would be throwned. 

nset3 = set(set2)
nset3.remove("apple")
# print(nset3)

# Discard()

# If the item to remove doesnt exist, no error is throwned.

nset4 = set(set2)
nset4.discard("doesnt exist")
# print(nset4)


# Join Set

# The union() method returns a new set with all items from both sets:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# Or making use of the update() method

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)








