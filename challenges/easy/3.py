
"""
    Dificulty: Easy
    
    Remove empty List from List
    
    Sometimes, while working with python data, we can have a problem in which we need to filter out certain empty data. These can be None, empty string etc. This can have application in many domains. Let’s discuss certain ways in which removal of empty lists can be performed.
    
"""

test_list = [5, 6, [], 3, [], [], 9]

# Solution 1

# using list comprehension


newlist = [x for x in test_list if x != []]

print(newlist)

# Solution 2

# Using filter

newlist2 = list(filter(None, test_list))

print(newlist2)