#First, make some rooms to input 2 numbers
x = int(input('X:')) 
y = int(input("Y:"))
i = max(x,y)
if (x == 0 or y == 0):
	print('The greatest common divisor is', i)
else:
 while True:
	  if (i%x == 0 and i%y == 0):
	    break
	  i += 1
 GCD = x*y/i
 print('The greatest common divisor is', GCD)