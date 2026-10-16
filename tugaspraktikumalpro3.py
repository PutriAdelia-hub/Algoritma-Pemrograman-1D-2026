# ==== Tugas Praktikum Alpro Soal 3 ====

jarak_satu_arah = 100
konsumsi_bbm_per_liter = 40 # 40 km per 1 liter
konsumsi_bahan_bakar = float(input("Masukkan konsumsi bahan bakar (dalam km/liter): "))
harga_bbm_per_liter = float (input("Masukkan harga bahan bakar per liter (dalam Rp): "))
sisa_bbm_ditangki = 1.5

print(" Rumus Perhitungan Bahan Bakar -----")
total_jarak_pp = jarak_satu_arah * 2
konsumsi_bbm = total_jarak_pp / konsumsi_bbm_per_liter
beli_bbm = konsumsi_bbm - sisa_bbm_ditangki
total_harga_bbm = beli_bbm * harga_bbm_per_liter

print("====== Total kebutuhan ======")
print("Total jarak pulang pergi:", total_jarak_pp, "km")
print("Total bahan bakar yang dibutuhkan:", konsumsi_bbm, "liter")
print("Total bahan bakar yang harus dibeli: ", beli_bbm, "liter")
print("Total harga bahan bakar: Rp", total_harga_bbm)