import numpy as np

# Time intervals (in seconds)
time = np.array([0, 1, 2, 3, 4])

# Corresponding vertical positions (in meters)
height = np.array([0, 5, 15, 20, 18])

# Calculate displacement
displacement = height[-1] - height[0]

# Calculate total time
total_time = time[-1] - time[0]

# Calculate average velocity
average_velocity = displacement / total_time

print("Displacement:", displacement, "meters")
print("Total Time:", total_time, "seconds")
print("Average Velocity:", average_velocity, "m/s")