import pygame
from pygame.locals import *
def drawblock(screen,block, xco, yco):
    screen.fill((112, 15, 63))
    screen.blit(block, (xco, yco))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((1000, 500))
    screen.fill((112, 15, 63))
    pygame.display.flip()

    block = pygame.image.load("snakehead.png").convert_alpha()
    block = pygame.transform.scale(block, (55, 25))
    xco = 100
    yco = 300
    screen.blit(block, (xco,yco))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                yco -=10
            elif event.key == K_DOWN:   
                yco+=10
            elif event.key == K_LEFT:
                xco -=10
            elif event.key == K_RIGHT:   
                xco+=10
            drawblock(screen,block, xco, yco)

pygame.quit()

    
