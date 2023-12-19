# Import the regular expression module
import re

# Read the data from the file and split it into two parts: workflow and parts
ll = [x for x in open("day_19_aplenty/data.txt").read().strip().split("\n\n")]
workflow, parts = ll


# Define a function that converts a string into a list of integers
def ints(s):
    return list(map(int, re.findall(r"\d+", s)))


# Convert each line in parts into a list of integers
parts = [ints(l) for l in parts.split("\n")]

# Create a dictionary that maps each work name to its corresponding workflow
workflow = {l.split("{")[0]: l.split("{")[1][:-1] for l in workflow.split("\n")}


# Define a function that evaluates a part based on a given work
def eval2(part, work):
    # Get the workflow for the work
    w = workflow[work]
    # Unpack the part into four variables: x, m, a, and s
    x, m, a, s = part
    # Loop through each item in the workflow
    for it in w.split(","):
        # If the item is "R", return False
        if it == "R":
            return False
        # If the item is "A", return True
        if it == "A":
            return True
        # If the item does not contain ":", recursively evaluate the part with the item as the work
        if ":" not in it:
            return eval2(part, it)
        # Otherwise, split the item into a condition and a work
        cond = it.split(":")[0]
        # Evaluate the condition using the part variables
        if eval(cond):
            # If the condition is true, check the work
            # If the work is "R", return False
            if it.split(":")[1] == "R":
                return False
            # If the work is "A", return True
            if it.split(":")[1] == "A":
                return True
            # Otherwise, recursively evaluate the part with the work
            return eval2(part, it.split(":")[1])
    # If none of the items match, raise an exception
    raise Exception(w)


# Initialize the sum of the part values
p1 = 0

# Loop through each part
for part in parts:
    # If the part is evaluated to be True with the work "in", add its sum to p1
    if eval2(part, "in"):
        p1 += sum(part)
# Print the final value of p1
print(p1)


# Define a function that returns a list of ranges that satisfy both a character and a value condition
def both(ch, gt, val, ranges):
    # Get the index of the character in the string "xmas"
    ch = "xmas".index(ch)
    # Initialize an empty list for the new ranges
    ranges2 = []
    # Loop through each range in the input ranges
    for rng in ranges:
        # Convert the range into a list
        rng = list(rng)
        # Get the lower and upper bounds of the range for the character
        lo, hi = rng[ch]
        # If the condition is greater than, set the lower bound to the maximum of the current lower bound and the value plus one
        if gt:
            lo = max(lo, val + 1)
        # Otherwise, set the upper bound to the minimum of the current upper bound and the value minus one
        else:
            hi = min(hi, val - 1)
        # If the lower bound is greater than the upper bound, skip this range
        if lo > hi:
            continue
        # Update the range for the character with the new bounds
        rng[ch] = (lo, hi)
        # Append the range as a tuple to the new ranges list
        ranges2.append(tuple(rng))
    # Return the new ranges list
    return ranges2


# Define a function that returns a list of ranges that satisfy a given work
def acceptance_ranges_outer(work):
    # Split the workflow for the work into a list of items
    return acceptance_ranges_inner(workflow[work].split(","))


# Define a function that returns a list of ranges that satisfy a list of workflow items
def acceptance_ranges_inner(w):
    # Get the first item in the list
    it = w[0]
    # If the item is "R", return an empty list
    if it == "R":
        return []
    # If the item is "A", return a list of ranges that cover all possible values
    if it == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    # If the item does not contain ":", return the ranges for the item as a work
    if ":" not in it:
        return acceptance_ranges_outer(it)
    # Otherwise, split the item into a condition and a work
    cond = it.split(":")[0]
    # Check if the condition is greater than or less than
    gt = ">" in cond
    # Get the character and the value from the condition
    ch = cond[0]
    val = int(cond[2:])
    # Invert the value based on the condition
    val_inverted = val + 1 if gt else val - 1
    # Get the ranges that satisfy the condition being true
    if_cond_is_true = both(ch, gt, val, acceptance_ranges_inner([it.split(":")[1]]))
    # Get the ranges that satisfy the condition being false
    if_cond_is_false = both(ch, not gt, val_inverted, acceptance_ranges_inner(w[1:]))
    # Return the union of the two lists of ranges
    return if_cond_is_true + if_cond_is_false


# Initialize the product of the range sizes
p2 = 0
# Loop through each range in the ranges for the work "in"
for rng in acceptance_ranges_outer("in"):
    # Initialize the product of the range bounds
    v = 1
    # Loop through each bound in the range
    for lo, hi in rng:
        # Multiply the product by the difference between the bounds plus one
        v *= hi - lo + 1
    # Add the product to p2
    p2 += v
# Print the final value of p2
print(p2)
