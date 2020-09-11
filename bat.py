import pygame
import numpy as np

class Bat:
    width = 50
    height = 10
    center = np.array([0,0])
    velocity = np.array([0,0])
    bat_color = (0,0,100)

    def __init__(self,x=None,y=None):
        if x == None and y == None:
            pass
        else:
            self.center = np.array([x,y])

    def draw(self, gameDisplay):
        temp = self.get_rect()
        
        pygame.draw.rect(gameDisplay,self.bat_color,(temp))

    def get_rect(self):
        x,y = self.center
        return (int(x - self.width), int(y - self.height), self.width, self.height)