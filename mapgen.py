"""
MASLAB 2024
Map file generation
"""

from random import choice
from math import degrees, acos

# Set the starting coordinate
START = (0, 0)

# Store the possible steps
STEPS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]

# Set the direction of the last step
LAST_STEP = None

def internal_angle(this):
    """
    Compute the most recent internal angle
    """
    if LAST_STEP is not None:
        return degrees(acos(LAST_STEP[0] * this[0] + LAST_STEP[1] * this[1]))
    else:
        return 90.0

# TODO: implement the rest of this
pass