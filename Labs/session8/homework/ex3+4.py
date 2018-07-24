from random import choice
from turtle import *
colors = ["red","yellow","blue","green","pink",'black',"orange","purple"]
pensize(2)
shape = ("turtle")
speed(-1)
def draw_square(x,y):
    for edges in range(4):
            color(y)
            
            fd(x)
            lt(90)
            
for i in range(30):
    draw_square(i * 7, choice(colors))
    left(17)
    penup()
    forward(i * 2)
    pendown()




mainloop()