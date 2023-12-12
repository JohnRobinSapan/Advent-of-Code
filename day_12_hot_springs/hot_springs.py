import functools

# Read lines from the file and remove any leading/trailing whitespace.
lines = [line.strip() for line in open("day_12_hot_springs/data.txt").readlines()]


# Use functools.lru_cache as a decorator to cache the results of expensive function calls.
@functools.lru_cache(maxsize=None)
def count_patterns(pattern, current_run_length, remaining_runs):
    # Base case: if the pattern is empty, check if a valid solution has been reached.
    if not pattern:
        if current_run_length is None and len(remaining_runs) == 0:
            return 1
        if (
            len(remaining_runs) == 1
            and current_run_length is not None
            and current_run_length == remaining_runs[0]
        ):
            return 1
        return 0

    # Calculate the maximum possible run length that can still be formed.
    possible_extensions = sum(1 for char in pattern if char in "#?")

    # Prune the search space if the remaining pattern cannot satisfy the remaining runs.
    if (
        current_run_length is not None
        and possible_extensions + current_run_length < sum(remaining_runs)
    ):
        return 0
    if current_run_length is None and possible_extensions < sum(remaining_runs):
        return 0
    if current_run_length is not None and len(remaining_runs) == 0:
        return 0

    # Initialize the count of possible patterns.
    count = 0

    # Recursive cases: explore different possibilities based on the first character of the pattern.
    if (
        pattern[0] == "."
        and current_run_length is not None
        and current_run_length != remaining_runs[0]
    ):
        return 0
    if pattern[0] == "." and current_run_length is not None:
        count += count_patterns(pattern[1:], None, remaining_runs[1:])
    if (
        pattern[0] == "?"
        and current_run_length is not None
        and current_run_length == remaining_runs[0]
    ):
        count += count_patterns(pattern[1:], None, remaining_runs[1:])
    if (pattern[0] == "#" or pattern[0] == "?") and current_run_length is not None:
        count += count_patterns(pattern[1:], current_run_length + 1, remaining_runs)
    if (pattern[0] == "?" or pattern[0] == "#") and current_run_length is None:
        count += count_patterns(pattern[1:], 1, remaining_runs)
    if (pattern[0] == "?" or pattern[0] == ".") and current_run_length is None:
        count += count_patterns(pattern[1:], None, remaining_runs)

    return count


# Initialize counters for part 1 and part 2 of the problem.
part1_count = 0
part2_count = 0

# Process each line in the input file.
for line in lines:
    # Split the line into the pattern and the list of required run lengths.
    pattern, run_lengths_str = line.split(" ")
    run_lengths = tuple([int(x) for x in run_lengths_str.split(",")])

    # Solve part 1 of the problem.
    part1_count += count_patterns(pattern, None, run_lengths)

    # Prepare the extended pattern for part 2.
    extended_pattern = "".join("?" + pattern for _ in range(5))

    # Solve part 2 of the problem.
    part2_count += count_patterns(extended_pattern[1:], None, run_lengths * 5)

# Print the results for part 1 and part 2.
print("Part 1:", part1_count)
print("Part 2:", part2_count)