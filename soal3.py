suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))
if suhu > 1000:
    if tekanan > 50:
        status_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status_bahaya = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status_bahaya = "Tekanan Tidak Stabil"
    else:
        status_bahaya = "Operasi Reaktor Normal"
else:
    status_bahaya = "Reaktor Belum Cukup Panas"
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print(f"Suhu Terpantu  : {suhu} °C")
print(f"Tekanan Gas    : {tekanan} Bar")
print(f"Status Bahaya  : {status_bahaya}")
print(f"Status Pompa   : {status_pompa}")