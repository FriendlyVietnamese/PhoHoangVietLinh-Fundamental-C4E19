numbers = [1,6,8,1,2,1,5,6]
print("[Press X to quit the program]\nI have this list of numbers:\n",*numbers)

while True:     
    counter = 0
    x = input("\nEnter a number!: ")
    if x == "x" or x == "X":
        break
    else :
        for i in range(len(numbers)):
                if numbers[i] == int(x):
                    counter +=1
                else:
                    pass
    print("{0} appears {1} times.".format(x,counter))
   
