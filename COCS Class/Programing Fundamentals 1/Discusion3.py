import random #random module 

#List/Dicts/vars to use for progarm
small_item_shop = ['sword','sheld','dagger','staff'] #items from store list
player_inventory = {'gold':100,'sword':0,'shield':0,'staff':0} #current inventory dict
con_item = '' #bad item var

def random_con(shop): #helper function for show_shop
    global con_item #gets the con_item var from the global enviroment to modity it
    con_item = random.choice(shop) #random pick from item shop

def show_shop(shop):
    random_con(shop) #uses random_con helper function
    print("\nWelcome to my shop, here are my $100g wears. (M'aiq the Liar)")
    print('-------------------------------------------------------')
    for item in shop: #goes through items in the shop
        print(f'*{item.capitalize()}* ')
    print('-------------------------------------------------------')

def show_inventory():
    print('--PLAYER INVENTORY--')
    for item,amount in player_inventory.items(): #goes through key and values in players_iventory by using .items()
        print(f'{item.capitalize()}:{amount}',end=' ') #method to capitalize first letter
    print('\n-------------------')

def buy(shop):
    player_buy = (input('Item name to buy or leave: ').lower()).strip() #lowercase and remove spaces from string
    
    if player_buy == con_item.lower(): #lower function to remove case-sensitive
        print(f"M'aiq takes your 100g and hands you a broken {con_item} with a smile. (runs away)")
    elif player_buy in small_item_shop: #in is to check for item in list
        print(f"M'aiq takes your 100g and hands you a {player_buy}.")
    else:
        print('Ended up leaving the shop from not finding the item you wanted')
    
show_inventory() #starts showing inventory
show_shop(small_item_shop) #starts the store
buy(small_item_shop) #have the player buy
