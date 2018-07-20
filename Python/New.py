x = int(input("?:"))
def giaithua1(x):
    if x==1:
        return 1
    else:
        return x*giaithua1(x-1)