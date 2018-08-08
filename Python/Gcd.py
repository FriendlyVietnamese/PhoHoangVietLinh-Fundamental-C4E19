print("Hello mother fucker! nhập thu chi, ấn [x] nếu ko muốn nhập nữa")
listt = []
total = 0
while True:
# for i in range(4):
	history = str(input("What do you want?: "))
	if history == "x":
		break
	else:	
		listt.append(history)

for item in listt:
	if item.split(" ")[0] == "w":
		total -= int(item.split(" ")[1])
	elif item.split(" ")[0] == "d":
		total += int(item.split(" ")[1])
	
print("Hiện còn {0} đồng trong tài khoản".format(total))

	




