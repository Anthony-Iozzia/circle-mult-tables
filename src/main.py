from enum import Enum
import sys
import matplotlib.pyplot as plt
import numpy as np

table = 2
nb_points = 80
fig_resolution = 150 # dpi
Mode = Enum('Mode', ['STATIC', 'ANIM_MODULO', 'ANIM_TABLE'])
