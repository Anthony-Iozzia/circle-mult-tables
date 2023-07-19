from enum import Enum
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

Mode = Enum('Mode', ['STATIC', 'ANIM_MODULO', 'ANIM_TABLE'])
table = 0
modulo = 0
table_start = 0
table_end = 0
table_step = 0
modulo_start = 0
modulo_end = 0
modulo_step = 0
delay_between_frames_modulo = 0
delay_between_frames_table = 0

########## Settings ########
fig_resolution = 150 # dpi
mode = Mode.STATIC # STATIC, ANIM_MODULO, ANIM_TABLE

if mode == Mode.STATIC:
    table = 2 # multiplication table (supports decimal numbers)
    modulo = 10 # number of points on the circle (integer)
elif mode == Mode.ANIM_MODULO:
    table = 2 # multiplication table (supports decimal numbers)
    modulo_start = 20 # only integer
    modulo_end = 200 # only integer
    modulo_step = 1 # only integer
    delay_between_frames_modulo = 25 # ms (default=200)
elif mode == Mode.ANIM_TABLE:
    table_start = 20 # supports decimal numbers
    table_end = 100 # supports decimal numbers
    table_step = 0.1 # supports decimal numbers
    modulo = 80 # number of points on the circle (integer)
    delay_between_frames_table = 25 # ms (default=200)
############################

# Check that mode is valid
if not isinstance(mode, Mode):
    print("Invalid mode")
    sys.exit(1)

# Ensure that modulo is an integer
modulo = int(modulo)
modulo_start = int(modulo_start)
modulo_end = int(modulo_end)
modulo_step = int(modulo_step)

# Compute the number of decimal places of a number
def nb_decimal_places(number):
    return len(str(number).split('.')[-1]) if isinstance(number, float) else 0

table_current = table_start
modulo_current = modulo_start
table_decimal_places = 0
if mode == Mode.STATIC:
    table_decimal_places = nb_decimal_places(table)
elif mode == Mode.ANIM_MODULO:
    table_decimal_places = 0
elif mode == Mode.ANIM_TABLE:
    table_decimal_places = nb_decimal_places(table_step)

def on_close(event):
    plt.close()
    raise SystemExit

# Create a new figure and configure it
fig, graph = plt.subplots(dpi=fig_resolution)
fig.canvas.manager.window.title("Circular multiplication tables")

# Register the callback function to exit the program when the window is closed
plt.connect('close_event', on_close)

def update_figure(frame=0):
    global table_current
    global modulo_current
    if mode == Mode.ANIM_TABLE:
        table_current += table_step
        modulo_current = modulo
    elif mode == Mode.ANIM_MODULO:
        modulo_current += modulo_step
        table_current = table
    else:
        table_current = table
        modulo_current = modulo
        

    plt.clf() # Clear the previous figure
    graph = plt.gca() # Get the graph
    graph.set_aspect('equal') # set aspect ratio
    graph.set_axis_off() # remove the axes

    # Draw the circle
    radius = 1
    circle = plt.Circle((0, 0), radius, fill=False)
    graph.add_artist(circle)

    # Generate the angles for the points
    angles = np.linspace(np.pi/2, (-3/2)*np.pi, modulo_current, endpoint=False)

    # Compute the x and y coordinates for the points
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)

    # Draw the points
    graph.plot(x, y, color='red', marker='o', linestyle='', markersize=3)
    
    # Add labels to the points: place these labels on a slightly bigger circle
    radius_labels = radius * 1.075
    x_labels = radius_labels * np.cos(angles)
    y_labels = radius_labels * np.sin(angles)
    for i, angle in enumerate(angles):
        label = str(i)
        graph.annotate(label, xy=(x_labels[i], y_labels[i]), horizontalalignment='center', verticalalignment='center')

    # Draw the lines
    for i in range(modulo_current):
        p1 = i
        p2 = int((i * table_current) % modulo_current)
        graph.plot([x[p1], x[p2]], [y[p1], y[p2]], color="black", linestyle="solid", linewidth=0.3)
    
    # Add table and modulo information
    table_current_rounded = round(table_current, table_decimal_places)
    table_current_formatted = f"{table_current_rounded:.{table_decimal_places}f}"
    graph.text(0, radius * 1.35, f"Table: {table_current_formatted}", horizontalalignment='center', verticalalignment='top', fontsize=12, weight='bold')
    graph.text(0, radius * 1.25, f"Modulo: {modulo_current}", horizontalalignment='center', verticalalignment='top', fontsize=12, weight='bold')


if mode == Mode.STATIC:
    update_figure()
elif mode == Mode.ANIM_MODULO:
    nb_frames = modulo_end - modulo_start + 1
    animation = FuncAnimation(fig=plt.gcf(), func=update_figure, frames=nb_frames, interval=delay_between_frames_modulo, repeat=False)
elif mode == Mode.ANIM_TABLE:
    nb_frames = int(1/table_step)*int(table_end - table_start + 1)
    animation = FuncAnimation(fig=plt.gcf(), func=update_figure, frames=nb_frames, interval=delay_between_frames_table, repeat=False)
else:
    print("Error: Invalid mode")
    sys.exit(1)

# Show the figure
plt.show()
