from river import river
import mlab2
mlab2.connect()

Africa_rivers = river.objects( continent = "Africa")
for item in Africa_rivers:
    print(item["name"])

Short_rivers = river.objects(continent = "S. America", length__lt = 1000)
for item in Short_rivers:
    print(item["name"])

