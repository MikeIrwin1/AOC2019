with open('input\\day_2.txt', 'r') as f:
    data = [int(x) for x in (f.read().strip().split(','))]

def solve_part_1(data, noun, verb):
    memory = data[:]
    memory[1] = noun
    memory[2] = verb
    for val in range(0, len(memory) , 4):
        op = memory[val]
        pos1 = memory[val+1]
        pos2 = memory[val+2]
        dest = memory[val+3]
        if op == 1:
            memory[dest] = memory[pos1] + memory[pos2]
        elif op == 2:
            memory[dest] = memory[pos1] * memory[pos2]
        elif op == 99:
            break
    return memory[0]

def solve_part_2(data):
    for noun in range(100):
        for verb in range(100):
            if solve_part_1(data, noun, verb) == 19690720:
                return (100*noun + verb)            

part_1 = solve_part_1(data, 12, 2)
part_2 = solve_part_2(data)
print('Part 1 Output: ', part_1)
print('Part 2 Output: ', part_2)
