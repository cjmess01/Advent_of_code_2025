import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()

with open(sys.argv[1], "r") as file:
    lines = [line.strip() for line in file.readlines()]

def make_rotation(start : int, instr : str) -> tuple[int, int]: # Given start and instruction, return new start and num times passed 0

    times_passed_zero = 0
    num_clicks = int(instr[1:])

    full_revolutions = int(num_clicks / 100)
    times_passed_zero += full_revolutions

    sign = 1 if instr[0] == "R" else -1
    remaining_val = sign * (num_clicks - full_revolutions*100)

    intermediate = start + remaining_val

    if start == 0:
        if intermediate < 0:
            intermediate += 100
    elif start > 0 and intermediate < 0:
        intermediate += 100
        times_passed_zero += 1

    if intermediate == 0 :
        times_passed_zero += 1

    elif start > 0 and intermediate > 99:
        intermediate -= 100
        times_passed_zero += 1

    return intermediate, times_passed_zero

start = 50
p0 = 0


for lineno, line in enumerate(lines):
    start, times = make_rotation(start, line)
    p0 += times

print(p0)
print(start)



