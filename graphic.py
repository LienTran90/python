import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
WHITE = (255, 255, 255)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
windowSurface.fill(WHITE)
pygame.display.set_caption('Graphic')


# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 5

GREEN = (0, 255, 0)
RED = (255, 0, 0)

b2 = {'rect': pygame.Rect(250, 200, 20, 20), 'color': GREEN, 'dir': UPLEFT}
boxes = [b2]

line = {'startPoint': [150, 350], 'endPoint': [250, 350]}
myRectX = [];
myRectY = 100;

for rectCount in range(round(WINDOWWIDTH / 20)):
    myRectX.append(rectCount * 20)

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    startPoint = line['startPoint']
    endPoint = line['endPoint']
    if keys[K_LEFT]:
        if startPoint[0] > 0:
            startPoint[0] = startPoint[0] - 10
            line['startPoint'] = startPoint
            endPoint[0] = endPoint[0] - 10
            line['endPoint'] = endPoint
    if keys[K_RIGHT]:
        if endPoint[0] < WINDOWWIDTH:
            startPoint[0] = startPoint[0] + 10
            line['startPoint'] = startPoint
            endPoint[0] = endPoint[0] + 10
            line['endPoint'] = endPoint

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    for b in boxes:
        # Move the box data structure.
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        # Check whether the box has moved out of the window.
        if b['rect'].top < 0 or b['rect'].top < myRectY + 20:
            # The box has moved past the top.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

            positionX =round(b['rect'].left / 20)
            for index in myRectX:
                if index == positionX * 20:
                    myRectX.remove(positionX*20)

        if b['rect'].bottom == startPoint[1]:
            # The box has moved past the bottom.
            if  b['rect'].left > startPoint[0] and b['rect'].left < endPoint[0]:
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT

        if b['rect'].left < 0:
            # The box has moved past the left side.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT

        if b['rect'].right > WINDOWWIDTH:
            # The box has moved past the right side.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        if b['rect'].bottom > startPoint[1] + 20:
            # The box has moved past the bottom.
            pygame.quit()
            sys.exit()

        # Draw the box onto the surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
        pygame.draw.line(windowSurface, RED, line['startPoint'], line['endPoint'], 10)
        for index in myRectX:
            pygame.draw.rect(windowSurface, RED, pygame.Rect(index, myRectY, 20, 20))

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)
