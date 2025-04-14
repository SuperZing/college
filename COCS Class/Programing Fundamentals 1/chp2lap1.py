#vars
cars_mileage = float(input('Cars mileage: '))
cost_of_gas = float(input('Gas price: '))

#in miles
distances = [20, 75, 500]

#gas cost results for miles
gas_cost_20 = (distances[0]/cars_mileage)*cost_of_gas
gas_cost_75 = (distances[1]/cars_mileage)*cost_of_gas
gas_cost_500 = (distances[2]/cars_mileage)*cost_of_gas

#print results
print(f'{gas_cost_20:.2f} {gas_cost_75:.2f} {gas_cost_500:.2f}')
