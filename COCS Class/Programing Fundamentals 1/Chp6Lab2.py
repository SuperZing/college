#define function
def feet_to_steps(user_feet):
    step = 2.5 #feet
    return int(user_feet//step)

##main program
user_feet = float(input('Number of feet walked: '))
print()
print(feet_to_steps(user_feet)) #function call
