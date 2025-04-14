#function definition
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven/miles_per_gallon)*dollars_per_gallon

#main to run the code in script file and not as import 
if __name__=='__main__': #inputs 
    miles_per_gallon = float(input("Cars miles per gallon: "))
    dollars_per_gallon = float(input("Cost of gas per gallon $"))


    #3 function calls with thier miles
    miles_10 = driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    miles_50 = driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    miles_400 = driving_cost(miles_per_gallon, dollars_per_gallon, 400)

    #output
    print(f'\n{miles_10:.2f}\n{miles_50:.2f}\n{miles_400:.2f}')
