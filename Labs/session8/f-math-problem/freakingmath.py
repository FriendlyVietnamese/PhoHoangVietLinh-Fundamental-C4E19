from random import randint,choice

def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    
    a = randint(2,9)
    b = randint(2,9)
    errors = choice([-1,0,0,1,-2,+2,0])
    display_result = a*b + errors
    return [a, b, "x", display_result]
    
    print(generate_quiz())
# run whenever click
def check_answer(x, y, op, result, user_choice):
    #User_choice: True/False
    
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