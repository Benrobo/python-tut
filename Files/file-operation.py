import os
import time
    
"""
   Write to an Existing File
    To write to an existing file, you must add a parameter to the open() function:

    "a" - Append - will append to the end of the file

    "w" - Write - will overwrite any existing content
"""

print("")


try:
    cdir = os.getcwd()
    fil = os.path.join(cdir, "Files", "temp", "test.txt")
    # open the file for with writing or appending mode which would overide all data
    f = open(fil, "a")    
    f.write("Overide data \n")
    # print("file data appended successfully")
    
    # reading data from file
    # open the file with reading mode
    f = open(fil, "r")
    # print(f.read())
    f.close()
except:
    print("No such file exist")

"""
    Create a New File
    To create a new file in Python, use the open() method, with one of the following parameters:

    "x" - Create - will create a file, returns an error if the file exist

    "a" - Append - will create a file if the specified file does not exist

    "w" - Write - will create a file if the specified file does not exist
"""

try:
    cdir = os.getcwd()
    fil = os.path.join(cdir, "Files", "temp", "newfile.txt")
    f = open(fil, "w")
    # print("File created..")
    f.close()
except:
    print("File already exist")
    
    

"""
    Renaming File and Folder
    
    This operation can be done using the os.rename(curr_dir_name, new_dir_name)
"""    

try:
    cdir = os.getcwd()
    oldname = os.path.join(cdir, "Files", "temp", "newfile.txt")
    newname = os.path.join(cdir, "Files", "temp", "rename.txt")
    
    os.rename(oldname, newname)
    print("File renamed")
    
except:
    print("Something went wrong..")


"""
    Delete a File
    To delete a file, you must import the OS module, and run its os.remove() function:
"""

try:
    fil = os.path.join(cdir, "Files", "temp", "newfile.txt")
    # os.remove(fil)
except:
    print("Failed to delete file, no such file exist")
    

"""
    Check if File exist:
    To avoid getting an error, you might want to check if the file exists before you try to delete it:
"""

fil = os.path.join(cdir, "Files", "temp", "newfile.txt")
if os.path.exists(fil):
    pass
    # print("Deleting file..")
    # time.sleep(2)
    # os.remove(fil)
    # print("File deleted..")
else:
    print("The file does not exist")



"""
    Delete Folder
    To delete an entire folder, use the os.rmdir() method:
"""

fil = os.path.join(cdir, "Files", "temp2")
if os.path.exists(fil):
    print("Deleting folder..")
    time.sleep(2)
    os.rmdir(fil)
    print("Folder deleted..")
else:
    print("The Folder does not exist")