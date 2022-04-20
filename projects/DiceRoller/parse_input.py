

# Parse INputs

def parse_input(inputs):
    if inputs == None or inputs == "":
        return print("Expecteda number of dice to roll, but got none")
        
    MIN = 1
    MAX = 6
    
    userInp = int(inputs)
    
    if userInp < MIN:
        return print("invalid dice number. {}".format(userInp))
    elif userInp > MAX:
        return print("invalid dice number. {}".format(userInp))

    return userInp