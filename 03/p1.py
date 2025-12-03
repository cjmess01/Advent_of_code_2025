import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]


def get_largest_number_1d( s_num : str ) -> str:
    # Gets the largest 1 digit number in a number
    for i in reversed(range(0,10)):
        if str(i) in s_num:
            return str(i)
    return "0"


def get_largest_number_2d( s_num : str ) -> int:
    tens_place = get_largest_number_1d(s_num[0:-1])
    ones_place = get_largest_number_1d(s_num[s_num.index(tens_place)+1:])
    result = int(tens_place + ones_place)

    # print(f"TEN: {tens_place}")
    # print(f"ONE: {ones_place}")
    # print(f"SO: {result}")
    return result



sum = 0
for line in lines:
    sum += (val:=get_largest_number_2d(line))


print(sum)

