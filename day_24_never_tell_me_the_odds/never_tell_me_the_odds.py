# Import the combinations function from itertools module
from itertools import combinations


# Define a function to transpose a matrix
def matrix_transpose(matrix):
    # Use the zip function to swap the rows and columns of the matrix
    # Use the map and list functions to convert the result into a list of lists
    return list(map(list, zip(*matrix)))


# Define a function to get the minor of a matrix at a given row and column
def matrix_minor(matrix, row, col):
    # Use list comprehension to remove the row and column from the matrix
    # Return the resulting matrix
    return [row[:col] + row[col + 1 :] for row in (matrix[:row] + matrix[row + 1 :])]


# Define a function to calculate the determinant of a matrix
def matrix_det(matrix):
    # If the matrix is 2x2, use the formula: ad - bc
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Initialize the determinant to zero
    determinant = 0
    # Loop through the columns of the matrix
    for col in range(len(matrix)):
        # Use the cofactor expansion formula: (-1)^c * a0c * det(M0c)
        # Where a0c is the element at the first row and cth column
        # And M0c is the minor of the matrix at the first row and cth column
        determinant += (
            ((-1) ** col) * matrix[0][col] * matrix_det(matrix_minor(matrix, 0, col))
        )

    # Return the determinant
    return determinant


# Define a function to calculate the inverse of a matrix
# Adapted from: https://stackoverflow.com/a/39881366/3889449
def matrix_inverse(matrix):
    # Calculate the determinant of the matrix
    determinant = matrix_det(matrix)
    # Initialize an empty list to store the cofactors
    cofactors = []

    # Loop through the rows of the matrix
    for row in range(len(matrix)):
        # Initialize an empty list to store the row of cofactors
        row_cofactors = []

        # Loop through the columns of the matrix
        for col in range(len(matrix)):
            # Calculate the minor of the matrix at the current row and column
            minor = matrix_minor(matrix, row, col)
            # Calculate the cofactor of the matrix at the current row and column
            # Use the formula: (-1)^(r+c) * det(Mrc)
            # Where Mrc is the minor of the matrix at the rth row and cth column
            cofactor = ((-1) ** (row + col)) * matrix_det(minor)
            # Append the cofactor to the row of cofactors
            row_cofactors.append(cofactor)

        # Append the row of cofactors to the list of cofactors
        cofactors.append(row_cofactors)

    # Transpose the matrix of cofactors
    cofactors = matrix_transpose(cofactors)

    # Loop through the rows and columns of the matrix of cofactors
    for row in range(len(cofactors)):
        for col in range(len(cofactors)):
            # Divide each element by the determinant of the matrix
            cofactors[row][col] /= determinant

    # Return the inverse matrix
    return cofactors


# Define a function to find the intersection point of two vectors in 2D
# Adapted from: https://stackoverflow.com/a/20677983/3889449
def intersection_2d_forward(point_a, vector_a, point_b, vector_b):
    # Add the vectors to the points to get the end points of the vectors
    point_a1 = (point_a[0] + vector_a[0], point_a[1] + vector_a[1])
    point_b1 = (point_b[0] + vector_b[0], point_b[1] + vector_b[1])
    # Calculate the difference between the x-coordinates and y-coordinates of the points
    dx = (point_a[0] - point_a1[0], point_b[0] - point_b1[0])
    dy = (point_a[1] - point_a1[1], point_b[1] - point_b1[1])

    # Calculate the determinant of the matrix formed by dx and dy
    div = matrix_det((dx, dy))
    # If the determinant is zero, the vectors are parallel and do not intersect
    if div == 0:
        return None, None

    # Calculate the determinant of the matrix formed by the points and their end points
    d = (matrix_det((point_a, point_a1)), matrix_det((point_b, point_b1)))

    # Use Cramer's rule to solve for the x-coordinate of the intersection point
    x = matrix_det((d, dx)) / div
    # Check if the x-coordinate is in the same direction as the vectors
    # If not, the vectors do not intersect in the forward direction
    if (x > point_a[0]) != (vector_a[0] > 0) or (x > point_b[0]) != (vector_b[0] > 0):
        return None, None

    # Use Cramer's rule to solve for the y-coordinate of the intersection point
    y = matrix_det((d, dy)) / div
    # Check if the y-coordinate is in the same direction as the vectors
    # If not, the vectors do not intersect in the forward direction
    if (y > point_a[1]) != (vector_a[1] > 0) or (y > point_b[1]) != (vector_b[1] > 0):
        return None, None

    # Return the intersection point
    return x, y


# Define a function to calculate the difference between two vectors in 3D
def vector_diff(vector_a, vector_b):
    # Subtract the corresponding components of the vectors
    return (
        vector_a[0] - vector_b[0],
        vector_a[1] - vector_b[1],
        vector_a[2] - vector_b[2],
    )


