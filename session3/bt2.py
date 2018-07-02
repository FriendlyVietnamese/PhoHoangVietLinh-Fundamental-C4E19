# list/ array
# print(*list) để list tất cả mà không có dấu ngoặc vuông, phảy, ngoặc kép
# sep = "" / phân tách các phần tử trong list
# CRUD - Create - Read- Update- Delete

menu = ["Kem", 'Xôi', 'Phở', 'thịt']
# print(*menu, sep = "\e")
# print(len(menu))
# menu.append("Chè")
# print(*menu, sep = "\e")
# print(len(menu))


# for i in range(len(menu)):
    # print(menu[i])
for item in menu:
    print(item)
menu[1] = "Gái"
print(*menu, sep =", ")