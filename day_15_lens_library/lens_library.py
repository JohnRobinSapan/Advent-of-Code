# Read input data from file and split by commas
input_data = open("day_15_lens_library/data.txt").read().strip().split(",")

# Initialize variables for part 1 and part 2 solutions
part1_solution = 0
part2_solution = 0


# Function to calculate a hash value for a given string
def calculate_hash(input_str):
    hash_value = 0
    for char in input_str:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


# Initialize lists to store lenses and their lengths
lenses = [[] for _ in range(256)]
lens_lengths = [{} for _ in range(256)]

# Process each input line
for index, line in enumerate(input_data):
    # Update part 1 solution by adding the hash value of the current line
    part1_solution += calculate_hash(line)

    # Extract label and calculate hash value for the label
    label = line.split("=")[0].split("-")[0]
    hash_value_label = calculate_hash(label)

    # Check if the line contains "-" or "=" and update lenses and lens_lengths accordingly
    if "-" in line:
        if label in lenses[hash_value_label]:
            lenses[hash_value_label].remove(label)
    if "=" in line:
        if label not in lenses[hash_value_label]:
            lenses[hash_value_label].append(label)
        lens_lengths[hash_value_label][label] = int(line.split("=")[1])

# Calculate part 2 solution based on the given formula
for box, lens_list in enumerate(lenses):
    for position, lens_label in enumerate(lens_list):
        part2_solution += (box + 1) * (position + 1) * lens_lengths[box][lens_label]

# Print the final solutions for part 1 and part 2
print("Part 1 Solution:", part1_solution)
print("Part 2 Solution:", part2_solution)
