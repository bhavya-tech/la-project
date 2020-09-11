import pygame

class Bat:
    width = 50
    height = 10
    x=0
    y=0
    bat_color = (0,0,100)

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay,self.bat_color,(self.x,self.y,self.width,self.height))