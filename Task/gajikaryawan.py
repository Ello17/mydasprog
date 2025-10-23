def format_rupiah(amount) :
    return "Rp.{:,}".format(amount).replace(",",".")

nama_karyawan = input("Masukan Nama Karyawan         : ")
jabatan = input("Golongan Jabatan (1/2/3)      : ")
pendidikan = input("Pendidikan (SMA/D1/D3/S1)     : ")
jam_kerja = int(input("Masukan Jam Kerja Karyawan    : "))

gaji_pokok = 300000
gol1 = 0.05
gol2 = 0.1
gol3 = 0.15
p_sma = 0.025
p_d1 = 0.05
p_d3 = 0.20
p_s1 = 0.30

if jabatan == "1":
    tunjangan_jabatan = gaji_pokok * gol1
elif jabatan == "2":
    tunjangan_jabatan = gaji_pokok * gol2
elif jabatan == "3":
    tunjangan_jabatan = gaji_pokok * gol3
else:
    tunjangan_jabatan = 0

if pendidikan == "SMA" or "sma" :
    tunjangan_pendidikan = gaji_pokok * p_sma
elif pendidikan == "D1" or "d1" :
    tunjangan_pendidikan = gaji_pokok * p_d1
elif pendidikan == "D3" or "d3" :
    tunjangan_pendidikan = gaji_pokok * p_d3
elif pendidikan == "S1" or "s1" :
    tunjangan_pendidikan = gaji_pokok * p_s1
else :
    tunjangan_pendidikan = 0
    
if jam_kerja > 8 :
    uang_lembur = (jam_kerja - 8) * 3500
else :
    uang_lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + uang_lembur

print("="*12, "Rincian Gaji Karyawan", "="*12)
print("Nama Karyawan         : "+str(nama_karyawan))
print("Gaji Pokok            : "+str(format_rupiah(gaji_pokok)))
print("Tunjangan Jabatan     : "+str(format_rupiah(tunjangan_jabatan)))
print("Tunjangan Pendidikan  : "+str(format_rupiah(tunjangan_pendidikan)))
print("Uang Lembur           : "+str(format_rupiah(uang_lembur)))
print("Total Gaji Karyawan   : "+str(format_rupiah(total_gaji)))
print("="*47)
