from datetime import datetime as date

"""
    Python Dates
    
    A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""


x = date.now()
# print(x) # 2022-03-22 12:03:56.771803

# print(x.year)
# print(x.strftime("%B"))

"""
    Creating Date Objects
    To create a date, we can use the datetime() class (constructor) of the datetime module.

    The datetime() class requires three parameters to create a date: year, month, day.
"""


x = date(2022, 3, 22)

# print(x)


"""
    The strftime() Method
    The datetime object has a method for formatting date objects into readable strings.

    The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

x = date(2022, 3, 23)

print(x.strftime("%A")) # week day Wednesday
print(x.strftime("%a")) # week day Wed
print(x.strftime("%b")) # Month name, short version
print(x.strftime("%B")) # Month name, Full version
print(x.strftime("%H")) # Hour 00-23
print(x.strftime("%I")) # Hour 00-12
print(x.strftime("%p")) # AM/PM