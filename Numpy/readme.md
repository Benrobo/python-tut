## Numpy

Numpy stands for Numerical Python which is purposely used for working with arrays.

The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with `ndarray` very easy.

# Why is NumPy Faster Than Lists?

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Numpy is faster than traditional `list` because part of numpy is written in `python`,  but most of the parts that require `fast` computation are written in `C or C++`.