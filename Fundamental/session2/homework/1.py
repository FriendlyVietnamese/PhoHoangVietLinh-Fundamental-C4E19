h = int(input("Bạn cao bao nhiêu cm?^^: "))
w = int(input("Bạn nặng bao nhiêu Kg?^^: "))
H = float(h*0.01)
BMI = w/(H*H)
print("Chỉ số BMI:",int(BMI))
if BMI < 16:
    print("Mày thuộc loại super gầy rồi, ăn nhiều lên=))")
elif 16 <= BMI < 18.5:
    print("Hơi gầy đấy ahihi ^^") 
elif 18.5<= BMI <25:
    print("Chỉ số đẹp đấy hotboy ♥")
elif 25 <= BMI < 30:
    print("Mày sắp tiền hóa thành nhợn rồi =))")
else:
    print("Vãi đạn! Mày là nhợn thành tinh à?=))")
End = input("\nPress Enter to quit")