# Define a function to get the coefficient matrix and the constant terms vector
# for the system of equations given by the cross product of two vectors in 3D
def get_equations(point_a, vector_a, point_b, vector_b):
    # Calculate the difference between the x-coordinates, y-coordinates, and z-coordinates of the points
    dx, dy, dz = vector_diff(point_a, point_b)
    # Calculate the difference between the x-components, y-components, and z-components of the vectors
    dvx, dvy, dvz = vector_diff(vector_a, vector_b)

    # The system of equations is given by:
    #   (p - a) X (v - va) == (p - b) X (v - vb)
    # Where p is the unknown point, v is the unknown vector, and X is the cross product
    # Expanding the cross product, we get:
    #   (y - ya) * (vz - vaz) - (z - za) * (vy - vay) == (y - yb) * (vz - vbz) - (z - zb) * (vy - vby)
    #   (z - za) * (vx - vax) - (x - xa) * (vz - vaz) == (z - zb) * (vx - vbx) - (x - xb) * (vz - vbz)
    #   (x - xa) * (vy - vay) - (y - ya) * (vx - vax) == (x - xb) * (vy - vby) - (y - yb) * (vx - vbx)
    # Rearranging the terms, we get:
    #   -dvz * y + dvy * z + dvz * ya - dvy * za == -dvz * yb + dvy * zb
    #   dvz * x - dvx * z - dvz * xa + dvx * za == dvz * xb - dvx * zb
    #   -dvy * x + dvx * y + dvy * xa - dvx * ya == -dvy * xb + dvx * yb
    # Writing this in matrix form, we get:
    #   [0, -dvz, dvy, 0, -dz, dy] * [x, y, z, vx, vy, vz] == b[1] * vb[2] - b[2] * vb[1] - (a[1] * va[2] - a[2] * va[1])
    #   [dvz, 0, -dvx, dz, 0, -dx] * [x, y, z, vx, vy, vz] == b[2] * vb[0] - b[0] * vb[2] - (a[2] * va[0] - a[0] * va[2])
    #   [-dvy, dvx, 0, -dy, dx, 0] * [x, y, z, vx, vy, vz] == b[0] * vb[1] - b[1] * vb
    # Return the coefficient matrix (A) and the constant terms vector (B) for the system of equations
    A = [
        [0, -dvz, dvy, 0, -dz, dy],
        [dvz, 0, -dvx, dz, 0, -dx],
        [-dvy, dvx, 0, -dy, dx, 0],
    ]
    B = [
        point_b[1] * vector_b[2] - point_b[2] * vector_b[1] - (point_a[1] * vector_a[2] - point_a[2] * vector_a[1]),
        point_b[2] * vector_b[0] - point_b[0] * vector_b[2] - (point_a[2] * vector_a[0] - point_a[0] * vector_a[2]),
        point_b[0] * vector_b[1] - point_b[1] * vector_b[0] - (point_a[0] * vector_a[1] - point_a[1] * vector_a[0]),
    ]
    return A, B


# Define a function to multiply a matrix and a vector
def matrix_mul(matrix, vector):
    # Initialize an empty list to store the result
    result = []

    # Loop through the rows of the matrix
    for row in matrix:
        # Use the sum and zip functions to calculate the dot product of the row and the vector
        # Append the dot product to the result list
        result.append(sum(r * v for r, v in zip(row, vector)))

    # Return the result vector
    return result


# Define a function to solve the problem
def solve(hailstones):
    # Unpack the first three hailstones from the list
    (point_a, vector_a), (point_b, vector_b), (point_c, vector_c) = hailstones[:3]

    # Let our 6 unknowns be: p = (x, y, z) and v = (vx, vy, vz)
    # Solve the linear system of 6 equations given by:
    #
    #   (p - a) X (v - va) == (p - b) X (v - vb)
    #   (p - a) X (v - va) == (p - c) X (v - vc)
    #
    # Where X represents the vector cross product.

    # Get the coefficient matrix and the constant terms vector for the first pair of equations
    A1, B1 = get_equations(point_a, vector_a, point_b, vector_b)
    # Get the coefficient matrix and the constant terms vector for the second pair of equations
    A2, B2 = get_equations(point_a, vector_a, point_c, vector_c)
    # Concatenate the two matrices and vectors to get a 6x6 matrix and a 6x1 vector
    A = A1 + A2
    B = B1 + B2

    # Could also use fractions.Fraction to avoid rounding mistakes
    # Calculate the inverse of the coefficient matrix
    A_inv = matrix_inverse(A)
    # Multiply the inverse matrix and the constant terms vector to get the solution vector
    x = matrix_mul(A_inv, B)
    # Round the elements of the solution vector and return the sum of the first three elements
    return sum(map(round, x[:3]))


# Open the input file
fin = open("day_24_never_tell_me_the_odds/data.txt", "r")

# Initialize an empty list to store the hailstones
hailstones = []
# Initialize a variable to store the total number of intersections
total = 0

# Read the input file line by line
with fin:
    for line in fin:
        # Split the line by the @ symbol
        p, v = line.split("@")
        # Split the point and vector by the comma
        p = tuple(map(int, p.split(",")))
        v = tuple(map(int, v.split(",")))
        # Append the point and vector as a tuple to the hailstones list
        hailstones.append((p, v))

# Loop through all the possible pairs of hailstones
for a, b in combinations(hailstones, 2):
    # Find the intersection point of the two hailstones in 2D
    x, y = intersection_2d_forward(*a, *b)
    # If there is no intersection, skip this pair
    if x is None:
        continue

    # Check if the intersection point is within the given range
    xok = 200000000000000 <= x <= 400000000000000
    yok = 200000000000000 <= y <= 400000000000000
    # If both coordinates are within the range, increment the total number of intersections
    total += xok and yok

# Print the answer for part 1
print("Part 1:", total)

# Call the solve function with the hailstones list and print the answer for part 2
answer = solve(hailstones)
print("Part 2:", answer)
