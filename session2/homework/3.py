# Mỗi đoạn code là một ý của bài 3
print("\n1. Print 20 số từ 0 tới 19")
print(*range(0,20,1))
con= input("\nPress Enter to continue")



######################################
a = int(input("\n2. Print số từ 0 tới n-1\nWhat number do you what?: "))
print(*range(0,a))
con= input("\nPress Enter to continue^^")


########################################
print("\n3. In một chuỗi 0 và 1 consecutively")
print("0 1 "*8)
con= input("\nPress Enter to continue^^")


########################################
b = int(input("\n4. Ask users to enter a number n, then print n 1’s and 0’s in total consecutively.\nMuốn có bao nhiêu số?: "))
for i in range(b):
    if i%2 == 0:
        print("1 ", end="")
    else:
        print("0 ",end ="")
con= input("\nPress Enter to continue^^")



########################################
print("\n\n5. In bảng cửu chương 9*9")
startnum =1
stopnum = 10
for i in range(9):
    print(*range(startnum,stopnum,i+1))
    startnum+=1
    stopnum= 10*(i+2)
con= input("\nPress Enter to continue^^")


########################################
print("\n6. In bảng cửu chương kích thước tùy người nhập")
Stop = int(input("What number do you want bro?: "))
const = Stop
startnum = 1
End = const + 1
for j in range(Stop):
    print(*range(startnum,End,j+1))
    startnum+=1
    End = const*(2+j)+1


########################################
print("\n7.In bảng 1 và 0 kích thước 10x10 ")
con= input("\nPress Enter to continue^^")
for i in range(10):
    print("1  0  "*5)
con= input("\nPress Enter to continue^^")


########################################
#m là cạnh của hình vuông cạnh m*m
m = int(input("\n8. Ask user, rồi in hình vuông 0 và 1\nGive me a number dude: "))
for j in range(m):
    for i in range(m):
        if i%2 == 0:
            print("1  ", end='')
        else:
            print("0  ", end='')
    print("\t") 
End = input("Press Enter to quit the program")



    
    

    

