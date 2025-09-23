from prettytable import PrettyTable

nama = input("Masukkan nama pasien: ")
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))

berat_ideal = tinggi - 100
status_list = ["Berat Badan Ideal", "Kelebihan Berat Badan"]
isKelebihan = berat > berat_ideal
status = status_list[int(isKelebihan)]

tabel = PrettyTable()
tabel.field_names = ["Keterangan", "Hasil"]
tabel.align["Keterangan"] = "l"
tabel.align["Hasil"] = "l"

tabel.add_row(["Nama Pasien       :", nama])
tabel.add_row(["Tinggi Badan      :", f"{tinggi:.0f} cm"])
tabel.add_row(["Berat Badan       :", f"{berat:.0f} kg"])
tabel.add_row(["Berat Ideal       :", f"{berat_ideal:.0f} kg"])
tabel.add_row(["Status            :", status])

print("-" * 81)
print(f"|{'HASIL CEK BERAT BADAN':^79}|")
print("-" * 81)
print(tabel)
print("-" * 81)