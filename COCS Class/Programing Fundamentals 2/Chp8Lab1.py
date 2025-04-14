# User inputs string w/ numbers

user_input = input('Enter non-negative numbers: ')

 

# Write the code to split into separate strings

numbers = user_input.split()

# create an empty list called input_data

input_data = []

# Convert strings to floats using for loop

for num in numbers:
    input_data.append(float(num))

# Get max_value and average_value from the input_data

max_value = max(input_data)
average_value = sum(input_data)/len(input_data)

#Print values formatted to 2 decimal places

print(f'{max_value:.2f} {average_value:.2f}')