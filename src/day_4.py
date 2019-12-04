l_limit = 265275
u_limit = 781584

num_passwords = 0 
def validate_dupe(number):
    if number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4] or number[4] == number[5]:
        return True
    return False

def validate_increase(number):
    if number[0] <= number[1] <= number[2] <= number[3] <= number[4] <= number[5]:
        return True
    return False

def large_groups(number):
    for digit in number:
        if number.count(digit) == 2:
            return True
    return False


for attempt in range(l_limit,u_limit+1):
    password = str(attempt)
    if validate_dupe(password) and validate_increase(password) and large_groups(password):
        num_passwords += 1

print(num_passwords)