import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    ranges = [str(item.strip()) for item in file.readline().split(',')]

def is_invalid(number : int) -> bool :
    s_num = str(number)
    if len(s_num) % 2 == 1:
        return False
    half_way = int(len(s_num)/2)
    first_half = int(s_num[0:half_way])
    second_half = int(s_num[half_way:])
    if first_half == second_half:
        return True
    return False

sum = 0
for item in ranges:
    l_b = int(item.split('-')[0])
    u_b = int(item.split('-')[1])
    # print(f"{l_b} to {u_b}")
    for num in range(l_b, u_b+1):
        if is_invalid(num):
            # print(num)
            sum += num

print(sum)
