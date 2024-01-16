"""
MASLAB 2024
Constructs a Map object from a map file
"""

import sys
from pygame import init, draw, Rect, display, event, QUIT, image, transform

# Set commonly used colors
BLACK = (0, 0, 0)
RED = (237, 54, 26)
GREEN = (19, 217, 9)
BLUE = (61, 175, 219)
GRAY = (227, 221, 107)
LIGHT_RED = (255, 135, 135)
LIGHT_GREEN = (199, 224, 164)
WHITE = (255, 255, 255)

# Set pixels per foot
PPF = 60

# Set tile width (in feet)
TILE_WIDTH = 2

# Set cube width (in pixels)
WIDTH = 20

# Set robot width (in pixels)
ROBOT_WIDTH = 60

# Set bounding box width (in inches)
BOX_WIDTH_IN = 20

# Set bounding box width (in pixels)
BOX_WIDTH = BOX_WIDTH_IN / 12 * PPF

# Set Z spacing of cubes (in pixels)
ZSPACING = 8

# Set dimensions of board
XTILES = 5
YTILES = 4

# Set size of 2-foot game tile
RESOLUTION = TILE_WIDTH * PPF

# Set X and Y offsets (in pixels)
XOFF = RESOLUTION / 2
YOFF = RESOLUTION / 2

# Set board dimensions
SIZE = XTILES * RESOLUTION + 2 * XOFF, YTILES * RESOLUTION + 2 * YOFF

class Map:
    def __init__(self, filename):
        """
        Constructs a new map from an input file
        """
        # Read input file
        with open(filename, "r") as f:
            data = f.read()

        # Parse map file
        w, x, p, b, a, r = self.parse(data)
        
        # Initialize data lists
        self.walls = w
        self.platforms = p
        self.box = x
        self.cubes = b
        self.apriltags = a
        self.robot = r

    def draw(self):
        # Initialize pygame
        init()

        # Set up pygame screen
        width, height = SIZE
        self.screen = display.set_mode(SIZE)

        self.screen.fill(BLACK)
        display.flip()

        # Draw grid coordinates
        x = XOFF
        while x <= width:
            y = YOFF
            while y <= height:
                draw.circle(self.screen, WHITE, (x, y), 1)
                y += RESOLUTION
            x += RESOLUTION

        # Draw walls
        for wall in self.walls:
            draw.line(self.screen, *wall)

        # Draw bounding box
        for box in self.box:
            draw.line(self.screen, *box)

        # Draw cubes
        for cube in self.cubes:
            draw.rect(self.screen, *cube)

        # Draw platforms
        for platform in self.platforms:
            draw.line(self.screen, *platform)

        # Draw AprilTags
        for tag in self.apriltags:
            draw.rect(self.screen, *tag)

        # Draw robot
        if not (self.robot is None):
            self.screen.blit(*self.robot)

        # Update display
        display.update()

        # Wait for QUIT
        while True:
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()
            
    def parse(self, data):
        """
        Parses map data
        """
        # Prepare data file
        rows = [r.strip() for r in data.split("\n") if len(r.strip()) > 0 and r[0] != "#"]

        # Initialize object lists
        walls = []
        box = []
        platforms = []
        cubes = []
        apriltags = []

        # Initialize robot
        robot = None

        # Iterate through objects
        for row in rows:
            values = [v.strip() for v in row.split(",")][1:]

            match row[0]:

                # Wall
                case "W":
                    x1, y1, x2, y2 = [float(v) for v in values]
                    walls.append((BLUE, (x1 * RESOLUTION + XOFF, y1 * RESOLUTION + YOFF), (x2 * RESOLUTION + XOFF, y2 * RESOLUTION + YOFF), 2))

                # Bounding box
                case "B":
                    xc, yc = [float(v) for v in values]
                    box.append((GREEN, (xc * RESOLUTION + XOFF - BOX_WIDTH / 2, yc * RESOLUTION + YOFF - BOX_WIDTH / 2), (xc * RESOLUTION + XOFF + BOX_WIDTH / 2, yc * RESOLUTION + YOFF - BOX_WIDTH / 2), 1))
                    box.append((GREEN, (xc * RESOLUTION + XOFF + BOX_WIDTH / 2, yc * RESOLUTION + YOFF - BOX_WIDTH / 2), (xc * RESOLUTION + XOFF + BOX_WIDTH / 2, yc * RESOLUTION + YOFF + BOX_WIDTH / 2), 1))
                    box.append((GREEN, (xc * RESOLUTION + XOFF + BOX_WIDTH / 2, yc * RESOLUTION + YOFF + BOX_WIDTH / 2), (xc * RESOLUTION + XOFF - BOX_WIDTH / 2, yc * RESOLUTION + YOFF + BOX_WIDTH / 2), 1))
                    box.append((GREEN, (xc * RESOLUTION + XOFF - BOX_WIDTH / 2, yc * RESOLUTION + YOFF + BOX_WIDTH / 2), (xc * RESOLUTION + XOFF - BOX_WIDTH / 2, yc * RESOLUTION + YOFF - BOX_WIDTH / 2), 1))

                # Robot
                case "R":
                    x1, y1 = [float(v) for v in values[0:2]]
                    angle = 180 - float(values[2]) # negative for clockwise rotation

                    img = image.load("botpic_cropped.png")
                    imgScale = (float(ROBOT_WIDTH), float(ROBOT_WIDTH))
                    img = transform.scale(img, imgScale)
                    img = transform.rotate(img, angle)

                    robot = (img, (x1 * RESOLUTION - ROBOT_WIDTH / 2 + XOFF, y1 * RESOLUTION - ROBOT_WIDTH / 2 + YOFF))

                # Cube
                case "C":
                    x1, y1, z1 = [float(v) for v in values[0:3]]
                    color = RED if values[3].upper() == "R" else GREEN
                    cubes.append((color, Rect(x1 * RESOLUTION - WIDTH/2 + (z1 - 1) * ZSPACING + XOFF, y1 * RESOLUTION - WIDTH/2 - (z1 - 1) * ZSPACING + YOFF, WIDTH, WIDTH)))

                # Platform
                case "P":
                    x1, y1, x2, y2 = [float(v) for v in values]
                    platforms.append((GRAY, (x1 * RESOLUTION + XOFF, y1 * RESOLUTION + YOFF), (x2 * RESOLUTION + XOFF, y2 * RESOLUTION + YOFF), 10))

                # AprilTag
                case "A":
                    x1, y1 = [float(v) for v in values[0:2]]
                    color = LIGHT_RED if values[2].upper() == "R" else LIGHT_GREEN
                    apriltags.append((color, Rect(x1 * RESOLUTION - WIDTH/2 + XOFF, y1 * RESOLUTION - WIDTH/2 + YOFF, WIDTH, WIDTH)))

                case other:
                    raise Exception(f"Did not recognize game object: {other}")
        
        return walls, box, platforms, cubes, apriltags, robot