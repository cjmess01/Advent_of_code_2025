import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]



# I am thinking that any 12 digit number that starts with 1 is larger than an 11 digit that begins with 9

# We should repeatedly grab from the substring the number that fulfills these criteria
# I. The number has at least 12-n numbers behind it, with n being the recursive call we are as
# II. The number is the highest number that fulfills criteria I
# III. The number is the first occurance of the number in II



def get_largest_number_1d( s_num : str ) -> str:
    # Gets the largest 1 digit number in a number
    for i in reversed(range(0,10)):
        if str(i) in s_num:
            return str(i)
    return "0"


def get_largest_number_12d( s_num : str , recursive_calls : int = 0 ) -> str:
    if recursive_calls == 11:
        return get_largest_number_1d(s_num)
    else:
        this_digit = get_largest_number_1d(s_num[0:(-11+recursive_calls)])
        ind = s_num.index(this_digit)
        next_digit = get_largest_number_12d(s_num[ind+1:], recursive_calls+1)
        return this_digit + next_digit

sum = 0
for line in lines:
    sum += int(val:=get_largest_number_12d(line))
    print(val)


print(sum)
