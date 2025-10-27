import os
from data import Users, labGear
from status import *

# ======== Fungsi dan Prosedur ========

# Fungsi tanpa parameter
def tampilkan_header():
    print("=== SISTEM LAB GEAR UNIVERSITAS ===")
    print("Selamat datang di sistem manajemen alat laboratorium\n")

# Fungsi dengan parameter
def cek_jumlah_alat(nama_alat):
    try:
        if nama_alat in labGear:
            return labGear[nama_alat]["jumlah"]
        else:
            raise ValueError("Alat tidak ditemukan.")
    except ValueError as e:
        print("Error:", e)
        return None

# Prosedur tanpa parameter
def tampilkan_daftar_user():
    os.system("cls || clear")
    print("=== DAFTAR USER TERDAFTAR ===")
    for user, info in Users.items():
        print(f"- {user} ({info['role']})")
    input("\nTekan Enter untuk kembali...")

# Prosedur dengan parameter
def tambah_alat(nama):
    try:
        jumlah = input("Masukkan jumlah alat: ").strip()
        if not jumlah.isdigit() or int(jumlah) <= 0:
            raise ValueError("Jumlah harus angka positif.")
        labGear[nama] = {"jumlah": int(jumlah), "status": "tersedia", "peminjam": "-"}
        print(f"Alat '{nama}' berhasil ditambahkan!")
    except ValueError as e:
        print("Error:", e)

# Fungsi rekursif (contoh bonus)
def hitung_total_alat(index=0, total=0):
    keys = list(labGear.keys())
    if index == len(keys):
        return total
    alat = keys[index]
    total += labGear[alat]["jumlah"]
    return hitung_total_alat(index + 1, total)

