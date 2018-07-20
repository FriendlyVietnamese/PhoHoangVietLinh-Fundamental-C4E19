import random
print("Đoán tên người")
words = ["champion",'Vietlinh','Nhung',"LinhChi","Hoang"]

for i in range(len(words)):
    r = random.randint(0,len(words))
    a = list(words[r])
    print()
    
    for char in range(len(a)):
        random_letter = random.choice(a)
        print(random.choice(random_letter), end = " ")
        a.remove(random_letter)
    while True:
        inp = input("\nYour answer?: ")
        if inp == words[r]:

            print("Correct! Nice")
            break
        
        else:
            print("Sai rùi!")
    


    