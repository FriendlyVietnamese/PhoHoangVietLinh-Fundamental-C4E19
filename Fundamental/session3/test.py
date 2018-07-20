print("2.5 : Let do this for 4 months (or as long as you want):")
sizes = [5, 7, 300, 90, 24, 50, 75]
print()
print(" =====>> Hello, my name is Huyen and there are my sheep sizes")
print(" \t ",sizes)
print()
month = int(input(" Enter the number of months: "))
for i in range(month):
    temp = 0
    for item in sizes:
        item += 50
        sizes[temp] = item
        temp += 1
        sizes_max = max(sizes)
    print("Month {0} :".format(i+1))
    print(" One month  has passed, now here is my flock ")
    print(" \t ", sizes)
    index = sizes.index(sizes_max)
    sizes[index] = 8               
    print(" Now my biggest sheep has size {0} let's shear it. After shearing, here is my flock".format(sizes_max))
    print(" \t ", sizes)
    print()