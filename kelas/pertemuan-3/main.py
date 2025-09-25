# nilai = 70
# if nilai > 75:
#     print("nilai A")
# elif nilai > 65:
#     print("nilai B")
# else:
#     print("nilai C")

# suhu = 35

# if suhu >= 35:
#     print("PANAS")
# if suhu > 30:
#     print("Sauna")
# elif suhu > 20:
#     print("normal")
# else:
#     print("dingin")

umur = int(input("Masukkan umur Anda: "))
if umur < 13:
    kategori = "Anak-Anak"
elif umur < 18:
    kategori = "Remaja"
elif umur < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print(f"Umur : {umur} Kategori : {kategori}")

nilai = 70
status = "Lulus" if nilai >= 60 else "Tidak Lulus"
print(status)

tinggiBadan = 150
pesan = "Boleh" if tinggiBadan >= 145 else "tidak boleh"
print(pesan)

totalBelanja = 1000000
if totalBelanja > 100000:
    diskon = "20%"
elif totalBelanja > 50000:
    diskon = "10%"
else:
    diskon = "Tidak Dapat"

print(f"Total Belanja : {totalBelanja} diskon : {diskon}")
