import json


"""
    JSON is a syntax for storing and exchanging data.

    JSON is text, written with JavaScript object notation.
    JSON in Python
    
    Python has a built-in package called json, which can be used to work with JSON data.
"""

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.

# JSON
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)

# print(y)

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

x = {
    "name": "ben",
    "age": 20
}

y = json.dumps(x)

# print(y, type(y))

"""
    You can convert Python objects of the following types, into JSON strings:

    dict
    list
    tuple
    string
    int
    float
    True
    False
    None
"""
# Dict
# print(json.dumps({"name": "John", "age": 30}))
# # List
# print(json.dumps(["apple", "bananas"]))
# # Tuple
# print(json.dumps(("apple", "bananas")))
# # String
# print(json.dumps("hello"))
# # Integer
# print(json.dumps(42))
# # Float
# print(json.dumps(31.76))
# # Boolean
# print(json.dumps(True))
# print(json.dumps(False))
# # None
# print(json.dumps(None))


# Convert a Python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))

"""
    Format the Result
    The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

    The json.dumps() method has parameters to make it easier to read the result:
"""



# Use the indent parameter to define the numbers of indents:

print(json.dumps(x, indent=1))


# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:

print(json.dumps(x,separators=(", ", " : ")))

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:
    
print(json.dumps(x, indent=4, sort_keys=True))