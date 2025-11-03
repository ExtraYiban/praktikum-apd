from prettytable import PrettyTable
from data import labGear
from utils.warna import SUCCESS, ERROR, WARNING, TITLE, RESET

def cek_jumlah_alat(nama_alat):
    try:
        if nama_alat in labGear:
            return labGear[nama_alat]["jumlah"]
        else:
            raise ValueError("Alat tidak ditemukan.")
    except ValueError as e:
        print(ERROR + "Error: " + str(e))
        return None

def tambah_alat(nama):
    try:
        jumlah = input("Masukkan jumlah alat: ").strip()
        if not jumlah.isdigit() or int(jumlah) <= 0:
            raise ValueError("Jumlah harus angka positif.")
        labGear[nama] = {"jumlah": int(jumlah), "status": "tersedia", "peminjam": "-"}
        print(SUCCESS + f"Alat '{nama}' berhasil ditambahkan!" + RESET)
    except ValueError as e:
        print(ERROR + "Error: " + str(e))

def tampilkan_stok_alat():
    from os import system
    system("cls || clear")
    print(TITLE + "=== STOK ALAT ===" + RESET)

    if not labGear:
        print(WARNING + "Belum ada alat." + RESET)
        return

    table = PrettyTable()
    table.field_names = ["Nama Alat", "Jumlah", "Status", "Peminjam"]

    for nama, info in labGear.items():
        table.add_row([nama, info["jumlah"], info["status"], info["peminjam"]])

    print(table)

def hitung_total_alat(index=0, total=0):
    keys = list(labGear.keys())
    if index == len(keys):
        return total
    alat = keys[index]
    total += labGear[alat]["jumlah"]
    return hitung_total_alat(index + 1, total)

