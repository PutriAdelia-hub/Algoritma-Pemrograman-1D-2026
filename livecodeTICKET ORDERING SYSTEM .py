Regular = 40.000 
VIP = 75.000 
VVIP = 100.000 
jenis_ticket = input("masukkan jenis ticket:") #digunakan untuk pemgguna menginputkan jenis ticket
jumlah_ticket = int(input("masukkan jumlah ticket yang dibeli:")) #intejer karna pengguna akan memasukan jumlah ticket yang dimana berupa angka bulat 

total = jenis_ticket * jumlah_ticket
if jenis_ticket == "Regular":
    bertanya_minuman = input("apakah ingin tambahan minuman (YA/TIDAK)?")
    print("menambahkan minuman seharga 10.000, Regular")
    if jenis_ticket == VIP:
        print("mendapatkan minuman gratis")
        if jenis_ticket == VVIP:
            print("mendapatkan minuman gratis")
        else:
            print("tidak mendapatkan minuman")

if jumlah_ticket <= 3:
    diskon = 0.15
    if jumlah_ticket >3:
        diskon = 0.10
else:
    print("tidak mendapat diskon")

print(f"Total yang harus dibayar", total)
print("anda mendapatkan diskon", diskon)
#dalam variable regular, vip, dan vvip data tersebut bertipe data int yang dimana merupakan bilangan bulat 
#program diunttukkan pengguna menginputkan jenis ticket yang dipilih dan berapa jumlah ticket yang akan dibeli, yang menggunakan tipe data intejer atau bilangan bulat. 
# setelah itu menggunakan penyeleksian kondisi yang if_else untuk melakukan penyeleksian
#dan agar pengguna tahu bahwa dia mendapatkan diskon maka menggunakan diskon yang dimana dengan menggunakan modulus %