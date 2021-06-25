from turtle import *
from make_button_maze import make_button
from ursina import *
from ursina_main_maze import main_function
from ursina_main_maze import update
import winsound


EXIT = False
FONT_SIZE = 28
FONT = ('Segoe Script', FONT_SIZE, 'bold')
BGCOLOR = "#0E0F1E"
BUTTONBG = "#1F3049"

# creating the main window
window = Screen()
window.setup(width = 1.0,height= 1.0) # 1.0 means fit to the screensize
window.tracer(0)
# hiding the window bars
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(2)

# go back to main page
def goback(x,y):
    window.tracer(0)
    if (x>-100 and x<200) and (y>160 and y<240):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        window.clear()
        welcome_screen()
# about function
def about_function():
    # winsound.PlaySound(None, winsound.SND_PURGE)
    # texts in about
    window.clear()
    window.tracer(0)
    window.bgpic('background2.png')
    abt = Turtle()
    abt.color('#9bf30e')
    abt.hideturtle()
    abt.penup()
    abt.goto(0,-450)
    abt.write('This is a Maze Game developed by Milan Adhikari. I used Ursina and Turtle \n'
              'module in this game. Some of the models used in this project were downloaded \n'
              '   while the rest of them were created using Blender. All the textures were \n'
              '   downloaded but have been modified according to need using Photoshop. \n',align='center',font = ('Segoe Script', 21, 'bold'))

    make_button(FONT_SIZE,'Okay',50,200,15,4)
    onscreenclick(goback)
# help function
def help_function():
    window.clear()
    window.bgpic('background2.png')
    window.tracer(0)
    abt = Turtle()
    abt.color('#9bf30e')
    abt.hideturtle()
    abt.penup()
    abt.goto(0, -500)
    abt.write('1. Use W key and S key for moving forward and backward.\n'
              '2. Use A key and D key for moving left and right respectively.\n'
              '3. Use your mouse to control the view. \n'
              '3. Press Q key to exit the game. \n ', align='center', font=FONT)
    make_button(FONT_SIZE, 'Okay', 50,200, 15, 4)
    onscreenclick(goback)

def maze_screen(x,y):
    if (y < -390 and y > -470) and (x >-150 and x <150):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        begin_function()

def begin_function():
    winsound.PlaySound('runner',winsound.SND_ASYNC)
    global EXIT
    EXIT = True
    update()
    main_function()

# start function
def start_function():
    window.clear()
    window.tracer(0)
    window.bgpic('maze_background.png')
    text = Turtle()
    text.color('#9bf30e')
    text.hideturtle()
    text.penup()
    text.goto(0, 400)
    text.write('This is the Maze that you will have to Conquer', align='center', font=FONT)
    make_button(FONT_SIZE, 'Begin', 0, -430, 15, 4)
    text.goto(-650,-200)
    text.color('yellow')
    text.write(' Yellow Button \n'
               '= Starting point \n', align='center', font=FONT)
    text.color('red')
    text.goto(650, -200)
    text.write(' Red Button \n'
               '= Ending point \n', align='center', font=FONT)
    onscreenclick(maze_screen)

def quit_function():
    global EXIT
    EXIT = True

# Which button was clicked, we see that
def screenclick(x,y):
    if (x > -250 and x < 250) and (y <-310 and y >-390):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        start_function()
    if (x > -880 and x < -380) and (y <-310 and y >-390):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        about_function()
    if (x < 880 and x > 380) and (y <-310 and y >-390):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        help_function()
    if (x < 870 and x > 570) and (y < 440 and y > 360):
        winsound.PlaySound('button1', winsound.SND_ASYNC)
        quit_function()



# making welcome screen
def welcome_screen():
    window.tracer(0)
    window.bgpic('background_final.png')
    winsound.PlaySound('piano', winsound.SND_ASYNC)
    # start game button
    make_button(FONT_SIZE,'Start Game',0,-350,25,4)
    # about game button
    make_button(FONT_SIZE, 'About Game', -630, -350, 25, 4)
    # help button
    make_button(FONT_SIZE, 'Help', 630, -350, 25, 4)
    # Quit Button
    make_button(FONT_SIZE, 'Quit', 720, 400, 15, 4)
    # detecting click
    onscreenclick(screenclick)

# calling the main screen
welcome_screen()

while EXIT == False:
    window.update()

