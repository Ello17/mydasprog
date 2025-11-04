

no_absen = []
namaLengkap = []
nilaiTugas1 = []
nilaiTugas2 = []
nilaiTugas3 = []
nilaiAkhir = []

ulang = int(input("Masukkan jumlah data siswa yang akan diinput: "))

for i in range(ulang) :
    print("="*38,"Masukan Data Siswa",i+1, "="*38)
    no_absen.append(input("Masukkan No Absen: "))
    namaLengkap.append(input("Masukkan Nama Lengkap: "))
    nilaiTugas1.append(int(input("Masukkan Nilai Tugas 1: ")))
    nilaiTugas2.append(int(input("Masukkan Nilai Tugas 2: ")))
    nilaiTugas3.append(int(input("Masukkan Nilai Tugas 3: ")))

for i in range(ulang) :
    nilaiAkhir.append((nilaiTugas1[i]+nilaiTugas2[i]+nilaiTugas3[i])/3)
# total_nilai = (nilaiTugas1[0] + nilaiTugas2[0] + nilaiTugas3[0]) / 3

#output
print("="*42," Data Siswa ","="*42)
print("No Absen"," "*10,"Nama Lengkap"," "*10,"Nilai Tugas 1"," "*5,"Nilai Tugas 2"," "*5,"Nilai Tugas 3"," "*5)
print("-"*98)
for i in range(ulang) :
    print(f"{no_absen[i]:>5} {namaLengkap[i]:>22} {nilaiTugas1[i]:>22} {nilaiTugas2[i]:>20} {nilaiTugas3[i]:>19}")
print("-"*98)
print("Total Nilai Rata-Rata Siswa :",int(nilaiAkhir[i]))


