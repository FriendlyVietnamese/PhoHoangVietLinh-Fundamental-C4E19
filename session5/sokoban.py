map = {
    "size_x":5,
    "size_y":5
}
player={
    "x":4,
    "y":4
}
boxes = [
    {"x":1, "y":1},
    {"x":2, "y":2},
    {"x":3, "y":3},
]
destination = [
    {"x":1,"y":2},
    {"x":2,"y":3},
    {"x":3,"y":4},
]
while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            box_is_here = False
            des_is_here = False
            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True  
            for toado in boxes:
                if x == toado["x"] and y == toado["y"]:
                    box_is_here = True
            for des in destination:
                if x == des["x"] and y == des["y"]:
                    des_is_here = True  
                
            
            if player_is_here == True:
                print("P ", end ="\t")
            elif box_is_here == True:
                print("B ", end = "\t")        
            elif des_is_here == True:
                print("D ", end = "\t")    
            
            else:
                print("- ", end ="\t")
        print()
    move = input("\nYour move?: ")
    dx = 0
    dy = 0

    if move == "w".lower():
        dy  = -1
    elif move == "S".lower():
        dy = 1
    elif move == "A".lower():
        dx = -1
    elif move == "D".lower():
        dx= 1
    else:
        print("Wtf?")
    if 0 <= player["x"] + dx < map['size_x'] and 0<= player["y"] + dy < map['size_y']:    
        player["x"] += dx
        player["y"] += dy   
    for item in boxes:
            if player["x"] == item["x"] and player["y"] == item["y"]:
                item["x"] +=dx
                item["y"] +=dy
                
    
    

