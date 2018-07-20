from turtle import *
shape("turtle")
speed(-1)
pensize(2)
bgcolor("yellow")
color("red")
for i in range(11):
    for e in range(2):
        fd(100)
        lt(90)
    for ed in range(3):
        fd(200)
        lt(90)
    fd(100)
    lt(90)
    fd(200)
    lt(180)
    fd(100)
    lt(360/11)


mainloop()