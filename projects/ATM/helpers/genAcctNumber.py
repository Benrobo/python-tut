import random


# Generate account mnumber
def generateAccountNumber(count=12):
    acct_num = ""
    nums = []
    
    for i in range(count):
        nums.append(i)
        rand = random.choice(nums)
        acct_num += str(rand)
    return acct_num

