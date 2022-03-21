# Create a list containing a valid integers and a suqares  of those interges from 1-10

"""
    [(1,1)(2,4)(3,9)...(n, n^2)]
"""

# Solution 1

comb = []

for x in range(1,11):
    comb.append((x, x**2))
print(comb)

# Solution 2

comb2 = [[x, x**2] for x in range(1,10)]

print(comb2, end="\n")