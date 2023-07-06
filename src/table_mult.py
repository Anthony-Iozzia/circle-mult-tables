import sys
import matplotlib.pyplot as plt
import numpy as np

########## Settings ########
table = 84
nb_points = 84
fig_resolution = 150 # dpi
############################

if len(sys.argv) >= 2:
    table = int(sys.argv[1])
if len(sys.argv) >= 3:
    nb_points = int(sys.argv[2])

# Generate the angles for the points
angles = np.linspace(np.pi/2, (-3/2)*np.pi, nb_points, endpoint=False)

# Compute the x and y coordinates for the points
x = np.cos(angles)
y = np.sin(angles)

# Create a new figure
fig, ax = plt.subplots(dpi=fig_resolution)

# Draw the circle
circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(circle)

# Draw the points
# ax.plot(x, y, 'ro', markersize=0) # r=red, o=circle

# Add labels for the points
# for i, angle in enumerate(angles):
#     ax.annotate(str(i), xy=(x[i], y[i]), xytext=(x[i]+0.1, y[i]+0.1))

# Draw the lines
for i in range(nb_points):
    p1 = i
    p2 = (i * table) % nb_points
    ax.plot([x[p1], x[p2]], [y[p1], y[p2]], 'k-', linewidth=0.3) # b=blue, -=solid line

# Set the aspect ratio of the plot
ax.set_aspect('equal')

# Hide the axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

# Display the plot
plt.show()
