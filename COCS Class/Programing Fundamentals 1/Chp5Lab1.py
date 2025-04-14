#input and output
password = input('Enter: ')
crypt_password = ''

#dict of letters to change
change = {'i': '1', 'a': '@', 'm':'M', 'B':'8', 's':'$'}

#for loop on password string
for letter in password:
    if letter in change.keys():
        crypt_password += change[letter]
    else:
        crypt_password+=letter
print()
print(f'{crypt_password}!')
