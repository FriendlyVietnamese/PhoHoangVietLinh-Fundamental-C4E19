from random import randint, choice
import eval

while True:
    operators = choice(["+","-","*","/"])
    # print(type(operators))
    a = randint(1,10)
    b = randint(1,10)
    ans = eval.function(a,operators,b)
    error = choice([-1,0,0,1])
    display = ans + error
    choices = input("{0} {3} {1} là: {2}?(Y/N):\n".format(a,b,display,operators))

    if error == 0:
        if choices == "y":
            print("nice!♥")
        elif choices == "n":
            print("Nah")
        else:
            print("lệnh wtf gì đây??! ")
    else:
        if choices =="y":
            print("Sai rùi!")
        elif choices =="n":
            print("Ok")