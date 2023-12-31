import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

########## Settings ########
table_start = 20
table_end = 100
step = 0.05
nb_points = 200
fig_resolution = 150 # dpi
delay_between_frames = 10 # ms (default=200)
############################

table_current = table_start

def nb_decimal_places(number):
    return len(str(number).split('.')[-1]) if isinstance(number, float) else 0

def update_figure(frame):
    plt.clf()  # Clear the current figure

    global table_current
    table_current += step

    # Generate the angles for the points
    angles = np.linspace(np.pi/2, (-3/2)*np.pi, nb_points, endpoint=False)

    # Compute the x and y coordinates for the points
    x = np.cos(angles)
    y = np.sin(angles)

    # Get the current figure and axes
    fig = plt.gcf()
    ax = plt.gca()

    # Draw the circle
    circle = plt.Circle((0, 0), 1, fill=False)
    ax.add_artist(circle)

    # # Draw the points
    # ax.plot(x, y, 'ro', markersize=3) # r=red, o=circle

    # # Add labels for the points
    # for i, angle in enumerate(angles):
    #     ax.annotate(str(i), xy=(x[i], y[i]), xytext=(x[i]+0.1, y[i]+0.1))

    # Draw the lines
    for i in range(nb_points):
        p1 = i
        p2 = int((i * table_current) % nb_points)
        ax.plot([x[p1], x[p2]], [y[p1], y[p2]], 'k-', linewidth=0.3) # b=blue, -=solid line

    # Set the aspect ratio of the plot
    ax.set_aspect('equal')

    # Remove the axes
    ax.set_axis_off()

    decimal_places = nb_decimal_places(step)
    value = round(table_current,decimal_places)
    formatted_value = f"{value:.{decimal_places}f}"
    ax.text(0, 1.3, f"Table: {formatted_value}", ha='center', va='top', fontsize=12, weight='bold')
    ax.text(0, 1.2, f"Modulo: {nb_points}", ha='center', va='top', fontsize=12, weight='bold')

def on_close(event):
    plt.close()
    raise SystemExit

# Set the figure resolution
plt.rcParams['figure.dpi'] = fig_resolution

# Create the animation
animation = FuncAnimation(fig=plt.gcf(), func=update_figure, frames=int(1/step)*int(table_end - table_start + 1), interval=delay_between_frames, repeat=False)

plt.gcf().canvas.manager.window.title("Circle multiplication tables")

# Register the callback function to exit the program when the window is closed
plt.connect('close_event', on_close)

# Display the animation
plt.show()
