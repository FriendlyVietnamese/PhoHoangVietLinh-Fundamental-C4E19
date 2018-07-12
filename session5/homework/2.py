numbers = [1,6,8,1,2,1,5,6]
print("[Press X to quit the program\nI have this list of numbers:\n",*numbers)
counter = 0
while True:     
    x = int(input("\nWhat number do you want to find?: "))
    for i in range(len(numbers)):
                if numbers[i] == x:
                    counter +=1

                else:
                    pass
    print("{0} appears {1} times.".format(x,counter))
