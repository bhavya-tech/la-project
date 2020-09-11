import pygame, ball, bat
import numpy as np

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ping Pong')

pong = ball.Ball()
bat1 = bat.Bat()

clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((0,200,0))

    pong.draw(gameDisplay)
    bat1.draw(gameDisplay)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()