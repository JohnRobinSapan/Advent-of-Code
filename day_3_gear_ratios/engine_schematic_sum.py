import math as m

# Open the file and read the lines into a list called 'board'
board = list(open("day_3_gear_ratios/data.txt"))

# Create a dictionary to store characters that are not numbers or dots
chars = {
    (r, c): []
    for r in range(140)
    for c in range(140)
    if board[r][c] not in "01234566789."
}

# Iterate over each row and character in the board
for r, row in enumerate(board):
    # Initialize an empty string to keep track of consecutive digits
    consecutive_digits = ""
    for c, char in enumerate(row):
        # Check if the character is a digit
        if char.isdigit():
            # If it is, add it to the string of consecutive digits
            consecutive_digits += char
        elif consecutive_digits:
            # If the current character is not a digit and we have
            # consecutive digits, process them
            start = c - len(consecutive_digits) - 1
            end = c + 1
            edge = {(r, c) for r in (r - 1, r, r + 1) for c in range(start, end)}

            # Add the integer value of the consecutive digits to the
            # corresponding positions in the 'chars' dictionary
            for o in edge & chars.keys():
                chars[o].append(int(consecutive_digits))
            # Reset the string of consecutive digits
            consecutive_digits = ""

# Calculate the sum of sums and the product of pairs
sum_of_sums = sum(sum(p) for p in chars.values())
product_of_pairs = sum(m.prod(p) for p in chars.values() if len(p) == 2)

# Print the results
print(sum_of_sums, product_of_pairs)
