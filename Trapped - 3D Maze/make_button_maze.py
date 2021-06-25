import turtle
from turtle import *

def make_button(font_size,text,x,y,length,width):
    button = Turtle()
    button.speed(0)
    button.shape('square')
    button.width(10)
    button.penup()
    button.color('#990066')
    button.pencolor('#2ee3da') # color of text
    button.goto(x,y)
    button.shapesize(stretch_wid=width,stretch_len=length)
    button.stamp() # stamp garesi aba turtle hide gareni, stamp gareko kura dekhirakhcha
    button.hideturtle()
    button.goto(x,y-(font_size)/0.6) # this is been done for aligning the text. align garna lai turtle hide garera, position change gareko, wrt fontsize
    button.write(text,align='center',font = ('Segoe Script', font_size, 'bold'))
