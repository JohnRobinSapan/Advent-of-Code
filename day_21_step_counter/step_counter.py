# Define the value of k
k = 202300

# Define an alias for the enumerate function
n = enumerate

# Create a set I using a set comprehension, extracting relevant characters from data
I = {
    i + j * 1j
    for i, l in n(open("day_21_step_counter/data.txt"))
    for j, c in n(l)
    if "$" < c
}

# Define a lambda function 'e' that calculates the size of a set based on a formula
e = lambda t, L="": len(
    eval(
        "{d for p in" * t + "{65+65j}" + "for d in[p+1,p+1j,p-1,p-1j]if{d%s}&I}" % L * t
    )
)

# Calculate the results using the defined function and constants
part1 = e(64)
part2 = ~-k * (k * (e(132) + e(N := 131)) - e(65)) + k * e(196, ".real%N+d.imag%N*1j")

# Print the final result
print(part1, part2)
