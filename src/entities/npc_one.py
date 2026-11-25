from ursina import *

class npc_one(Entity):
    def __init__(self):
        super().__init__(model = 'cube', color = color.rgb(1, 100, 1), texture = 'brick', position = (0, 0, 0))
        