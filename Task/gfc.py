# Program GEROBAK FRIED CHICKEN

def format_rupiah(amount):
    return "Rp.{:,}".format(amount).replace(",", ".")

menu = {
    "D": ("Dada", 2500),
    "P": ("Paha", 2000),
    "S": ("Sayap", 1500)
}

print("GEROBAK FRIED CHICKEN")
print("=" * 40)
print(f"{'Kode':<6} {'Jenis Potong':<15} {'Harga':>10}")
print("-" * 40)
for kode, (nama, harga) in menu.items():
    print(f"{kode:<6} {nama:<15} {format_rupiah(harga):>11}")
print("=" * 40)

total = 0
pesanan = []

jumlah_jenis = int(input("Berapa jenis potong yang dibeli? "))

for i in range(jumlah_jenis):
    kode = input(f"Jenis ke-{i+1} (D/P/S): ").upper()
    if kode in menu:
        banyak = int(input("Jumlah potong: "))
        nama, harga = menu[kode]
        jumlah = harga * banyak
        pesanan.append((nama, harga, banyak, jumlah))
        total += jumlah
    else:
        print("Kode tidak valid, diabaikan.")

# Tampilkan struk
print("\nStruk Pembelian")
print("=" * 50)
print(f"{'Jenis':<10} {'Harga':>10} {'Banyak':>10} {'Jumlah':>15}")
print("-" * 50)
for nama, harga, banyak, jumlah in pesanan:
    print(f"{nama:<10} {format_rupiah(harga):>11} {banyak:>6} {format_rupiah(jumlah):>19}")
print("-" * 50)
pajak = int(total * 0.10)
print(f"{'Total':<32} : {format_rupiah(total)}")
print(f"{'Pajak 10%':<32} : {format_rupiah(pajak)}")
print(f"{'Bayar':<32} : {format_rupiah(total + pajak)}")