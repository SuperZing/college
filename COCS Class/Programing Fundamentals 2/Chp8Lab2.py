services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 
'Wax' : 3, 'Vacuum' : 5 }

base_wash = 10

total = 0

 

service_choice1 = input()

service_choice2 = input()

 

###my code###
def service_order(serv):
    if serv in services.keys():
        print(f'{serv} - ${services[serv]}')
        return services[serv]
    return 0

print(f'BlueCar Wash\nBase car wash - $10') #default car wash service

total = base_wash+service_order(service_choice1)+service_order(service_choice2) #service options

print(f'-----\nTotal price: ${total}\n') #total cost
