# Write the input statement here. Use the user_input variable to store the input from the user.

user_input = input('Write something: ')

#Assign an empty string to the variable user_input_no_spaces

user_input_no_spaces = ''

# Write the for loop to iterate each character in user_input.

for char in user_input:

    # write an if statement to check if the character is alphanumeric and not a digit. Use string methods to do this.

    if char.isalnum():
        if not(char.isdigit()):
            user_input_no_spaces += char

print(user_input_no_spaces)
