from ursina import *

class block(Entity):
    def __init__(self, pos):
        super().__init__(model = 'cube', color = color.rgb(1, 100, 1), texture = 'rainbow', position = pos)
        