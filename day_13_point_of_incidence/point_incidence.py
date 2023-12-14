# Read data from the file and split it into a list of lists
points_list = list(
    map(str.split, open("day_13_point_of_incidence/data.txt").read().split("\n\n"))
)


def find_point_of_incidence(points):
    """
    Find the point of incidence for a given list of points.

    Args:
    - points (list): List of points represented as strings.

    Returns:
    - int: Index of the point of incidence.
    """
    for i in range(len(points)):
        # Check the sum of differences between consecutive elements in reversed and normal order
        if (
            sum(
                c != d
                for rev, norm in zip(points[i - 1 :: -1], points[i:])
                for c, d in zip(rev, norm)
            )
            == search_value
        ):
            return i
    else:
        return 0


# Initialize the search values
search_values = [0, 1]

# Iterate over the search values and print the result
for search_value in search_values:
    # Calculate the sum of the point of incidence for both the original and transposed points
    result_sum = sum(
        100 * find_point_of_incidence(points) + find_point_of_incidence([*zip(*points)])
        for points in points_list
    )

    # Print the result sum for the current search value
    print(result_sum)
