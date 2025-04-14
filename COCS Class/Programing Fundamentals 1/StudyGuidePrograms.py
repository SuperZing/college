#make pyramid
def py(blocks):
    layers = 0
    while layers < blocks:
        layers +=1
        blocks -= layers
    else:
        print(layers)


def h(number):
    flag = True
    steps = 0
    if number > 0:
        n = number
    else:
        print('Number is not whole; ending program')
        flag = False
    while flag and n != 1 and n > 0: #flag first to ignore n var that arent created yet
        steps += 1 #put on top since it won't matter if inside if or else; since one or the other still needs to happen
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        print(n)
    else:
        print(f'steps = {steps}')
