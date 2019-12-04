l_limit = 265275
u_limit = 781584

num_passwords = 0 
def validate_dupe(number):
    num_string = str(number)
    if num_string[0] == num_string[1] or num_string[1] == num_string[2] or num_string[2] == num_string[3] or num_string[3] == num_string[4] or num_string[4] == num_string[5]:
        return True
    return False

def validate_increase(number):
    num_string = str(number)
    if num_string[0] <= num_string[1] <= num_string[2] <= num_string[3] <= num_string[4] <= num_string[5]:
        return True
    return False

for attempt in range(l_limit,u_limit):
    if validate_dupe(attempt) and validate_increase(attempt):
        num_passwords += 1

print(num_passwords)