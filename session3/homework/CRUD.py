

items = ["T-shirt", "Sweater","Jacket"]
a = 0
while True:
    w = str(input("Welcome to our shop! What do you want (C,R,U,D)?\nIf you dont want to be here, type [X]\n"))
    if  w == "R" or w =="r":
        print("Our shop has:")
        for index,item in enumerate(items):
            print(index+1,"\b.",item) 
    elif w == "C" or w =="c":
        new = input("Enter new item: ")
        items.append(new)
        print("Our items: ")
        for index,item in enumerate(items):
            print(index+1,"\b.",item)
    elif w == "U" or w == "u":
        position =int(input("Update position?: ")) - 1
        items[position] = input("New items?: ")
        print("Ok, now our shop has:")
        for index,item in enumerate(items):
            print(index+1,"\b.",item)
    elif w == "D" or w == "d":
        i = int(input("Delete position?: ")) - 1
        del items[i]
        for index,item in enumerate(items):
            print(index+1,"\b.",item)
    elif w == "X" or w == "x":
        break
    else:
        print("I dont know what you mean!")