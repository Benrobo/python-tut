import random


def generatePin(count=4):
    nums = "01234567"
    char = " ".join(nums).split(" ")
    pin = ""
    
    for x in range(1, count+1):
        rand = random.choice(char)
        pin += rand
    
    return pin
    