#input
print("""
==========================
   Input Data Diri Anda            
==========================""")
nama = input("Siapa Nama Anda ? ")
kelas = input("Kelas : ")
nim = input("NIM : ")
nilaimtk = float(input("Masukkan Nilai MTK Anda : "))
nilaipancasila = float(input("Masukkan Nilai Pancasila Anda : "))
nilaiindo = float(input("Masukkan B.indo Nilai Anda : "))
nilairatarata = (nilaimtk + nilaipancasila + nilaiindo) / 3
lulus = nilairatarata >= 75


print("""
==========================
      Data Diri Anda            
==========================""")
print("Nama Anda :", nama)
print("Kelas Anda :", kelas)
print("NIM Anda :", nim)
print("Nilai Rata Rata Anda :", nilairatarata)

if lulus :
    print("Selamat Anda Lulus")
else :
    print("Silahkan coba lagi minggu depan")


# print("namaku adalah", nama)
# print("kelasku adlah", kelas)
# print("nimku adalah", nim)