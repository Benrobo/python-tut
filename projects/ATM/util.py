import random
from datetime import datetime as date
import time

# Utility File

# Generate account mnumber
def acctGenerate(self, count=12):
    acct_num = ""
    nums = []
    
    for i in range(count):
        nums.append(i)
        rand = random.choice(nums)
        acct_num += str(rand)
    return acct_num


    
# Generate unique ID
def genId(self, count=12):
    char = "#abcdefgh123456789;@$%^&*()!~"
    formated_char = " ".join(char).split(" ")
    uuid = ""
    
    for i in range(count):
        rand = random.choice(formated_char)
        uuid += rand
    unique = list(set(uuid))
    return f"""#{"".join(str(elm) for elm in unique)}"""



# Format date
def formatDate(self):
    currDate = date.now()
    year = currDate.year
    month = currDate.strftime("%B")
    day = currDate.strftime("%d")
    hr = currDate.strftime("%I")
    mint = currDate.strftime("%M")
    am = currDate.strftime("%p")
    return f"{month} {day}, {year} {hr}:{mint} {am}"

