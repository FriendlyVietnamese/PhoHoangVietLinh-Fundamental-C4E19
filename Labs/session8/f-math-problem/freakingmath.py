from random import *
def linh_tinh():
    x = randint(3,9)
    y = randint(2,9)
    errors = choice([-1,0,0,1,-2,+2,0])
    
def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    linh_tinh()
    display_result = x*y + errors
    return [x, y, "x", display_result]
    print(generate_quiz(x))
# mỗi khi click thì function chạy
def check_answer(x, y, op, result, user_choice):
    #User_choice: True/False
    linh_tinh()
    if error == 0:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if choices ==False:
            return True
        else:
            return False