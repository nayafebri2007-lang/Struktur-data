# validasi nama 
nama = input("Masukkan nama anda: ")

if nama.lower() == "naya":
    print("lanjut ke program berikutnya\n")
else:
    print("Silahkan coba lagi\n")

# Input angka
angka = int(input("Masukkan angka (1-10): "))

# Validasi angka
if angka < 1 or angka > 10:
    print("Angka harus antara 1 sampai 10")
else:
    print(f"\nTabel perkalian {angka}:")
    
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")

print("\nProgram selesai")