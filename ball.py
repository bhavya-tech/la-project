import pygame
import numpy as np

class Ball:
    ball_radius = 5
    center = np.array([10,10])
    velocity = np.array([0,1])
    color = (255,0,0)

    def __init__(self,x=None,y=None):
        if x == None and y == None:
            pass
        else:
            self.center = np.array([x,y])

    def draw(self,gameDisplay):
        pygame.draw.circle(gameDisplay,self.color,tuple(map(int,self.center)),self.ball_radius)