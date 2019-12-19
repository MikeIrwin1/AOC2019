with open('input\\day_5.txt', 'r') as f:
    data = [int(x) for x in (f.read().strip().split(','))]

input = 5
ptr = 0

def addition():
    data[param_3] = data[param_1] + data[param_2]

def multiply():
    data[param_3] = data[param_1] * data[param_2]

def set_input():
    data[param_1] = input

while(int(str(data[ptr])[-2:]) != 99):
    instruction = str(data[ptr]).zfill(5)
    op = int(instruction[-2:])
    param_1 = data[ptr+1] if int(instruction[2]) == 0 else ptr+1
    param_2 = data[ptr+2] if int(instruction[1]) == 0 else ptr+2
    param_3 = data[ptr+3] if int(instruction[0]) == 0 else ptr+3
    if op == 1:
        addition()
        ptr += 4
    elif op == 2:
        multiply()
        ptr += 4
    elif op == 3:
        set_input()
        ptr += 2
    elif op == 4:
        output = data[param_1]
        ptr += 2
    elif op == 5:
        if data[param_1] != 0:
            ptr = data[param_2]
        else: 
            ptr += 3
    elif op == 6:
        if data[param_1] == 0:
            ptr = data[param_2]
        else:
            ptr +=3
    elif op == 7:
        if data[param_1] < data[param_2]:
            data[param_3] = 1
            ptr += 4
        else:
            data[param_3] = 0
            ptr += 4
    elif op == 8:
        if data[param_1] == data[param_2]:
            data[param_3] = 1
            ptr += 4
        else:
            data[param_3] = 0
            ptr += 4       

print('Part 1 Output: ', output)

