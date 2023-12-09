# Open the file and read the binary sequences into a list of strings
histories = open("day_9_mirage_maintenance/data.txt").readlines()

# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate the binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to calculate the first Lagrange interpolation based on a list of numbers
def Lagrange1(nums):
    n = len(nums)
    res = 0
    for i, x in enumerate(nums):
        res += x * binomial_coefficient(n, i) * (-1) ** (n - 1 - i)
    return res

# Function to calculate the second Lagrange interpolation based on a list of numbers
def Lagrange2(nums):
    n = len(nums)
    res = 0
    for i, x in enumerate(nums):
        res += x * binomial_coefficient(n, i + 1) * (-1) ** i
    return res

# Initialize result variables for the two Lagrange interpolations
res1, res2 = 0, 0

# Iterate over each line in the file
for line in histories:
    # Convert the binary sequence to a list of integers
    nums = list(map(int, line.strip().split()))
    # Calculate and accumulate the results of the two Lagrange interpolations
    res1 += Lagrange1(nums)
    res2 += Lagrange2(nums)

# Print the final results of the two Lagrange interpolations
print(res1,res2)
