from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

def update():
    print(player.position)

grass = load_model('groundgrass')
grass_texture = load_texture('grassy.png')
log = load_model('cutlog')
log_texture = load_texture('log_texture.png')
stones = load_model('stones')
stones_texture = load_texture('stones_texture.png')



# model

ground_circle = Entity(model = 'ground_circle',scale =18,collider = 'mesh')
ground_circle.position =Vec3(-23.4068, 0, 21.7427)


# grass_land = Entity(model = grass, texture = grass_texture,scale =10)
# grass_land.position = Vec3(-23.4068, 1.5, 21.7427)


player = FirstPersonController()
player.position =  Vec3(-23.4068, 1.5, 21.7427)

b = 0.1
a = 0.4



for i in range(1,60,1):
    grass_land = Entity(model='groundgrass', texture='grassy.png', scale=10)
    grass_land.position = Vec3(-23.4068, 1.5-b, 1.7427+a)
    a += 0.4
    if grass_land.z > 33:
        b = b+0.07
    else:
        b = 0.01



app.run()