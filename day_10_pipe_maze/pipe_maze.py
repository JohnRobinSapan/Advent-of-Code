# Open the file and read the data
with open("day_10_pipe_maze/data.txt", "r") as f:
    raw_data = f.read()

# Split the data into lines
grid = raw_data.split("\n")
height = len(grid)
width = len(grid[0])

# Initialize the output grid for part 2
output_grid = [[0] * width for _ in range(height)]

# Find the starting position marked by 'S'
start_x, start_y = -1, -1
for i in range(height):
    for j in range(width):
        if "S" in grid[i]:
            start_x = i
            start_y = grid[i].find("S")
print("Starting position:", start_x, start_y)

# Define movement directions and corresponding happy characters
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
happy_chars = ["-7J", "|LJ", "-FL", "|F7"]
start_dirs = []

# Determine valid starting directions
for i in range(4):
    dx, dy = directions[i]
    next_x = start_x + dx
    next_y = start_y + dy
    if (
        0 <= next_x < height
        and 0 <= next_y < width
        and grid[next_x][next_y] in happy_chars[i]
    ):
        start_dirs.append(i)
print("Valid directions:", start_dirs)
start_valid = 3 in start_dirs  # part 2

# Define transformation rules for each direction and character
transform_rules = {
    (0, "-"): 0,
    (0, "7"): 1,
    (0, "J"): 3,
    (2, "-"): 2,
    (2, "F"): 1,
    (2, "L"): 3,
    (1, "|"): 1,
    (1, "L"): 0,
    (1, "J"): 2,
    (3, "|"): 3,
    (3, "F"): 0,
    (3, "7"): 2,
}

# Traverse the maze starting from the first valid direction
current_dir = start_dirs[0]
current_x = start_x + directions[current_dir][0]
current_y = start_y + directions[current_dir][1]
path_length = 1
output_grid[start_x][start_y] = 1  # Part 2
while (current_x, current_y) != (start_x, start_y):
    output_grid[current_x][current_y] = 1  # Part 2
    path_length += 1
    current_dir = transform_rules[(current_dir, grid[current_x][current_y])]
    current_x += directions[current_dir][0]
    current_y += directions[current_dir][1]
print("Length of the path:", path_length)
print("Half of the length:", path_length // 2)

# End Part 1
# Begin Part 2

# Count the number of times the path crosses itself
cross_count = 0
for i in range(height):
    inside = False
    for j in range(width):
        if output_grid[i][j]:
            if grid[i][j] in "|JL" or (grid[i][j] == "S" and start_valid):
                inside = not inside
        else:
            cross_count += inside
print("Number of enclosed areas:", cross_count)
