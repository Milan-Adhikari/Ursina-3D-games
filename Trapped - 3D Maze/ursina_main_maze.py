from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

cheat = 0

def update():
    if held_keys['q']:
        application.quit()
    if held_keys['Q']:
        application.quit()

def main_function():
    application = Ursina()
    # model
    maze = Entity(model = 'maze1',texture = 'whales.png',scale = 6,collider = 'mesh')   #position = Vec3(0, 0.04, 0)
    maze.position = Vec3(-80,0,80)
    ground = Entity(model ='finalground',scale = 0.07,texture = 'grass_try.png',collider = 'mesh')   #Vec3(40.1828,0.04,-36.1306)
    ground.position = Vec3(0,0,0)
    house = Entity(model ='final_hut',texture = 'ground_try_big.png',scale =0.3,double_sided = True, collider = 'mesh',parent = scene)
    house.position =Vec3(-22.2702, 0.14, 30.0108)
    house.rotation = Vec3(0,90,0)
    around_house_tree = Entity(model ='around_house_tree',texture = 'wall.png' ,double_sided = True,scale = 0.3)
    around_house_tree.position =Vec3(-22.9737, 0.14, 22.7982)
    around_house_tree.rotation = Vec3(0,90,0)
    sky = Entity(model = 'own_sphere',scale = 1.5,texture ='staryy.png',double_sided = True,collider = 'mesh')
    sky.position =Vec3(0,0,0)
    sky.rotation = Vec3(180,0,180)
    player = FirstPersonController(speed = 10,jump_height = 2)
    player.position = Vec3(-23.6749, 0.14, 19.599)
    cube = Entity(model = 'cube',texture = 'colorful_stars.png',scale = 3)
    cube.position= Vec3(-19.1653, 1.14, 79.7171)
    txt =  Text(text='Go back. You are trapped here forever!',color = color.black,scale = 90,x = -39.1653,y = 6,z = 89.7171,parent = scene )
    application.run()

# main_function()