# Read the binary sequence and map data from the file
sequence, *maps = open("day_8_haunted_wasteland/data.txt").read().split("\n")
print(sequence)  # Print the binary sequence

# Initialize an empty dictionary to store the nodes
result_dict = {}

# Process the nodes and store them in the dictionary
for nodes in maps:
    if nodes:  # Check if the line is not empty
        # Split the line into variable name and node parts, stripping whitespace
        variable, nodes_part = map(str.strip, nodes.split("="))
        # Extract the nodes and store them in a list
        nodes_list = [nodes_part[1:4], nodes_part[6:-1]]
        # Assign the list to the corresponding variable in the dictionary
        result_dict[variable] = nodes_list

# Initialize variables for the search
path_found = False  # Flag to indicate when the path is found
steps = 0  # Counter for the number of steps taken
# List of starting nodes (nodes ending with 'A')
nodes = [node for node in result_dict if node[-1] == "A"]

# Search for the path using the binary sequence
while not path_found:
    # Get the current step from the sequence, wrapping around if necessary
    step = sequence[steps % len(sequence)]
    # Count the number of nodes that have reached the destination ('Z')
    found_nodes = sum(1 for node in nodes if node[-1] == "Z")

    # Check if all nodes have reached the destination
    if found_nodes == len(nodes):
        path_found = True  # Set the flag to True
        print("Path found in", steps, "steps")  # Print the result

    # Update the list of nodes based on the current step
    nodes = [result_dict[node][0 if step == "L" else 1] for node in nodes]
    steps += 1  # Increment the step counter

# Print the total number of nodes processed
print(len(result_dict))
