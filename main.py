# This is a sample Python script.

import sys, pygame, math

def arrow(screen, position, heading):
    print(position)
    arrow_length = 15
    end = 0
    if heading == "N":
        end = (position[0], position[1] - arrow_length)
    if heading == "S":
        end = (position[0], position[1] + arrow_length)
    if heading == "E":
        end = (position[0] - arrow_length, position[1])
    if heading == "W":
        end = (position[0] + arrow_length, position[1])
    pygame.draw.line(screen, (200,200,200), position, end, 5)
    pygame.draw.circle(screen, (255,255,255), position, 6)

if __name__ == '__main__':
    #open the file, parse it into list format
    elements = []
    file = open("2022_sample_map.txt", "r")
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split(',')
        elements.append(line_list)
    print(elements)
    buffer = 10;
    #set up pygame
    pygame.init()
    size = width, height = 320, 240
    buffered_size = width_buffered, height_buffered = 320 + 2*buffer, 240 + 2*buffer
    screen = pygame.display.set_mode(buffered_size)
    blockSize = 20  # Set the size of the grid block

    #draw the grid
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            pygame.draw.circle(screen, (255,255,255), (x + buffer,height-y + buffer), 1)
    #parse the file
    for element in elements:
        print(element)
        n = element[0]
        if  n == 'W':
            #generic wall
            start = (int(element[1])*blockSize + buffer, height - int(element[2])*blockSize + buffer)
            end = (int(element[3])*blockSize + buffer, height - int(element[4])*blockSize + buffer)
            pygame.draw.line(screen,(0,0,255), start, end, 1)
        if n == 'Y':
            # yellow boundary wall
            start = (int(element[1]) * blockSize + buffer, height - int(element[2]) * blockSize + buffer)
            end = (int(element[3]) * blockSize + buffer, height - int(element[4]) * blockSize + buffer)
            pygame.draw.line(screen, (255, 255, 0), start, end, 1)
        if n == 'B':
            #green boundary box
            start = (int(element[1]) * blockSize + buffer, height - int(element[2]) * blockSize + buffer)
            end = (int(element[3]) * blockSize + buffer, height - int(element[4]) * blockSize + buffer)
            pygame.draw.line(screen, (0, 255, 0), start, end, 1)
        if n == "P":
            #purple boundary
            start = (int(element[1]) * blockSize + buffer, height - int(element[2]) * blockSize + buffer)
            end = (int(element[3]) * blockSize + buffer, height - int(element[4]) * blockSize + buffer)
            pygame.draw.line(screen, (255, 0, 255), start, end, 1)
        if n == "R":
            #red ball
            pygame.draw.circle(screen, (255, 0, 0), (int(element[1])*blockSize + buffer, height - int(element[2])*blockSize + buffer), 5)
        if n == "G":
            #green ball
            pygame.draw.circle(screen, (0, 255, 0), (int(element[1])*blockSize + buffer, height - int(element[2])*blockSize + buffer) , 5)
        if n == "L":
            arrow(screen, (int(element[1])*blockSize + buffer, height-int(element[2])*blockSize + buffer), element[3])
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

