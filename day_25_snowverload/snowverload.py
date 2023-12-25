# Import the math and random modules
import math, random

# Initialize an empty set of vertices
vertices = set()

# Initialize an empty set of edges
edges = set()

# Open the data file and read each line
for line in open("day_25_snowverload/data.txt"):
    # Split the line by spaces and assign the first element to vertex and the rest to neighbors
    vertex, *neighbors = line.replace(":", " ").split()
    # Add the vertex and its neighbors to the set of vertices
    vertices |= {vertex, *neighbors}
    # Add the pairs of vertex and neighbor to the set of edges
    edges |= {(vertex, neighbor) for neighbor in neighbors}

# Define a function that returns the subset that contains a given vertex
subset_of = lambda vertex: next(subset for subset in subsets if vertex in subset)

# Repeat until a valid partition is found
while True:
    # Initialize a list of subsets, each containing one vertex
    subsets = [{vertex} for vertex in vertices]

    # Repeat until there are only two subsets left
    while len(subsets) > 2:
        # Pick a random edge from the set of edges
        vertex1, vertex2 = random.choice([*edges])
        # Find the subsets that contain the two vertices of the edge
        subset1, subset2 = map(subset_of, (vertex1, vertex2))
        # If the subsets are different, merge them into one and remove the other
        if subset1 != subset2:
            subset1 |= subset2
            subsets.remove(subset2)
    # If the number of edges between the two subsets is less than 4, break the loop
    if sum(subset_of(vertex1) != subset_of(vertex2) for vertex1, vertex2 in edges) < 4:
        break

# Print the product of the lengths of the two subsets
print(math.prod(map(len, subsets)))
