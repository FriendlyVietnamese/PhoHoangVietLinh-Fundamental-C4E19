total = 2
months = int(input("Anh muốn nuôi thỏ trong bao nhiêu tháng?: "))
print("Tháng 0: 1 cặp thỏ!")
for i in range(months):
    total += i
    print("Tháng {0}: {1} cặp thỏ!".format(i+1,total))