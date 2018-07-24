from turtle import *
import random
shape("triangle")
# speed(-1)
pensize(2)
color('blue')
def draw_star(x,y,length):
    for egdes in range(5):
        fd(length)
        rt(144)
        speed(0)
    penup()
    goto(x,y)
    pendown()
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 50)
    draw_star(x, y, length)
        
        
        





mainloop()