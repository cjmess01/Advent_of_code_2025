import sys
if(len(sys.argv) < 2):
    print("Include cmd arg for file name")
    exit()
with open(sys.argv[1], "r") as file:
    lines = file.readlines()

ranges = []
item_ids = []
for line in lines:
    if line.strip() == "":
        pass
    elif line.find('-') != -1:
        ranges.append(line.strip())
    else:
        item_ids.append(int(line.strip()))

lower_bounds = []
upper_bounds = []
sum = 0

for range_i in ranges:
    lower_bounds.append(int(range_i.split('-')[0]))
    upper_bounds.append(int(range_i.split('-')[1]))

for item_id in item_ids:
    # print(f"id: {item_id}")
    for i, l_b in enumerate(lower_bounds):
        # print(f"l_b: {l_b}")
        if item_id < l_b: # skip if less than lower bound
            continue
        if item_id <= upper_bounds[i]:
            # print(f"u_b: {upper_bounds[i]}")
            # print("SUCCESS")
            sum+=1
            # print(item_id)
            break


        # if 
print(sum)
