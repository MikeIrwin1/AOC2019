with open('input\\day_2.txt', 'r') as f:
    data = [int(x) for x in (f.read().strip().split(','))]

def solve_part_1(data):
    data[1] = 12
    data[2] = 2
    for val in range(0, len(data) , 4):
        op = data[val]
        noun = data[val+1]
        verb = data[val+2]
        dest = data[val+3]
        if op == 1:
            data[dest] = data[noun] + data[verb]
        elif op == 2:
            data[dest] = data[noun] * data[verb]
        elif op == 99:
            break
    return data[0]

def solve_part_2(data):
    for noun in range(100):
        for verb in range(100):
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
                if memory[0] == 19690720:
                    print('noun: ', noun, 'verb: ', verb)
                    return (100*noun + verb)
            

# part_1 = solve_part_1(data)
part_2 = solve_part_2(data)
print('output: ', part_2 )

# print(part_2)
# print(data)
