# Read data from file
with open("day_23_a_long_walk/data.txt") as file:
    data = file.read().strip().splitlines()

# Part 1
# Create a graph of edges between cells
edges = {}
for row_index, row in enumerate(data):
    for col_index, value in enumerate(row):
        if value == ".":
            # Connect neighboring cells with an edge
            for delta_row, delta_col in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                adj_row, adj_col = row_index + delta_row, col_index + delta_col
                if (
                    0 <= adj_row < len(data)
                    and 0 <= adj_col < len(row)
                    and data[adj_row][adj_col] == "."
                ):
                    edges.setdefault((row_index, col_index), set()).add(
                        (adj_row, adj_col)
                    )
                    edges.setdefault((adj_row, adj_col), set()).add(
                        (row_index, col_index)
                    )
        if value == ">":
            # Connect the current cell to the right
            edges.setdefault((row_index, col_index), set()).add(
                (row_index, col_index + 1)
            )
            edges.setdefault((row_index, col_index - 1), set()).add(
                (row_index, col_index)
            )
        if value == "v":
            # Connect the current cell downwards
            edges.setdefault((row_index, col_index), set()).add(
                (row_index + 1, col_index)
            )
            edges.setdefault((row_index - 1, col_index), set()).add(
                (row_index, col_index)
            )

# Define dimensions of the grid
num_rows, num_cols = len(data), len(data[0])

# BFS to find the longest path
queue = [(0, 1, 0)]  # Starting position and distance
visited = set()
max_distance = 0

while queue:
    current_row, current_col, distance = queue.pop()

    # Handling backtracking
    if distance == -1:
        visited.remove((current_row, current_col))
        continue

    # Check if reached the target position
    if (current_row, current_col) == (num_rows - 1, num_cols - 2):
        max_distance = max(max_distance, distance)
        continue

    # Skip if already visited
    if (current_row, current_col) in visited:
        continue

    visited.add((current_row, current_col))
    queue.append((current_row, current_col, -1))

    # Explore neighbors
    for adj_row, adj_col in edges[(current_row, current_col)]:
        queue.append((adj_row, adj_col, distance + 1))

print("Part 1:", max_distance)

# Part 2
# Create a graph of edges with lengths for Part 2
edges_with_lengths = {}

for row_index, row in enumerate(data):
    for col_index, value in enumerate(row):
        if value in ".>v":
            for delta_row, delta_col in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                adj_row, adj_col = row_index + delta_row, col_index + delta_col
                if (
                    0 <= adj_row < len(data)
                    and 0 <= adj_col < len(row)
                    and data[adj_row][adj_col] in ".>v"
                ):
                    edges_with_lengths.setdefault((row_index, col_index), set()).add(
                        (adj_row, adj_col, 1)
                    )
                    edges_with_lengths.setdefault((adj_row, adj_col), set()).add(
                        (row_index, col_index, 1)
                    )

# Remove nodes with degree 2 by merging the edges
while True:
    for node, adjacent_edges in edges_with_lengths.items():
        if len(adjacent_edges) == 2:
            edge_a, edge_b = adjacent_edges
            edges_with_lengths[edge_a[:2]].remove(node + (edge_a[2],))
            edges_with_lengths[edge_b[:2]].remove(node + (edge_b[2],))
            edges_with_lengths[edge_a[:2]].add(
                (edge_b[0], edge_b[1], edge_a[2] + edge_b[2])
            )
            edges_with_lengths[edge_b[:2]].add(
                (edge_a[0], edge_a[1], edge_a[2] + edge_b[2])
            )
            del edges_with_lengths[node]
            break
    else:
        break

# BFS to find the longest path with lengths
queue = [(0, 1, 0)]  # Starting position and distance
visited = set()
max_distance_with_lengths = 0

while queue:
    current_row, current_col, distance = queue.pop()

    # Handling backtracking
    if distance == -1:
        visited.remove((current_row, current_col))
        continue

    # Check if reached the target position
    if (current_row, current_col) == (num_rows - 1, num_cols - 2):
        max_distance_with_lengths = max(max_distance_with_lengths, distance)
        continue

    # Skip if already visited
    if (current_row, current_col) in visited:
        continue

    visited.add((current_row, current_col))
    queue.append((current_row, current_col, -1))

    # Explore neighbors with lengths
    for adj_row, adj_col, length in edges_with_lengths[(current_row, current_col)]:
        queue.append((adj_row, adj_col, distance + length))

print("Part 2:", max_distance_with_lengths)
