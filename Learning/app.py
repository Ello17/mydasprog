no_absen = []
namaLengkap = []
nilaiTugas1 = []
nilaiTugas2 = []
nilaiTugas3 = []
nilaiAkhir = []

ulang = int(input("Masukkan jumlah data siswa yang akan diinput: "))

for i in range(ulang) :
    print("="*10," Masukan Data Siswa",i+1, "="*10)
    no_absen.append(input("Masukkan No Absen: "))
    namaLengkap.append(input("Masukkan Nama Lengkap: "))
    nilaiTugas1.append(int(input("Masukkan Nilai Tugas 1: ")))
    nilaiTugas2.append(int(input("Masukkan Nilai Tugas 2: ")))
    nilaiTugas3.append(int(input("Masukkan Nilai Tugas 3: ")))

total_nilai = (nilaiTugas1[0] + nilaiTugas2[0] + nilaiTugas3[0]) / 3

print("="*10," Data Siswa ","="*10)
print("No Absen      :", no_absen[0])
print("Nama Lengkap  :", namaLengkap[0])
print("Nilai Tugas 1 :", nilaiTugas1[0])
print("Nilai Tugas 2 :", nilaiTugas2[0])
print("Nilai Tugas 3 :", nilaiTugas3[0])
print("Total Nilai   :", int(total_nilai))

# for i in range(ulang) :
#     nilaiAkhir.append((nilaiTugas1[i]+nilaiTugas2[i]+nilaiTugas3[i])/3)