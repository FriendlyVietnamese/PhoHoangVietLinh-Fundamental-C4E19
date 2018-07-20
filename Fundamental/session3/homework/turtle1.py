from turtle import *
shape("turtle")
speed(-1)
pensize(2)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
cạnh = 3
i = 0

for a in range(10):
    for b in range(cạnh):
        color(colors[i])
        fd(70)
        lt(360/cạnh)
    i +=1
    if i == 5:
        i = 0
    cạnh = cạnh + 1

mainloop()

