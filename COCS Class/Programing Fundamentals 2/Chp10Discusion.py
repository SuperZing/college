#base class (would be way better with time module)
class Package():
    def __init__(self, order_date, package_id):
        self.order_date = order_date.replace('/','') #string 'month/day/year'
        self.package_id = 'id#'+package_id #string 'id#-number'
        self.tracking_number = self.package_id+self.order_date
        self.delivered = False
    
    def set_delivered(self):
        self.delivered = True
    
    def get_info(self):
        print(f'\nPackage ID:{self.package_id}, Order Date: {self.order_date}, Tracking Number: {self.tracking_number}, Delivered: {self.delivered}.')


class PriorityPackage(Package): #derived class
    def __init__(self, order_date, package_id, priority_level):
        Package.__init__(self, order_date, package_id) #get base class constructor
        self.priority_level = priority_level.capitalize().strip() #string 'Priority Mail Express', 'Priority Mail', 'First-Class Mail', etc..
    
    priority_types = {'Priority Mail Express':'1-2 days or overnight delivery up to 70lbs.', 'Priority Mail':'2-3 business day delivery up to 70lbs.', 'First-Class Mail':'1-3 business day delivery of small packages 13oz.'}

    def get_info(self):
        Package.get_info(self)
        print(f'Priority Level:', pri)




#derived class
class AmazonTruck(Package):
    def __init__(self):
        Package.__init__(self, order_date, order_id)
        self.packages = [] #package object list
        self.delivered_packages = [] #deliverd package list

    def add_package(self, package): #add package to packages list
        self.packages.append(package)
    
    def remove_package(self, package):
        if package in self.packages:
            package.set_delivered()
            self.packages.remove(package)
            self.delivered_packages.append(package)

    def delivered_report(self):
        print('--Pending Packages--')
        if self.packages == []:
            print('Empty')
        else:
            for package in self.packages:
                print(package.get_info()) #prints package info

        print('\n--Delivered Packages--')
        if self.delivered_packages == []:
            print('Empty')
        else:
            for package in self.delivered_packages:
                print(package.get_info()) #prints package info
    
normal_package = Package('11/17/2024','1')
normal_package.get_info()

priority_package = PriorityPackage('12/18/2024', '2', 'Priority Mail Express')
priority_package.get_info()

#myTruck = AmazonTruck()
#myTruck.add_package(package1)
#myTruck.add_package(package2)

#myTruck.delivered_report()