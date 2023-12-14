# Define a function to transpose a grid of equal-length strings
def transpose_listgrid(grid):
    """Transpose `grid`, where `grid` is a list of equal-length strings."""
    # Use zip to group the characters in each column and join them into strings
    return list(map("".join, zip(*grid)))


# Define a function to apply another function to a value n times
def apply_n_times(f, x, n):
    """
    Apply `f` to `x` `n` times, returning the result.

    Assumes `f` is deterministic and takes one hashable argument.

    Saves time by finding the first cycle, calculating its length, and using that to skip ahead.
    """
    # Initialize a dictionary to store the values seen and their indices
    seen = {}
    # Loop n times
    for i in range(n):
        # Check if x is already seen
        if x in seen:
            # Break the loop if a cycle is found
            break
        # Store x and its index in the dictionary
        seen[x] = i
        # Update x by applying f to it
        x = f(x)
    # If the loop finishes without breaking, return x
    else:
        return x

    # Find the start and length of the cycle
    cycle_start = seen[x]
    cycle_len = i - cycle_start
    # Find the remaining number of iterations after skipping the cycle
    remaining = (n - i) % cycle_len
    # Recursively apply f to x for the remaining iterations
    return apply_n_times(f, x, remaining)


# Define a function to roll a line of characters to the east
def roll_line_east(line):
    # Split the line by "#" and sort each segment in ascending order
    # Join the segments with "#" and return the result
    return "#".join(("".join(sorted(p)) for p in line.split("#")))


# Define a function to roll a line of characters to the west
def roll_line_west(line):
    # Split the line by "#" and sort each segment in descending order
    # Join the segments with "#" and return the result
    return "#".join(("".join(sorted(p, reverse=True)) for p in line.split("#")))


# Define a function to roll a list of lines to the east
def roll_east(lines):
    # Apply the roll_line_east function to each line and return the result
    return [roll_line_east(l) for l in lines]


# Define a function to roll a list of lines to the west
def roll_west(lines):
    # Apply the roll_line_west function to each line and return the result
    return [roll_line_west(l) for l in lines]


# Define a function to roll a list of lines to the north
def roll_north(lines):
    # Transpose the list of lines and roll it to the west
    # Transpose the result and return it
    return transpose_listgrid(roll_west(transpose_listgrid(lines)))


# Define a function to roll a list of lines to the south
def roll_south(lines):
    # Transpose the list of lines and roll it to the east
    # Transpose the result and return it
    return transpose_listgrid(roll_east(transpose_listgrid(lines)))


# Define a function to calculate the load of a list of lines
def calculate_load(lines):
    # Sum the products of the row number and the number of "O" in each row
    # Reverse the order of the rows and start counting from 1
    return sum(r * row.count("O") for r, row in enumerate(lines[::-1], 1))


# Define a function to perform a cycle of rolling operations on a list of lines
def do_a_cycle(lines):
    # Roll the list of lines to the east, south, west, and north in order
    # Return the result
    return roll_east(roll_south(roll_west(roll_north(lines))))


# Define a function to apply a cycle of rolling operations to an input string
def apply_cycle_to_input(data):
    # Split the input string by newline characters and convert it to a list of lines
    # Apply the do_a_cycle function to the list of lines
    # Join the result with newline characters and return it
    return "\n".join(do_a_cycle(data.splitlines()))


# Read the data from a file
data = open("day_14_parabolic_reflector_dish/data.txt").read()
# Print the load of the data after rolling it to the north
print(calculate_load(roll_north(data.splitlines())))

# Apply a cycle of rolling operations to the data one billion times
data = apply_n_times(apply_cycle_to_input, data, 1_000_000_000)
# Print the load of the data after the cycles
print(calculate_load(data.splitlines()))
