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
nodes = [node for node in result_dict if node[-1]=='A']
print(nodes)
binary_sequence = ''.join('1' if char == 'R' else '0' for char in sequence)
print(binary_sequence)
while not path_found:
    step=steps % len(binary_sequence)
    #print(step)
    nodes = [result_dict[node][int(binary_sequence[step])] for node in nodes]
    steps += 1
    found_nodes=0
    for node in nodes:
        if node[-1]=='Z':
            found_nodes+=1
    #if(found_nodes):
        #print(found_nodes)
    if found_nodes==len(nodes):
        path_found = True
        print("Path found in", steps, "steps")
print(len(result_dict))
# print(maps)
