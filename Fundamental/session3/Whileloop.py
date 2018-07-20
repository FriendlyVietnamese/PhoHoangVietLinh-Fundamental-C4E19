from random import randint
# x = randint(0,101)
x = 50
i = 0
while i<7:
    guess = int(input("Guess my number bro(0-100): \n"))
    if x == guess:
        print("Correct, Congrats homie!")       
        break
    if guess - x < 10:
        print("Hơi to 1 tý")
    elif guess > x:
        print("To quá")

    if guess < x:
        print("Nhỏ quá!!")  
    elif guess - x > 10:
        print("Hơi nhỏ, cố lên sắp tới rồi =))")  
    i = i +1
    if i == 6:
        print("Thua cmnr=)))")
        break
