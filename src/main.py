from enum import Enum
import sys
import matplotlib.pyplot as plt
import numpy as np

table = 2 # multiplication table
modulo = 80 # number of points on the circle
fig_resolution = 150 # dpi
Mode = Enum('Mode', ['STATIC', 'ANIM_MODULO', 'ANIM_TABLE'])
mode = Mode.STATIC


# Create a new figure and configure it
fig, graph = plt.subplots(dpi=fig_resolution)
fig.canvas.manager.window.title("Circle multiplication tables")
graph.set_aspect('equal') # set aspect ratio
graph.set_axis_off() # remove the axes

graph.text(0, 1.3, f"Table: {table}", ha='center', va='top', fontsize=12, weight='bold')
graph.text(0, 1.2, f"Modulo: {modulo}", ha='center', va='top', fontsize=12, weight='bold')

if mode == Mode.STATIC:
    print("static")
elif mode == Mode.ANIM_MODULO:
    print("anim_modulo")
elif mode == Mode.ANIM_TABLE:
    print("anim_table")
else:
    print("Error: Invalid mode")
    sys.exit(1)

### CIRCLE ###
# Draw the circle
circle = plt.Circle((0, 0), 1, fill=False)
graph.add_artist(circle)

### POINTS ###
# Generate the angles for the points
angles = np.linspace(np.pi/2, (-3/2)*np.pi, modulo, endpoint=False)

# Compute the x and y coordinates for the points
x = np.cos(angles)
y = np.sin(angles)

# Draw the points
# ax.plot(x, y, 'ro', markersize=0) # r=red, o=circle

# Add labels for the points
# for i, angle in enumerate(angles):
#     ax.annotate(str(i), xy=(x[i], y[i]), xytext=(x[i]+0.1, y[i]+0.1))

### LINES ###
# Draw the lines
for i in range(modulo):
    p1 = i
    p2 = (i * table) % modulo
    graph.plot([x[p1], x[p2]], [y[p1], y[p2]], color="black", linestyle="solid", linewidth=0.3)

### DISPLAY ###
plt.show()
