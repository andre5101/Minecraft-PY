from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Block(Button):
    def __init__(self, block_type, block_id ,position=(0,0, 0)):
        
        match block_type:

            case "planks":
                if block_id == 0:
                    block_name = "planks_oak"
            case "dirt":
                if block_id == 0:
                    block_name = "normal dirt"
            case "stone":
                if block_id == 0:
                    block_name = "stone"

                if block_id == 1:
                    block_name = "cobblestone"

        match block_name:
            case "planks_oak":
                block_texture = "assets/planks_oak.png"
            case "normal dirt":
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
        if self.hovered:
            if key ==  "left mouse down":
                destroy(self)
            if key == "right mouse down":
                
                block = Block(position=self.position + mouse.normal, block_type="stone", block_id=0)

chunkSize = 16

for z in range(chunkSize):
    for x in range (chunkSize):
        voxel = Block(position=(x, 0, z), block_type="dirt", block_id=0)

player = FirstPersonController()

app.run()