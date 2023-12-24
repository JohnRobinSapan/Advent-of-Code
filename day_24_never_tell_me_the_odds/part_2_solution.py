# Import the Z3 library
import z3

# Read the data file and convert each line into a list of integers
# The data file contains the positions and velocities of hailstones
# Each line has the format x,y,z,vx,vy,vz
# where x,y,z are the coordinates and vx,vy,vz are the velocities
# The data is separated by '@' instead of ','
data_file = open("day_24_never_tell_me_the_odds/data.txt")
hailstones = [[int(i) for i in line.replace("@", ",").split(",")] for line in data_file]

# Create a vector of real variables for the position of the rock
# The vector has the format rx,ry,rz,rvx,rvy,rvz
# where rx,ry,rz are the coordinates and rvx,rvy,rvz are the velocities
rock_position = z3.RealVector("r", 6)

# Create a vector of real variables for the time when each hailstone hits the rock
# The vector has the format t1,t2,t3
# where t1 is the time when the first hailstone hits the rock, and so on
hit_times = z3.RealVector("t", 3)

# Create a solver object
solver = z3.Solver()

# Add the constraints that the rock and the hailstones have the same position at the hit times
# This is equivalent to solving the system of equations
# rx + rvx * t1 = x1 + vx1 * t1
# ry + rvy * t1 = y1 + vy1 * t1
# rz + rvz * t1 = z1 + vz1 * t1
# rx + rvx * t2 = x2 + vx2 * t2
# ...
# where xi,yi,zi,vxi,vyi,vzi are the data for the i-th hailstone
for t, hail in zip(hit_times, hailstones):
    for d in range(3):
        solver.add(
            rock_position[d] + rock_position[d + 3] * t == hail[d] + hail[d + 3] * t
        )

# Check if the solver can find a solution
if solver.check() == z3.sat:
    # Get the model (a satisfying assignment) from the solver
    model = solver.model()
    # Print the sum of the coordinates of the rock
    print(model.eval(sum(rock_position[:3])))
else:
    # The solver cannot find a solution
    print("No solution")
