
"""
    Problem
    Given: A string of length at most 200 letters and four integers , , and .
    
    Return: The slice of this string from indices through and through (with space in between),
    inclusively.
    
    Sample Output :- Humpty Dumpty
"""

letters = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain. 22 27 97 102"

string = "".join(letters[0:12]).center(2)

print(string)