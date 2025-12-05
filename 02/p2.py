import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    ranges = [str(item.strip()) for item in file.readline().split(',')]


def is_invalid(number : int) -> bool:

    # I thought of a bunch of heuristics including a dict with the counts of characters in the substring, but those methods became super convoluted really quickly. I think I need a more simple way. 

    # if a string is made of a bunch of substrings
    # Lets say the main string made of substrings is S, and the individual substring is x. If S is made of x... 

    # We know that x is shorter than S, so if wwe had a larger string, lets say   its S', where we know that S' is composed of 2 S back-to-back. 

    # If then we removed the first and last character of S', then S' would no longer be made of substrings of S. However, at least as many x as were in S would be in S' assuming they repeat cleanly. 

    # and since they would be back to back, they would make up a repeat of S, if and only if S is composed of repeats of x


    s_num = str(number)
    
    double_num = (s_num + s_num)[1:len(s_num)*2-1]
    if s_num in double_num:
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

