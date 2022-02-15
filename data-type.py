
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

a = ["apple", "banana", "cherry"]
b = {"name": "ben"}
c={"ben", "true", "begin", "ben"}

d = bytearray(5)
e = memoryview(bytes(5))

# NUMBERS

"""
    We have different numbers data-types in python
    - int, float, complex
"""

# INT

a = 67

# FLOAT

b = 3.142

# COMPLEX

c = 10e4

print(
    f"""
        Int: {a} {type(a)}
        Float: {b} {type(b)}
        Complex: {c} {type(c)}
    """
)


