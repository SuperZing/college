
#user input

user_word = input('Enter a palindrome: ')
palindorme = ''

#if statment
for char in user_word:
    if char.isalnum:
        palindorme += char

print(palindorme)
        
