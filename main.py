from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

items = ["planks_oak", "stone", "dirt", "cobblestone"]
selected = 0

def update():
    if held_keys['1']:
        selected = 0
    elif held_keys['2']:
        seleceted = 1
    elif held_keys['3']:
        selected = 2
    elif held_keys['4']:
        seleceted = 3

class Block(Button):
    def __init__(self, block_name, position=(0,0, 0)):

        match block_name:
            case "planks_oak":
                block_texture = "assets/planks_oak.png"
            case "dirt":
                block_texture = "assets/dirt.png"
            case "stone":
                block_texture = "assets/stone.png"
            case "cobblestone":
                block_texture = "assets/cobblestone.png"

        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = block_texture,
            color = color.rgb(255,255,255),
            highlight_color = color.white,
        )
        
    def input(self, key):
        global selected
        if held_keys['1']:
            selected = 0
        elif held_keys['2']:
            selected = 1
        elif held_keys['3']:
            selected = 2
        elif held_keys['4']:
            selected = 3
            
        if self.hovered:
            if key ==  "left mouse down":
                destroy(self)
            if key == "right mouse down":
                if selected >= 0 and selected <= len(items):
                    block = Block(position=self.position + mouse.normal, block_name=items[selected])

chunkSize = 16

for z in range(chunkSize):
    for x in range (chunkSize):
        voxel = Block(position=(x, 0, z), block_name="dirt")



player = FirstPersonController()



app.run()