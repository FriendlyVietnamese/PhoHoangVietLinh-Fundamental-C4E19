from turtle import *
shape("turtle")
speed(-1)
# pensize(2)
color("blue")
size = 1
for j in range(50):

        for i in range(4):
                fd(size)
                lt(90)
        size+=6
        rt(8)



mainloop()