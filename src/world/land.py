from ursina import *
from world.materials import sandbrick

class land:
    def __init__(self):
        
        for x in range(20):
            for z in range(20):
                sandbrick.block((x, 0, z))
            
