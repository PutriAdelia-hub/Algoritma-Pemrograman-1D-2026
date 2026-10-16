pin = int(input("Masukkan PIN: "))
jam = int(input("Masukkan jam kedatangan: "))
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:  
    if jam < 12:
        pesan_akses = "Garasi Pagi Terbuka"
    else:
        pesan_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:  
    if (digit1 + digit3) == digit2:
        pesan_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:  
    pesan_akses = "Akses Ditolak Sepenuhnya!"
status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print(f"Pemisahan PIN  : Digit 1 = {digit1}, Digit 2 = {digit2}, Digit 3 = {digit3}")
print(f"Jam Kedatangan : {jam}:00")
print(f"Status Garasi  : {pesan_akses}")
print(f"Status CCTV    : {status_cctv}")