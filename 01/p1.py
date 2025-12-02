import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()

with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]

def make_rotation(start : int, instr : str) -> int: # Given start and instruction, return new start
    # print(f"{instr[0]} - {instr[1:]}")
    sign = 1 if instr[0] == "R" else -1
    start += sign * int(instr[1:])
    
    if start < 0:
        start %= 100
    elif start > 99:
        start %= 100
    return start

start = 50
count = 0
for line in lines:
    start = make_rotation(start, line)

    count += 1 if start == 0 else 0

print(count)


