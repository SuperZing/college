import random


#user input
user_dice = input('Choose a Dnd dice [d20] [d12] [d10] [d8] [d6] [d4]: ')

#main goal is to remove non-numbers to use int() without errors
#create empty string
#loop all chars in user_dice and only get digits (nums) with .isdigit()
#use .join() function to join output digits
dice_num = int(''.join(char for char in user_dice if char.isdigit()))

#dice roll using values of [1,dice_num]
dice = random.randint(1,dice_num)

#outputs; using a if statment to give diffrent outputs for the randomness 
print('\n')
if dice_num > 20:
    print(f"That's not a standard Dnd dice!") #fix human error
elif dice == 20:
    print(f'YOU GOT A NAT20') #Best Roll
elif dice == 1:
    print(f'PRAY YOU GOT A NAT1') #Worse Roll
else:
    print(f'You roll a {user_dice.lower()} and got a {dice}') #Else


