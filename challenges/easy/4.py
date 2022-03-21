"""
    Difficulty: easy
    
    Problem:
    
    Given: Two positive integers a and b (a < b < 1000).
    Return: The sum of all odd integers from a through b, inclusively.
    
    sample dataset: 100 200
    output: 7500
    
    Hint:
        You can use a % 2 == 1 to test if a is odd
"""

def sumOdd(a, b):
    sum = 0
    for x in range(a, b+1):
        if x % 2 == 1: sum += x
    return sum

print(sumOdd(100, 200))