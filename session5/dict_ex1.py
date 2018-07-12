teencode = {
    "eny": "em người iu",
    "any": "anh người iu",
    "hc": "học",
    "ns": "nói",
    "vl":"việt linh"
}
print("Welcome to my dictionary!!^^\n"+"--**--  "*8)
   
print(*teencode.keys(), sep = "\t")
while True: 
    x = input("\nType a word!: ")

    if x in teencode:
        print("{0} ----> {1}".format(x,teencode[x]))  
    else:
        question = input("Không có từ này, có muốn add không(Y/N)?: ")
        if question == "y":
            added = input("\nMeaning?: ")
            teencode[x] = added
            print(*teencode.keys(), sep = "\t")
        elif question =="n":
            break
        else:
            print(input("\n.......\nđ hiểu lệnh này=)) Nhấn Enter để tiếp tục"))

            continue

