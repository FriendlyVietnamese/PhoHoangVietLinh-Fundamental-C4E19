#first, let's make some rooms to input those 2 numbers
while True:
	x= int(input("\nX:"))
	y= int(input("Y:"))
	i = 1
	Max= max(x,y)
#A particular circumstace in which either X or Y = 0	
	if (x == 0 or y == 0):
		print("The greatest common divisor is:", Max)
#Create a loop to calculate	the Least common multiplier
#LCM is calculated by increasing the number i by 1
#until the number i is divisible to 2 inputed numbers
	else:
		while True:

			if (i%x==0 and i%y==0):
				break
			i += 1
			GCD = x * y / i
		print('The greatest common divisor is:', GCD)	
