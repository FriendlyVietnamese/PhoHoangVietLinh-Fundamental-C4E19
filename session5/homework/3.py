bacteria = float(input("\nHow many bacterias are there?: "))
time = float(input("\nHow much time in minute?? :"))


total = bacteria * 2**(time/2)
print("\nSo after {0} min we will have {1} con vi khuẩn\n".format(int(time),int(total)))