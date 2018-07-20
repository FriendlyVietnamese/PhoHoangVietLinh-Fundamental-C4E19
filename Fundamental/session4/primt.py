while True:
    x = int(input("N=?: "))
    if x < 0:
        print("Đừng có nhập số âm!")
    elif x == 2:
        print("prime")
    else:
        for i in range(2,int(x**0.5)):
            if x%i == 0 or x == 0:
                print("not prime!")
                break
        else: print("{0} is a prime!".format(x))

