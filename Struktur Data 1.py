# Input nama
nama = input("Masukkan nama anda : ")

# Validasi nama 
if nama == "naya":
    print("Selamat datang naya")
else:
    print("Program selesai")

# Input umur
umur = int(input("Masukkan umur anda: "))
if umur <= 0:
    print("Anda belum lahir")
elif umur < 18:
    print("Anda belum cukup umur")
elif umur <= 18:
    print("Anda cukup umur")
elif umur > 60:
    print("Banyakin ibadah, bentar lagi mati")
else:
    print("Program selesai")