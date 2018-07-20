#First, make some rooms to input 2 numbers

x = float(input('X:')) 
y = float(input("Y:"))
i = max(x,y)
while True:
	if (i%x == 0 and i%y == 0):
	    break
	i += 1
GCD = x*y/i
print('The great common divisor is',GCD)


	

	

	
