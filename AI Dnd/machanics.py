### Dnd Machanics ###
from random import randint

def dice_roll(dice_num): #for dices (if rolling for dices use dice_roll function)
    return randint(1,dice_num)

def roll_stats(): #It's a dictonary right now
    return {'str':randint(8,20),
        'dex':randint(8,20),
        'con':randint(8,20),
        'int':randint(8,20),
        'wis':randint(8,20),
        'cha':randint(8,20)}

def get_coins(): #maybe item file or soemthing idk
    pass