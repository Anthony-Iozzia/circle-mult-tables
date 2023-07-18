import sys
import matplotlib.pyplot as plt
import numpy as np

########## Settings ########
table = 2.5
nb_points = 80
fig_resolution = 150 # dpi
############################

if len(sys.argv) >= 2:
    table = float(sys.argv[1])
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
    p2 = int(round((i * table) % nb_points))
    ax.plot([x[p1], x[p2]], [y[p1], y[p2]], color="black", linestyle="solid", linewidth=0.3)

# Set the aspect ratio of the plot
ax.set_aspect('equal')

# Remove the axes
ax.set_axis_off()

ax.text(0, 1.3, f"Table: {table}", ha='center', va='top', fontsize=12, weight='bold')
ax.text(0, 1.2, f"Modulo: {nb_points}", ha='center', va='top', fontsize=12, weight='bold')

fig.canvas.manager.window.title("Circle multiplication tables")

# Display the plot
plt.show()
