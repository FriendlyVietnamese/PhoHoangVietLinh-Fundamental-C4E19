from turtle import*
shape("turtle")
color("red")
fillcolor("yellow")
bgcolor("black")
speed(-1)
begin_fill()

for i in range(40):
    for j in range(2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    right(10)
end_fill()

mainloop()