#function definition
def days_in_feb(user_year):
    if user_year%4 == 0:
        days = 29
        if user_year%100 == 0 and not(user_year%400 == 0):
            days = 28
    else:
        days = 28
    return days

#program
if __name__ == '__main__':
    
    user_year = int(input('Year: '))
    
    #function call
    print(f'{user_year} has {days_in_feb(user_year)} days in February.')
