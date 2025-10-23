nama_pembeli = input("Masukan Nama Pembeli       : ") #tidak usah memakai float atau int karena ini teks
nama_barang = input("Masukan Nama Barang        : ") #tidak usah memakai float atau int karena ini teks
harga_barang = float(input("Masukan Harga Barang       : ")) #harus memakai float atau int karena ini angka
uang_bayar = float(input("Masukan Uang Bayar         : ")) #harus memakai float atau int karena ini angka

total_harga = harga_barang #total harga adalah harga barang
kembalian = uang_bayar - total_harga #kembalian adalah uang bayar dikurangi total harga

def format_rupiah(amount):
    return "Rp. {:,}".format(amount).replace(",", ".") #fungsi untuk format rupiah

print("===============HASIL===============")
print("Nama Pembeli : ",nama_pembeli)
print("Nama Barang  : ",nama_barang)    
print("Harga Barang : ",format_rupiah(harga_barang))
print("Uang Bayar   : ",format_rupiah(uang_bayar))
print("Total Harga  : ",format_rupiah(total_harga))
print("Kembalian    : ",format_rupiah(kembalian))