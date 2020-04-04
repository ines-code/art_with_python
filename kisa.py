import pygame
import pygame.gfxdraw

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

white = (255,255,255)
blue = (0,51,102)

black = (0,0,0)

running = True

def draw_flat_line(screen, x, y, length, color):
    for i in range(length):
        pygame.gfxdraw.pixel(screen, x, y + i, color)

import random   

while running:
    screen.fill(blue)
    for i in range(100):
        thisX, thisY = (random.randrange(0,screenWidth), random.randrange(0,screenHeight))
        thisLength = random.randrange(0,100)
        draw_flat_line(screen, thisX, thisY, thisLength, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    
