import os

"""
    To open the file, use the built-in open() function.

    The open() function returns a file object, which has a read() method for reading the content of the file:
"""

print("")

try:
    fil = "./Files/tmp/test.txt"
    f = open(fil)
    # print(f.read())
except:
    print("No such file exist")

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

try:
    fil = "./Files/tmp/test.txt"
    f = open(fil)
    # print("<with file content limit>")
    # print(f.read(3))
except:
    print("No such file exist")
    
"""
    Read Lines
    You can return one line by using the readline() method:
"""

try:
    fil = "./Files/tmp/test.txt"
    f = open(fil)
    # print("using readline() to read one line of the file")
    # print(f.readline())
except:
    print("No such file exist")
    
# By calling readline() two times, you can read the two first lines: 

try:
    fil = "./Files/tmp/test.txt"
    f = open(fil)
    # print("using readline() to read one line of the file")
    # print(f.readline())
    # print(f.readline())
except:
    print("No such file exist")
    
# By looping through the lines of the file, you can read the whole file, line by line:

# It is a good practice to always close the file when you are done with it.
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

try:
    fil = "./Files/tmp/test.txt"
    f = open(fil)
    for line, data in enumerate(f):
        print(line, data)
    f.close()
except:
    print("No such file exist")
