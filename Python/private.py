so_tien_goc = 0
def gui():
    while True:
        global so_tien_goc
        so_tien_gui = int(input("Moi nhap so tien gui: "))
        if so_tien_gui == "x":
            print("cam on da su dung dich vu")
            chaomung()
        so_tien_goc += so_tien_gui

        print("TK hien co: %d" % so_tien_goc)
    return so_tien_goc

def rut():
    while True:
        global so_tien_goc
        so_tien_rut = int(input("Moi nhap so tien rut: "))
        if so_tien_rut == "x":
            print("Cảm ơn quý khác đã sử dụng dịch vụ!")
            break
        elif so_tien_rut > so_tien_goc:
            print("TK het tien. Vui long nap them!")
            gui()
        else:
            so_tien_goc -= so_tien_rut
        print("TK hien co: %d" % so_tien_goc)
    return so_tien_goc

def chaomung():
    while True:
        print("""Ban muon gui tien hay rut tien: 
              Nhan 1 de gui tien
              Nhan 2 de rut tien
              Nhan "x" de thoat ra """)
        a = input(">>")
        if a == "1":
            return gui()
        elif a == "2":
            return rut()
        else:
            print("Sai cu phap. Moi nhap lai")
            continue

chaomung()









