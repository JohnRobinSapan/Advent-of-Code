from functools import reduce

# Read the data from the file and split it into seeds and mappings
seeds, *mappings = (
    open("day_5_if_you_give_a_seed_a_fertilizer/data.txt").read().split("\n\n")
)
# Convert the seeds from strings to integers
seeds = list(map(int, seeds.split()[1:]))


# Define a function that looks up the new positions and lengths after applying the mapping
def lookup(inputs, mapping):
    # Iterate over each input pair of start position and length
    for start, length in inputs:
        # Continue until the entire length has been mapped
        while length > 0:
            # Iterate over each mapping rule
            for m in mapping.split("\n")[1:]:
                # Extract the destination, source, and length from the mapping rule
                dst, src, len = map(int, m.split())
                # Calculate the difference between the current start and the source
                delta = start - src
                # Check if the current start is within the range of the mapping rule
                if delta in range(len):
                    # Adjust the length based on the delta and remaining length
                    len = min(len - delta, length)
                    # Yield the new position and length
                    yield (dst + delta, len)
                    # Update the start and length for the next iteration
                    start += len
                    length -= len
                    break
            # If no mapping rule applies, yield the current position and length
            else:
                yield (start, length)
                break


# Print the minimum destination position for each seed after applying the mappings
# The first list comprehension applies the mappings to each seed individually
# The second list comprehension applies the mappings to pairs of seeds
print(
    *[
        min(reduce(lookup, mappings, s))[0]
        for s in [zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])]
    ]
)
