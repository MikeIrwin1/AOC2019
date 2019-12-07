with open('input\\day_5.txt', 'r') as f:
    data = [int(x) for x in (f.read().strip().split(','))]

input = 1
ptr = 0

while(ptr < len(data)):
    instruction = str(data[ptr]).zfill(5)
    op = int(instruction[-2:])
    param_1 = data[ptr+1] if int(instruction[2]) == 0 else ptr+1
    param_2 = data[ptr+2] if int(instruction[1]) == 0 else ptr+2
    param_3 = data[ptr+3] if int(instruction[0]) == 0 else ptr+3
    if op == 1:
        data[param_3] = data[param_1] + data[param_2]
        ptr += 4
    elif op == 2:
        data[param_3] = data[param_1] * data[param_2]
        ptr += 4
    elif op == 3:
        data[param_1] = input
        ptr += 2
    elif op == 4:
        output = data[param_1]
        ptr += 2
    elif op == 99:
        break        

print('Part 1 Output: ', output)

