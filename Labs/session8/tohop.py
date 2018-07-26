from math import sqrt
a = float(input(""))
b = float(input(""))
c = float(input(""))
def nghiem_bac_2(a,b,c):
    delta = sqrt(b**2-4*a*c)
    x1 = (-b+delta)/2*a
    x2 = (-b-delta)/2*a
    return x1,x2
print(nghiem_bac_2(a,b,c))

        
        