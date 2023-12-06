from functools import reduce

# Read the data from the file and split each race into a list of its elements
races = [race.split()[1:] for race in open("day_6_wait_for_it/data.txt")]
# Zip the first and last elements of each race to create a list of tuples
races = list(zip(races[0], races[-1]))
# Print the list of tuples
print((races))


# Define a generator function that calculates the number of ways the record can be beaten
def time(length, record):
    ways = 0
    # Iterate over possible times
    for time in range(length + 1):
        # Check if the current time beats the record
        if time * (length - time) > record:
            ways += 1
            # Uncomment the next line to print each calculation (for debugging)
            # print(length - time, time * (length - time))
    # Yield the total number of ways the record can be beaten
    yield ways


# Define a function that calculates the product of all ways from the races
def result(races):
    # Use reduce to multiply all the ways together
    return reduce(
        lambda x, y: x * y,
        # Use a list comprehension to get the first value from each generator
        [next(time(int(length), int(record))) for length, record in races],
    )


# Create a generator that joins the corresponding elements from each tuple in races
result_iterator = ("".join([t[i] for t in races]) for i in range(len(races[0])))

# Initialize an empty list to hold the combined results
combined = []
# Append the tuple of joined strings to the combined list
combined.append(tuple(result_iterator))

# Print the result of the races and the combined result
print(
    result(races),
    result(combined),
)
