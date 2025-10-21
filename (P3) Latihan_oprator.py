nama = input("Siapa Nama Anda           : ")
tugas = int(input("Masukkan Nilai Tugas      : "))
uts = int(input("Masukkan Nilai UTS        : "))
uas = int(input("Masukkan Nilai UAS        : "))
nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.5)
lulus = nilai_akhir >= 70

if lulus : 
    print("Selamat Anda lulus Ujian")
else :
    print("Silahkan Coba Lagi Tahun Depan")
    
#opertor logika
syarat_lulus = uas >= 30
nilai_lulus = nilai_akhir >= 70

lulus = syarat_lulus and nilai_lulus

status = "Lulus" if lulus else "Tidak Lulus"
print("Nilai",nama,"adalah",nilai_akhir, ", status :",status)
#bisa menggunakan f contoh
#print(f"Nilai {nama} adalah {nilai_akhir}, status : {status}")