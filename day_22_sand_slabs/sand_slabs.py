import collections as C
import re


def update_sand_slabs(stack, skip=None):
    # Use defaultdict to store the peaks of each position in the grid
    peaks = C.defaultdict(int)
    falls = 0

    for i, (
        start_row,
        start_col,
        start_height,
        end_row,
        end_col,
        end_height,
    ) in enumerate(stack):
        if i == skip:
            continue

        # Calculate the area affected by the sand slab
        slab_area = [
            (row, col)
            for row in range(start_row, end_row + 1)
            for col in range(start_col, end_col + 1)
        ]

        # Find the maximum peak in the affected area and increment it
        peak = max(peaks[position] for position in slab_area) + 1

        # Update peaks for all positions in the area
        for position in slab_area:
            peaks[position] = peak + end_height - start_height

        # Update the sand slab with the new peak heights
        stack[i] = (
            start_row,
            start_col,
            peak,
            end_row,
            end_col,
            peak + end_height - start_height,
        )

        # Increment falls if the peak is less than the initial height
        falls += peak < start_height

    return not falls, falls


# Read sand slabs data from file and sort them based on initial heights
sand_slabs = sorted(
    [
        [*map(int, re.findall(r"\d+", line))]
        for line in open("day_22_sand_slabs/data.txt")
    ],
    key=lambda slab: slab[2],
)

# Update sand slabs in place
update_sand_slabs(sand_slabs)

# Apply the drop function for each sand slab and print the results
results = [update_sand_slabs(sand_slabs.copy(), skip=i) for i in range(len(sand_slabs))]
print(*map(sum, zip(*results)))
