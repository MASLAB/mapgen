# MASLAB 2024 Map File Visualizer

This repository will enable you to visualize MASLAB 2024 map files!

## Dependencies

- `pygame 2.1.2`

## Map File Format

Each line on a map file contains one game object.

The origin is located at the top left.  Positive `X` is to the right and
positive `Y` is downwards.

**Note**: the map file `X` and `Y` coordinates are in multiples of *2 feet*.
This is the side length of one foam mat tile.  The `Z` coordinates are in
multiples of *2 inches*.  This is the side length of one game cube.

### Wall

`W, [X1], [Y1], [X2], [Y2]`

`X1, Y1`: The location of the first edge
`X2, Y2`: The location of the second edge

### Bounding Box

`B, [X], [Y]`

`X1, Y1`: The location of the center of the bounding box

### Robot

`R, [X], [Y], [A]`

`X, Y`: The starting location of the robot
`A`: The starting orientation of the robot (positive clockwise, zero is up)

### Cube

`C, [X1], [Y1], [Z], [C]`

`X1, Y1`: The location of the cube
`Z`: The Z coordinate of the bottom face of the cube
`C`: The color of the cube (`R` is red and `G` is green)

### Central Platform

`P, [X1], [Y1], [X2], [Y2]`

`X1, Y1`: The location of the first edge
`X2, Y2`: The location of the second edge

### AprilTags

`A, [X1], [Y1], [C]`

`X1, Y1`: The location of the tag
`C`: The color of the tag's owner (`R` is red and `G` is green)