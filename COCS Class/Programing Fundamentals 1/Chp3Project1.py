#my fruits
my_fruit1 = input('My fruit is ')
my_fruit2 = input('My second fruit is ')
my_fruit3 = input('My third fruit is ')

#your fruits
your_fruit1 = input('Your fruit is ')
your_fruit2 = input('Your second fruit is ')

#their fruits
their_fruit = input('Their fruit is ')

#set methods
print()
fruits = {my_fruit1, my_fruit2, my_fruit3} #create set
print(f'{sorted(fruits)}')

fruits.add(your_fruit1)
fruits.add(your_fruit2)
print(f'{sorted(fruits)}') #added your_fruits

fruits.add(their_fruit)
print(f'{sorted(fruits)}') #added their_fruit

fruits.add(your_fruit1)
print(f'{sorted(fruits)}') #added your_fruit

fruits.remove(my_fruit1)
print(f'{sorted(fruits)}') #remove
