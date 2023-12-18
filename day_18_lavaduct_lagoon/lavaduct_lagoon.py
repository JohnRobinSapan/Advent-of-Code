# Read the data file and split each line into a list of three elements
data = list(map(str.split, open("day_18_lavaduct_lagoon/data.txt")))

# Define a dictionary that maps directions to x and y increments
directions = {
    "R": (1, 0),  # Right: increase x by 1, keep y the same
    "D": (0, 1),  # Down: increase y by 1, keep x the same
    "L": (-1, 0),  # Left: decrease x by 1, keep y the same
    "U": (0, -1),  # Up: decrease y by 1, keep x the same
    "0": (1, 0),  # Same as R
    "1": (0, 1),  # Same as D
    "2": (-1, 0),  # Same as L
    "3": (0, -1),  # Same as U
}


# Define a function that takes an iterable of steps and returns the final answer
def calculate_answer(steps, position=0, answer=1):
    # Loop through each step
    for (x_increment, y_increment), number in steps:
        # Update the position by adding the x and y increments multiplied by the number
        position += x_increment * number
        # Update the answer by adding the y increment multiplied by the position and the number, plus half the number
        answer += y_increment * position * number + number / 2

    # Return the answer as an integer
    return int(answer)


# Print the answers for part 1 and part 2
print(
    # Part 1: use the first and second elements of each line as direction and number
    calculate_answer(
        (directions[direction], int(number)) for direction, number, _ in data
    ),
    # Part 2: use the third element of each line as a hexadecimal string, and extract the direction and number from it
    calculate_answer(
        (directions[hex_string[7]], int(hex_string[2:7], 16))
        for _, _, hex_string in data
    ),
)
