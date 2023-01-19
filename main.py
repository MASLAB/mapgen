# This is a sample Python script. Only works with 2023 map

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
    file = open("2023_test_map.txt", "r")
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split(',')
        elements.append(line_list)
    print(elements)
    buffer = 10

    #set up pygame and board sizes
    pygame.init()
    res = 120
    tileX = 3 #number of board tiles across
    tileY = 3 #num of board tiles
    size = width, height = (tileX+2)* res, (tileY+2) *res #of total board, by numer of tiles
    screen = pygame.display.set_mode(size)
    blockSize = int(res/2) # Set the size of the grid block for every half tile
    print(blockSize)
    
    #draw white dots on grid
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            pygame.draw.circle(screen, (255,255,255), (x,y), 1)

    #insert and SETUP image
    img = pygame.image.load('botpic_cropped.png')

    imgScale = (float(0.5*res), float(0.5*res)) #set this to be height/width in terms of scale of board tile (ie. 0.3 of board tile)
    img = pygame.transform.scale(img, imgScale)
    screen.blit(img, (20,20))

    x_pos = 20
    y_pos = 20
    
    for element in elements:
        print(element)
        n = element[0]
        if  n == 'W':
            #generic wall
            start = (float(element[1])*res, float(element[2])*res)
            end = (float(element[3])*res, float(element[4])*res)
            pygame.draw.line(screen,(0,0,255), start, end, 1)
        if n == 'Y':
            # yellow boundary wall
            start = (float(element[1])*res, float(element[2])*res)
            end = (float(element[3])*res, float(element[4])*res)
            pygame.draw.line(screen, (255, 255, 0), start, end, 1)
        if n == 'B':
            #green boundary box
            start = (float(element[1])*res, float(element[2])*res)
            end = (float(element[3])*res, float(element[4])*res)
            pygame.draw.line(screen, (0, 255, 0), start, end, 1)
        if n == "P":
            #purple boundary
            start = (float(element[1])*res, float(element[2])*res)
            end = (float(element[3])*res, float(element[4])*res)
            pygame.draw.line(screen, (255, 0, 255), start, end, 1)
        if n == "R":
            #red ball
            pygame.draw.circle(screen, (255, 0, 0), (float(element[1])*res, float(element[2])*res), 5)
        if n == "G":
            #green ball
            pygame.draw.circle(screen, (0, 255, 0), (float(element[1])*res, float(element[2])*res) , 5)
        if n == "L":
            arrow(screen, (int(element[1])*blockSize + buffer, height-int(element[2])*blockSize + buffer), element[3])
        
    simulate = True # TODO: CHANGE TO NOT SIMULATE
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if simulate:
                x_change = 0
                y_change = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_DOWN:
                        y_change = 5
                    elif event.key == pygame.K_UP:
                        y_change = -5

                if x_change != 0 or y_change != 0:
                    x_pos += x_change
                    y_pos += y_change
                    screen.blit(img, (x_pos, y_pos))
                    pygame.init()
                    res = 120
                    tileX = 3 #number of board tiles across
                    tileY = 3 #num of board tiles
                    size = width, height = (tileX+2)* res, (tileY+2) *res #of total board, by numer of tiles
                    screen = pygame.display.set_mode(size)
                    blockSize = int(res/2) # Set the size of the grid block for every half tile
  
                    #draw white dots on grid
                    for x in range(0, width, blockSize):
                        for y in range(0, height, blockSize):
                            pygame.draw.circle(screen, (255,255,255), (x,y), 1)

                    x_pos += x_change
                    screen.blit(img, (x_pos, y_pos))
                    pygame.display.update()




