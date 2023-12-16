# Read the input from the file and create a grid represented by a dictionary
# where the keys are complex coordinates (position) and values are characters.
grid = {
    complex(i, j): char
    for j, row in enumerate(open("day_16_the_floor_will_be_lava/data.txt"))
    for i, char in enumerate(row.strip())
}


def traverse_path(start_positions):
    """
    Traverse the grid from the given starting positions and count the number of unique positions visited.

    Args:
        start_positions (list): List of starting positions represented as (position, direction) tuples.

    Returns:
        int: The number of unique positions visited minus 1.
    """
    visited_positions = set()

    while start_positions:
        position, direction = start_positions.pop()

        # Traverse in the specified direction until a breaking condition is met
        while not (position, direction) in visited_positions:
            visited_positions.add((position, direction))
            position += direction

            # Check the character at the current position and update the direction accordingly
            match grid.get(position):
                case "|":
                    direction = 1j
                    start_positions.append((position, -direction))
                case "-":
                    direction = -1
                    start_positions.append((position, -direction))
                case "/":
                    direction = -complex(direction.imag, direction.real)
                case "\\":
                    direction = complex(direction.imag, direction.real)
                case None:
                    break

    # Return the count of unique positions visited minus 1
    return len(set(pos for pos, _ in visited_positions)) - 1


# Start traversing from the initial position (-1, 1) and print the result
print(traverse_path([(-1, 1)]))

# Find the maximum number of unique positions visited starting from each direction
max_result = max(
    map(
        traverse_path,
        (
            [(pos - direction, direction)]
            for direction in (1, 1j, -1, -1j)
            for pos in grid
            if pos - direction not in grid
        ),
    )
)

# Print the maximum result
print(max_result)
