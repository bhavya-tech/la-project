import pygame, ball, bat
import numpy as np

pygame.init()

def main():
    # Screen
    display_width = 600
    display_height = 400
    fps = 60

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Ping Pong')

    # Game objects
    pong = ball.Ball(int(display_width/2), int(display_height/2))
    bat1 = bat.Bat(100,60)
    bat2 = bat.Bat(display_width - 60, display_height - 40)

    # Misc
    clock = pygame.time.Clock()
    crashed = False

    # game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        # Update objects
        pong.center += pong.velocity


        # Game screen update
        gameDisplay.fill((0,200,0))

        pong.draw(gameDisplay)
        bat1.draw(gameDisplay)
        bat2.draw(gameDisplay)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
