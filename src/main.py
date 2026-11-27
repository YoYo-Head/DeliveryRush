from ursina import *
from entities import player
from world import land

app = Ursina()




# debug menu
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = True
window.entity_counter.enabled = False
window.collider_counter.enabled = False

land.land()
p = player.Player((5, 1, 5))

def update():
    
    p.loop()



#EditorCamera()


app.run()