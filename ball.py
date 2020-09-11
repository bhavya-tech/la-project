import pygame,coord

class Ball:
    ball_radius = 5
    center = coord.Coord(10,10)
    color = (255,0,0)

    def __init__(self,x=None,y=None):
        if x == None and y == None:
            pass
        else:
            self.center = coord.Coord(x,y)
        

    def draw(self,gameDisplay):
        pygame.draw.circle(gameDisplay,self.color,self.center.get_tuple(),self.ball_radius)