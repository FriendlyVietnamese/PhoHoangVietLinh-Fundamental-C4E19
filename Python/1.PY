#First, make a loop and some places to input 2 numbers
while True:	
	x= int(input("\nX?:"))
	y= int(input("Y?:"))
	def GCD(x,y):
#if y = 0, the result is X, since 0 can devide all numbers		
	    if y == 0:
	        return x			
	    elif y != 0:
	    	return GCD(y, x % y)
	print GCD(x,y)


