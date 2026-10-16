hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1                 

    barang_saat_ini = 1
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat ** 5000           

        if kategori == 2:    # menambahkan dua sama dengan agar program mengetahui bahwa kategori tsb jika bernilai dua maka akan dieksekusi           
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (YA/TIDAK): ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
        else:
            jarak = input("Masukkan jarak (km): ")  
            if jarak > 100:
                biaya = 15000
            if jarak > 20:              
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan
    break #untuk menghentikan statemen
    ulangi = int(input("Layani pelanggan lain? (YA/TIDAK): "))  
    if ulangi == "n":
        pass

print("Total Pendapatan Hari Ini: Rp", total_pendapatan) #harusnya untuk menampilkan total pendapatan yakni dengan memanggil variable total_pendapatan bukan total_revenue 