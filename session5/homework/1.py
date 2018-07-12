inventory = {
    'Gold' : 500,
    'Pouch' : ['flint', 'twine', 'gemstone'],
    'Backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print("OK. Lets see what we have here!!\n"+"--    "*8)
a = 1
for i,j in inventory.items():
    print(a,". {0}: {1}".format(i,j))
    a +=1
inventory["Poket"] = ['seashell', 'strange berry','lint']


print(input("Lets add a pocket into our inventory, OK?"))

a = 1
for i,j in inventory.items():
    print(a,". {0}: {1}".format(i,j))
    a +=1


inventory["Backpack"].remove("dagger")
x = int(input("\nHow much gold do you want to add?: "))
inventory["Gold"] += x
print("  --"*10,"\nAnd now we have {0} gold".format(inventory["Gold"]))