# ======== Program Utama ========
while programBerjalan:
    os.system("cls || clear")
    tampilkan_header()

    if not sedangLogin:
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        try:
            pilih = input("Pilihan : ").strip()
            if pilih == "1":
                os.system("cls || clear")
                print("=== LOGIN ===")
                usernameInput = input("Username : ").strip()
                passwordInput = input("Password : ").strip()

                if usernameInput in Users and Users[usernameInput]["password"] == passwordInput:
                    sedangLogin = True
                    username = usernameInput
                    role = Users[usernameInput]["role"]
                    print("Login Berhasil!")
                else:
                    print("Login gagal! Username atau password salah.")
                input("Tekan Enter...")

            elif pilih == "2":
                os.system("cls || clear")
                print("=== REGISTER ===")
                newUser = input("Username Baru : ").strip()

                if newUser == "":
                    print("Username tidak boleh kosong!")
                elif newUser in Users:
                    print("Username sudah digunakan!")
                else:
                    newPass = input("Password : ").strip()
                    if newPass == "":
                        print("Password tidak boleh kosong!")
                    else:
                        Users[newUser] = {"password": newPass, "role": "user"}
                        print("Registrasi Berhasil!")
                input("Tekan Enter...")

            elif pilih == "3":
                programBerjalan = False
                print("Keluar dari program...")

            else:
                raise ValueError("Pilihan tidak valid!")

        except ValueError as e:
            print("Error:", e)
            input("Tekan Enter...")

    else:
        os.system("cls || clear")
        print(f"=== Login sebagai {username} ({role}) ===")
        print("1. Lihat Stok Alat")
        if role == "Admin":
            print("2. Tambah Alat")
            print("3. Update Status Alat")
            print("4. Hapus Alat")
            print("5. Lihat Daftar User")
        print("6. Hitung Total Jumlah Alat (rekursif)")
        print("7. Logout")

        try:
            pilih = input("Pilih Menu : ").strip()

            # Lihat Stok Alat
            if pilih == "1":
                os.system("cls || clear")
                print("=== STOK ALAT ===")
                if not labGear:
                    print("Belum ada alat.")
                else:
                    for nama, info in labGear.items():
                        print(f"- {nama} | Jumlah: {info['jumlah']} | Status: {info['status']} | Peminjam: {info['peminjam']}")

                    # Tambahan penggunaan cek_jumlah_alat()
                    tanya = input("\nIngin cek jumlah alat tertentu? (y/n): ").lower().strip()
                    if tanya == "y":
                        nama_cek = input("Masukkan nama alat: ").strip()
                        jumlah = cek_jumlah_alat(nama_cek)
                        if jumlah is not None:
                            print(f"Jumlah alat '{nama_cek}' adalah: {jumlah}")
                input("Tekan Enter...")

            # Tambah alat
            elif pilih == "2" and role == "Admin":
                os.system("cls || clear")
                print("=== TAMBAH ALAT ===")
                nama = input("Nama Alat : ").strip()
                if nama == "":
                    print("Nama alat tidak boleh kosong!")
                elif nama in labGear:
                    print("Alat sudah ada!")
                else:
                    tambah_alat(nama)
                input("Tekan Enter...")

            # Update status
            elif pilih == "3" and role == "Admin":
                os.system("cls || clear")
                print("=== UPDATE STATUS ===")
                if not labGear:
                    print("Tidak ada alat yang bisa diupdate.")
                else:
                    for i, alat in enumerate(labGear.keys(), start=1):
                        print(f"{i}. {alat} - {labGear[alat]['status']}")
                    no = input("Pilih nomor alat: ").strip()
                    if no.isdigit():
                        idx = int(no) - 1
                        if 0 <= idx < len(labGear):
                            namaAlat = list(labGear.keys())[idx]
                            print("1. Dipinjam\n2. Rusak\n3. Tersedia")
                            aksi = input("Pilih status : ").strip()
                            if aksi == "1":
                                peminjam = input("Nama Peminjam : ").strip()
                                if peminjam:
                                    labGear[namaAlat]["status"] = "dipinjam"
                                    labGear[namaAlat]["peminjam"] = peminjam
                                    print("Status alat diperbarui menjadi Dipinjam.")
                                else:
                                    print("Nama peminjam tidak boleh kosong.")
                            elif aksi == "2":
                                labGear[namaAlat]["status"] = "rusak"
                                labGear[namaAlat]["peminjam"] = "-"
                                print("Status alat diperbarui menjadi Rusak.")
                            elif aksi == "3":
                                labGear[namaAlat]["status"] = "tersedia"
                                labGear[namaAlat]["peminjam"] = "-"
                                print("Status alat diperbarui menjadi Tersedia.")
                            else:
                                print("Pilihan tidak valid.")
                        else:
                            print("Nomor alat tidak valid!")
                    else:
                        print("Masukkan angka!")
                input("Tekan Enter...")

            # Hapus alat
            elif pilih == "4" and role == "Admin":
                os.system("cls || clear")
                print("=== HAPUS ALAT ===")
                if not labGear:
                    print("Tidak ada alat yang bisa dihapus.")
                else:
                    for i, alat in enumerate(labGear.keys(), start=1):
                        print(f"{i}. {alat}")
                    no = input("Pilih nomor alat: ").strip()
                    if no.isdigit():
                        idx = int(no) - 1
                        if 0 <= idx < len(labGear):
                            namaAlat = list(labGear.keys())[idx]
                            konfirm = input(f"Hapus {namaAlat}? (y/n): ").lower().strip()
                            if konfirm == "y":
                                del labGear[namaAlat]
                                print("Alat berhasil dihapus.")
                            else:
                                print("Dibatalkan.")
                        else:
                            print("Nomor alat tidak valid.")
                    else:
                        print("Masukkan angka!")
                input("Tekan Enter...")

            # Lihat daftar user (khusus admin)
            elif pilih == "5" and role == "Admin":
                tampilkan_daftar_user()

            # Hitung total alat (rekursif)
            elif pilih == "6":
                total = hitung_total_alat()
                print(f"Total semua alat di lab: {total}")
                input("Tekan Enter...")

            elif pilih == "7":
                sedangLogin = False
                username = ""
                role = ""
                print("Logout berhasil!")
                input("Tekan Enter...")

            else:
                raise ValueError("Pilihan tidak valid atau akses ditolak!")

        except ValueError as e:
            print("Error:", e)
            input("Tekan Enter...")
