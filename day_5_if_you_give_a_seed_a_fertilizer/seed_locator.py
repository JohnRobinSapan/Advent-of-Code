from functools import reduce

data = {}
current_category = None

with open("day_5_if_you_give_a_seed_a_fertilizer/data.txt", "r") as file:
    for line in file:
        # Strip leading and trailing whitespaces
        line = line.strip()

        # Check if the line is a category line
        if ":" in line:
            current_category = line.split(":")[0]
            # Initialize the list for the current category
            data[current_category] = []
            if line.split(":")[1]:
                items = [int(item) for item in line.split() if item.isdigit()]
                data[current_category].extend(items)
        elif current_category is not None:
            # If it's not a category line and a category is set, process the items
            items = [int(item) for item in line.split()]
            if items:
                data[current_category].append(items)


def lookup(val, m):
    _, ranges = m
    print(_, ranges)
    for r in ranges:
        print(r,_)
        dst, src, n = r
        if src <= val < src + n:
            print(val - src + dst)
            return val - src + dst
        else:
            # print(val)
            return val

# print(list(data.items())[1:])
for s in list(data.items())[0][-1]:
    reduce_maps = reduce(lookup, list(data.items())[1:], int(s))
    print(reduce_maps)

