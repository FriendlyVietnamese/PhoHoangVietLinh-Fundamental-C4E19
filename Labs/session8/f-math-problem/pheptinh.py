from random import randint,choice
def random_numbers():
    a = randint(2,9)
    b = randint(2,9)
    return a,b
def linh_tinh(x,y):
    random_numbers()
    # correct_result = x*y
    return (a,b,x*y)
print(linh_tinh(a,b))