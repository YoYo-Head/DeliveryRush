from ursina import *
import threading

class Player(Entity):

    velocity: Vec3

    def __init__(self, pos):
        super().__init__(model = 'cube', color = color.rgb(1, 100, 1), texture = 'brick', position = pos, scale_y = 2)

        camera.position = pos

        self.position = camera.position + camera.forward / 2

        camera.position = (camera.position.x, camera.position.y + 1, camera.position.z)


        self.thread = threading.Thread(target=self.input_to_velocity)

        self.toggle_input(True)


    def toggle_input(self, enable: bool):
        if enable:
            self.thread.start()
        else:
            self.thread = threading.Thread(target=self.input_to_velocity)

    def apply_velocity(self):
        self.position * self.velocity

    def loop(self):
        self.apply_velocity()


    def input_to_velocity(self):
        # each direction has 6 units in it's axis
        xValue = 0
        zValue = 0

        while True:
            if held_keys['w']:
                xValue += 6

            if held_keys['a']:
                zValue += 6

            if held_keys['s']:
                xValue -= 6

            if held_keys['d']:
                zValue -= 6

            self.velocity = Vec3(xValue, 0, zValue)

        


                
        