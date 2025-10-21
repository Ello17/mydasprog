kode_baju = input("Masukan Kode Baju (H/K)  : ")
ukuran = input("Masukan Ukuran Baju (L/M/S) : ")

if kode_baju == "H" or kode_baju == "h" :
    merek = "Hijau"
    if ukuran == "L" or ukuran == "l" :
        harga = 100000
    elif ukuran == "M" or ukuran == "m" :
        harga = 80000
    elif ukuran == "S" or ukuran == "s" :
        harga = 60000
    else :
        harga = 0
elif kode_baju == "K" or kode_baju == "k" :
    merek = "Kuning"
    if ukuran == "L" or ukuran == "l" :
        harga = 110000
    elif ukuran == "M" or ukuran == "m" :
        harga = 90000
    elif ukuran == "S" or ukuran == "s" :
        harga = 70000
    else :
        harga = 0
else :
    merek = "Tidak Ada"
    harga = 0
    
print("===================================")
print("Merek Baju Anda Adalah : "+str(merek))
print("Harga Baju Anda Adalah : Rp."+str(harga))
print("===================================")