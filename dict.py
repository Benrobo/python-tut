
"""
    Dictionary
    
    Dictionaries are used to store data values in key:value pairs.

    A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
    
    dictionary items are ordered, mutable, and do not allow duplicate values.
"""


adict = {
    "name": "ben",
    "age": 21,
    "course": "CS",
}

# Adding to dictionary
adict["pet"] = "dog"

# Update an existing entry
adict["name"] = "benaiah"

# Delete a specific entry using the del keyword
del adict["pet"]

# print(adict)

# Get the keys of a dictionary

keys = adict.keys()

# print(keys)

adict["pet"] = "dog"

# print(keys)

# Get Values

val = adict.values()

# print(val)

# Get item :- the item() method would return each items in a dictionary as tuples.

item = adict.items()

# print(item) # dict_items([('name', 'benaiah'), ('age', 21), ('course', 'CS'), ('pet', 'dog')])

# Check if a specified key exist within a dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# if "model" in thisdict:
#     print("Yes, it does.")
    
    
"""
    Update Dictionary
    
    The update() method will update the dictionary with the items from the given argument.

    The argument must be a dictionary, or an iterable object with key:value pairs.
"""

ndict = dict(thisdict)

ndict.update({"year": 2022})

# print(ndict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2022}

# Clear a dictionary

ndict2 = dict(thisdict)
ndict2.clear()
print(ndict2) # {}

"""
    Loop Through a Dictionary
    You can loop through a dictionary by using a for loop.

    When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""

ndict3 = dict(thisdict)
keys = []
val = []

for k in ndict3:
    keys.append(k)
    val.append(ndict3[k])

print(keys)
print(val)









