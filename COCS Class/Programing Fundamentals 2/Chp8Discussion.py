#input history
history = []

#input
input_string = "Enter one of these: cos, sin, tan, or 'end' to end program & 'his' to see history: "
user_input = input(input_string).lower().strip() #lower and strip for user error

#math dict
math = {'cos':'adjacent/hypotenuse', 'sin':'opposite/hypotenuse', 'tan':'opposite/adjacent'}

while user_input != 'end':
    if user_input in math.keys(): #if in dict keys
        print(f'{user_input} = {math[user_input]}')
        history.append(user_input)
    elif user_input == 'his':
        if history == []: #checks if list is empty
            print('No History')
        else:
            print(f'History: {' '.join(history)}') #prints history
    else:
        print("That's not exactly right... ")

    print() #for empty line
    user_input = input(input_string).lower().strip() #ask for input agian to exit while loop
else: #while loop else statment
    print('\nProgram ended, bye')
