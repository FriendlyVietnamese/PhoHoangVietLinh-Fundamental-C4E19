from random import randint, choice
import eval

print("Welcome! If you dont want to play, press X")

while True:
    #chọn 1 dấu bất kì trong cộng trừ nhân chia, random 2 số a và b để tính toán
    operators = choice(["+","-","*","/"])
    a = randint(1,10)
    b = randint(1,10)
    ## stop ở đây!. nhìn thấy eval.function ko? lật qua bên kia
    ## t đã trả kết quả ra 1 phép tính, gán nó vào biến "ans"
    ans = eval.function(a,operators,b)
    #hiển thị kết quả trên màn hình cho người chơi
    error = choice([-1,0,0,1])
    display = ans + error
    #cho người chơi nhập trả lời+ đống điều kiện
    choices = input("{0} {3} {1} là: {2}?(Y/N):\n".format(a,b,display,operators))
    if choices == "x":
        exit()
    if error == 0:
        if choices == "y":
            print("nice!♥")
        elif choices == "n":
            print("Sai rồi, ngu vãi đái=))")
        else:
            print("lệnh wtf gì đây??! ")
    else:
        if choices =="y":
            print("Sai rùi a hi hi!")
        elif choices =="n":
            print("Ghê ghê! Đúng rùi :))")
        else:
            print("lệnh wtf gì đây??! ")