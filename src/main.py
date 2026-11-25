from ursina import *
from entities.npc_one import npc_one
from world import land



app = Ursina()

# debug menu
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = True
window.entity_counter.enabled = False
window.collider_counter.enabled = False

land.land()

EditorCamera()


app.run()