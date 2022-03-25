import random
    
# Generate unique ID
def genId(count=12):
    char = "#abcdefgh123456789;@$%^&*()!~"
    formated_char = " ".join(char).split(" ")
    uuid = ""
    
    for i in range(count):
        rand = random.choice(formated_char)
        uuid += rand
    unique = list(set(uuid))
    return f"""#{"".join(str(elm) for elm in unique)}"""
