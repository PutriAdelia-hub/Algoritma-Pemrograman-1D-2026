total_awal = float(input("Masukkan total belanja awal: "))
if total_awal % 100000 == 0:
    diskon = 1.0
if total_awal % 50000 == 0:
    diskon = 0.50
elif total_awal % 10000 == 0:
    diskon = 0.20
elif total_awal >= 200000:
    diskon = 0.10
else:
    diskon = 0.0
total_bayar = total_awal - (total_awal * diskon)
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("==== Struk Belanja ====")
print(f"Total belanja awal : Rp {total_awal:}")
print(f"Diskon didapat     : {int(diskon * 100)}%")
print(f"Total harus dibayar: Rp {total_bayar:}")
print(f"Status poin : {status_poin}")