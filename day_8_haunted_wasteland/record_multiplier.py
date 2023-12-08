sequence, *maps = open("day_8_haunted_wasteland/data.txt").read().split("\n")
print(sequence)
result_dict = {}  # Initialize an empty dictionary

for nodes in maps:
    if nodes:
        variable, nodes_part = map(str.strip, nodes.split("="))
        nodes_list = [nodes_part[1:4], nodes_part[6:-1]]
        result_dict[variable] = nodes_list

path_found = False
steps = 0
node = 'AAA'
binary_sequence = ''.join('1' if char == 'R' else '0' for char in sequence)
print(binary_sequence)
while not path_found:
    node =  result_dict[node][binary_sequence[steps]]
    steps += 1
    if node == "ZZZ":
        path_found = True
        print("Path found in ", steps, "steps")
print(len(result_dict))
# print(maps)
