size = [5,7,300,90,24,50,75]
i = 0
a = 1
print("Hi, I'm Linh the farmer. Here is the size of my sheeps:\n",size,"\n")
want = int(input("Bạn muốn nuôi cừu trong bao nhiêu tháng?: "))

for month in range(want):
    biggest = max(size)
     
    print("\tCon cừu to nhất tháng này là",biggest,"\n\tCạo lông nó nào!!\n\t\b"+"--  "*10)
    
    size.remove(max(size))
    size.append(8)
    print("\tAfter shearing, here is my flock:\n\t",size)
    for number in size:
        number +=50
        size[i] = number
        i+=1
    i = 0 
    print("Month", a, ":\n\t1 tháng trôi qua.. Đàn cừu hiện tại:\n\t",size)
    a+=1 

print("--^-- "*10,"\nThôi chán rồi, bán cừu đi du lịch thôi!! Giờ tớ đang có $ =",sum(size)*2)
