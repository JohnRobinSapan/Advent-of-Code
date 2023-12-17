# Import the heapq module to use a priority queue
import heapq


# Define a function that takes the start and end coordinates, the minimum and maximum number of moves in one direction, and returns the minimal heat accumulated along the path
def minimal_heat(start, end, min_moves, max_moves):
    # Initialize a priority queue with the starting point, its heat, and its previous direction
    queue = [(0, *start, 0, 0)]
    # Initialize a set to keep track of the visited points
    seen = set()
    # Loop until the queue is empty
    while queue:
        # Pop the point with the lowest heat from the queue
        heat, x, y, prev_x, prev_y = heapq.heappop(queue)
        # Check if the point is the end point
        if (x, y) == end:
            # Return the heat of the end point
            return heat
        # Check if the point has been visited before with the same previous direction
        if (x, y, prev_x, prev_y) in seen:
            # Skip this point
            continue
        # Add the point and its previous direction to the seen set
        seen.add((x, y, prev_x, prev_y))
        # Calculate the possible turns from the current point
        for delta_x, delta_y in {(1, 0), (0, 1), (-1, 0), (0, -1)} - {
            (prev_x, prev_y),
            (-prev_x, -prev_y),
        }:
            # Initialize the next point and its heat
            next_x, next_y, next_heat = x, y, heat
            # Loop from the minimum to the maximum number of moves in one direction
            for i in range(1, max_moves + 1):
                # Update the next point coordinates
                next_x, next_y = next_x + delta_x, next_y + delta_y
                # Check if the next point is on the board
                if (next_x, next_y) in board:
                    # Update the next point heat
                    next_heat += board[next_x, next_y]
                    # Check if the number of moves is at least the minimum
                    if i >= min_moves:
                        # Push the next point, its heat, and its direction to the queue
                        heapq.heappush(
                            queue, (next_heat, next_x, next_y, delta_x, delta_y)
                        )


# Read the board data from a file and store it as a dictionary of coordinates and heat values
board = {
    (row, col): int(heat)
    for row, line in enumerate(open("day_17_clumsy_crucible/data.txt"))
    for col, heat in enumerate(line.strip())
}
# Print the minimal heat for two different cases of minimum and maximum moves
print(minimal_heat((0, 0), max(board), 1, 3))
print(minimal_heat((0, 0), max(board), 4, 10))
