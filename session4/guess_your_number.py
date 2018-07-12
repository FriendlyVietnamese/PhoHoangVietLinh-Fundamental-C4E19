low = 0
high = 100
input("Guess your numb game^^\nNghĩ 1 số từ 0-100 đi!\n"+"Ấn 'L'arger nếu số t đoán lớn hơn số của bạn\nẤn 'S'maller nếu nhỏ hơn\nẤn C nếu đúng\nPress Enter to continue!!\n" +"--^-- "*10+"\n")
i = 1
while True:

    mid = (low + high)//2
    x = input("Is {0} is your number? ".format(mid)).lower()
    if x == "s":
        low = mid
    elif x =="l":
        high = mid
    if x =="c":
        print("T biết mà ahihi =))")
        break
    i +=1
    if i>7:
        print("Chơi trò bố láo à? :)) không cho chơi nữa!")
        break
    
        