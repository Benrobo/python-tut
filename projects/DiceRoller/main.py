from random import randint
from parse_input import parse_input
from roll_dice import roll_dice
from generate_dice_faces import generateDiceFace

def DiceRoller():
    
    # ask for user input
    while True:
        numOfDice = input("Enter number of dice to roll [1-6]: ")
        num_dice = parse_input(numOfDice)
        rolled = roll_dice(num_dice)

        faces = generateDiceFace(rolled)
        print(faces)
        

DiceRoller()