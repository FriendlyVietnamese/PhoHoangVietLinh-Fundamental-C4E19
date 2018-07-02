size = [5,7,300,90,24,50,75]
i = 0
a = 1
print("Hi, I'm Linh the farmer. Here is the size of my sheeps:\n",size)
for month in range(4):
    biggest = max(size)
     
    print("Now my biggest sheep has the size of",biggest,"\nLet's shear it!!")
    size.remove(max(size))
    size.append(8)
    print("After shearing, here is my flock:\n",size)
    for number in size:
        number +=50
        size[i] = number
        i+=1
    i = 0 
       
    print("Month", a, ":\n1 tháng trôi qua..\n",size)
    a+=1 
print("Thôi chán rồi, bán cừu đi du lịch thôi, giờ tớ đang có $ =",sum(size)*2)
