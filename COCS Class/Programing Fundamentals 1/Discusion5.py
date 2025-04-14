#Roulette game

import random #imports random module

lives = True #for while loop statment
nums = [1,2,3,4,5,6] #list of six nums
name = input("What's your name: ") #get user name

#helper function to pick random number for npc
def npc_spin():
    if random.choice(nums) == bad_num: #compares npc number and bad_num
        print("Your opponent falls to the ground, you're the last one standing")
        return True
    else:
        print("*He made it, now it's your turn agian\n")
        return False

while lives:
    bad_num = random.choice(nums) #create number/chance for losing
    num = int(input('Choose a number between 1-6: '))
    if num == bad_num: #compares user input to bad_num
        print(f'Everthing fades away..') #losing statment 
        lives = False #ends the while loop
    else:
        print("*You made it, now it's your opponents turn\n")
        if npc_spin(): #using helper fuction for if statment 
            break #ends program since you won
else:
    print(f'This is the end for you {name}, you lose') #else stament for when while loop ends
