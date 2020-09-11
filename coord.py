import numpy as np

class Coord:

    def __init__(self,x=None,y=None):
        if x == None and y == None:
            self.coord = np.array([0,0])
        else:
            self.coord = np.array([x,y])
    
    def get_tuple(self):
        return (self.coord[0],self.coord[1])
    
       