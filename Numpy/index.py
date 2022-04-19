import numpy as np


arr = np.array([1, 2, 3, 4, 5])

# print(type(arr), arr) # type is numpy.ndarray not list

# check numpy version

# print(np.__version__) ## 1.22.3

""" 
    To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
"""

arr = np.array((1, 2, 3, 4, 5))

# print(arr)

"""
    Dimensions in Arrays
    A dimension in arrays is one level of array depth (nested arrays).

    nested array: are arrays that have arrays as their elements.
"""


# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# Create a 0-D array with value 42


arr = np.array(42)

# print(arr)

"""
    1-D Arrays
    An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

    These are the most common and basic arrays.
"""

arr = np.array([1, 2, 3, 4, 5])

# print(arr)

"""
    2-D Arrays
    An array that has 1-D arrays as its elements is called a 2-D array.

    These are often used to represent matrix or 2nd order tensors.

    NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr)

"""
    3-D arrays
    An array that has 2-D arrays (matrices) as its elements is called 3-D array.

    These are often used to represent a 3rd order tensor.
"""


arr = np.array([
                [
                    [1, 2, 3], 
                    [4, 5, 6]
                ], 
                [
                    [1, 2, 3], 
                    [4, 5, 6]
                ]
            ])

# print(arr)

"""
    Check Number of Dimensions?
    NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
"""

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

"""
    Higher Dimensional Arrays
    An array can have any number of dimensions.

    When the array is created, you can define the number of dimensions by using the ndmin argument.
"""

arr = np.array([1,2,3], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)






