# use the input function to get the input from the user and the split function to split the sequence. Use list_A as the list variable

list_A = input('listA: ').split()

# use the input function to get the input from the user and the split function to split the sequence. Use list_B as the list variable

list_B = input('listB: ').split()

# Calculate sum of products

result = 0

for index in range(len(list_A)):
    result += int(list_A[index])*int(list_B[index])

#output
print(result)
