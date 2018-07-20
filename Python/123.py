#First, make a loop and some places to input 2 numbers
while True:	
	x= int(input("\nX?:"))
	y= int(input("Y?:"))
	def GCD(x,y):
#if y = 0, the result is X, since 0 can devide all numbers		
	    if y == 0:
	        return x
#if y is not equal to 0, recursive function will take the result of x % y, replace x
#then continue to divide it to y until y is equal to 0, then print the result of x	        
	    elif y != 0:
	        return GCD(y,x % y)
	print('The greatest common divisor is', GCD(x,y))
	       
