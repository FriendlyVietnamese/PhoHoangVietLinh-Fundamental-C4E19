import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
#1. Prepare data muốn vẽ
# Label- portion
labels = ["iOs","Androi","Web","React Native"]
portion = [15,15,45,25]
colors = ['black', 'gold', 'lightskyblue', 'red']
explode = [0,0,0,0.2]

#2. Plot.
pyplot.pie(portion,
            labels=labels,
            colors = colors,
            explode= explode)
pyplot.axis("equal")
# pyplot.set_cmap('hot')
#3. Show ra.
pyplot.show()