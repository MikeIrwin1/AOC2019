with open('input\\day_1.txt', 'r') as f:
    data = [int(i.split('\n')[0]) for i in f]

def module_fuel(module_mass):
    return module_mass//3 - 2

def solve_part_1(data):
    total_fuel = 0
    for item in data:
        total_fuel += module_fuel(item)
    return total_fuel

def solve_part_2(data):
    total_fuel = 0
    additional_fuel = 0
    for item in data:
        additional_fuel = module_fuel(item)

        while additional_fuel > 0:
            total_fuel += additional_fuel
            additional_fuel = module_fuel(additional_fuel)
    return total_fuel

part_1 = solve_part_1(data)
part_2 = solve_part_2(data)
print(part_1)
print(part_2)
