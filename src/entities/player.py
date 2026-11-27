from ursina import *
import threading

class Player(Entity):

    velocity: tuple[int, int, int]

    def __init__(self, pos):
        super().__init__(model = 'cube', color = color.rgb(1, 100, 1), texture = 'brick', position = pos, scale_y = 2)

        #camera.position = pos

        self.position = camera.position + camera.forward / 2

        #camera.position = (camera.position.x, camera.position.y + 1, camera.position.z)


        #self.thread = threading.Thread(target=self.input_to_velocity)

        #self.toggle_input(True)


    """def toggle_input(self, enable: bool):
        if enable:
            self.thread.start()
        else:
            self.thread = threading.Thread(target=self.input_to_velocity)"""

    def apply_velocity(self):

        if self.velocity != (0, 0, 0):

            self.position = (self.position[0] + self.velocity[0] * time.dt, 0, self.position[2] + self.velocity[2] * time.dt)

            print(self.position)
            camera.position = (camera.position[0] + self.velocity[0] * time.dt, 0, camera.position[2] + self.velocity[2] * time.dt) 

    def loop(self):
        self.input_to_velocity()
        self.apply_velocity()


    def input_to_velocity(self):
        # each direction has 6 units in it's axis
        xValue = 0
        zValue = 0

        
        if held_keys['w']:
            zValue += 6

        if held_keys['a']:
            xValue -= 6

        if held_keys['s']:
            zValue -= 6

        if held_keys['d']:
            xValue += 6

        self.velocity = (xValue, 0, zValue)

        


                
        