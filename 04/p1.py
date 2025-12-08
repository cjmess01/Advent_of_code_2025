import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    lines = file.readlines()

def get_cardinal_directions(i : int, j : int, i_len, j_len, lines) -> dict:
    # Given a location in the map, return a dict with the counts of each character type around it
    character_count = {}
    for x in range(-1,2):
        for y in range(-1,2):
            new_i = i+x
            new_j = j+y
            if new_i < 0 or new_i >= i_len:
                continue
            if new_j < 0 or new_j >= j_len:
                continue
            if x==0 and y==0:
                continue

            new_char = lines[new_i][new_j]
            character_count[new_char] = character_count.get(new_char, 0)+1

    return character_count



sum = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        current_spot = lines[i][j]
        counts = get_cardinal_directions(i,j,len(lines), len(lines[0]), lines)
        # print(counts)
        # print(f"{current_spot} AT {i},{j}")
        if current_spot == '@' and counts.get('@',0) < 4:
            # print(f"{current_spot} AT {i},{j}")
            sum+=1

print(sum)

