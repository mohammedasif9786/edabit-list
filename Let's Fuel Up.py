def calculate_fuel(distance):
    fuel_amount = 10 * distance
    if fuel_amount < 100:
        fuel_amount = 100
    return fuel_amount
print(calculate_fuel(15)) # print(fuel_amount)
print(calculate_fuel(23.5))
print(calculate_fuel(3))
