# Read the file and create a list of coordinates (x, y) where '#' appears
xs, ys = zip(
    *[
        (x, y)
        for y, row in enumerate(open("day_11_cosmic_expansion/data.txt"))
        for x, char in enumerate(row)
        if char == "#"
    ]
)


# Define a function to calculate the Manhattan distance between points
def dist(points):
    # For each point, calculate the sum of distances to all other points
    distances = [sum((l, 1)[point in points] for point in range(p)) for p in points]
    # Return the total sum of all distances divided by 2 (since each distance is counted twice)
    return sum(abs(a - b) for a in distances for b in distances) // 2


# Calculate and print the sum of distances for two different scenarios
for l in [2, 1_000_000]:
    print(sum(map(dist, [xs, ys])))
