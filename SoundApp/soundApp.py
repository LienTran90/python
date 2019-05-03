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
pygame.display.set_caption('Sound App')

line = {'startPoint': [150, 350], 'endPoint': [250, 350]}

player = pygame.Rect(170, 300, 50, 50)
playerImage = pygame.image.load('play.jpg')
playerStretchedImage = pygame.transform.scale(playerImage, (50, 50))
windowSurface.fill(WHITE)

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if player.collidepoint(pygame.mouse.get_pos()):
                print('abc')

    pygame.draw.rect(windowSurface,(0,0,0) , player)
    windowSurface.blit(playerStretchedImage, player)
    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)