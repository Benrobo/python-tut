from random import randint

# Roll Dice

def roll_dice(numOfDice):
    
    diceRolled = []
    
    for x in range(numOfDice):
        roll = randint(1,6)
        diceRolled.append(roll)
    return diceRolled