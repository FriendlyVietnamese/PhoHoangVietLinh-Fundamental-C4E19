menu = ['Kem',"Xôi","Phở"]
# print("Đây là các thứ tớ thích") 

# for i,j in enumerate(menu):
#     print(i+1,".",j)
# posi= int(input("** "*20 +"\nPosition you want to update: "))
# posi = posi -1
# menu[posi] = str(input("Thing you want to replace: "))

for index,item in enumerate(menu):
    print(index+1,".",item) 
# menu.pop(0) ## del với pop là theo index. remove theo item
# del menu[1]
# print(menu)