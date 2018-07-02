from turtle import *
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    begin_fill()
    for j in range(4):
        
        color(colors[i])
        fd(50)
        lt(90)
    end_fill()
    fd(50)
    
mainloop()