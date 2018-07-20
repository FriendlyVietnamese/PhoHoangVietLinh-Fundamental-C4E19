n = int(input("Tính giai thừa n\nWhat number do you want?: "))
result = 1
for i in range(n):
    result*=i+1
print("\nKết quả:",result)
End= input("\nPress Enter to quit")