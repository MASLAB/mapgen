"""
MASLAB 2024
Map Generation and Display
"""

import sys
from gamemap import Map

if __name__ == "__main__":
    filename = sys.argv[1]
    testmap = Map(filename)

    print()
    print("Use WASD to move")
    print("Use R to reset the robot")

    testmap.draw()