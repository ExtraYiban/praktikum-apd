import os
from data import Users, labGear
from status import *
from utils.tampilan import tampilkan_header, tampilkan_daftar_user
from utils.alat import cek_jumlah_alat, tambah_alat, tampilkan_stok_alat, hitung_total_alat
from utils.warna import SUCCESS, ERROR, WARNING, TITLE, INFO, RESET

while programBerjalan:
    os.system("cls || clear")
    tampilkan_header()

    if not sedangLogin:
        print(INFO + "1. Login")
        print(INFO + "2. Register")
        print("3. Keluar" + RESET)
        try:
            pilih = input("Pilihan : ").strip()
            if pilih == "1":
                os.system("cls || clear")
                print(TITLE + "=== LOGIN ===" + RESET)
                usernameInput = input("Username : ").strip()
                passwordInput = input("Password : ").strip()

                if usernameInput in Users and Users[usernameInput]["password"] == passwordInput:
                    sedangLogin = True
                    username = usernameInput
                    role = Users[usernameInput]["role"]
                    print(SUCCESS + "Login Berhasil!" + RESET)
                else:
                    print(ERROR + "Login gagal! Username atau password salah." + RESET)
                input("Tekan Enter...")

            elif pilih == "2":
                os.system("cls || clear")
                print(TITLE + "=== REGISTER ===" + RESET)
                newUser = input("Username Baru : ").strip()

                if newUser == "":
                    print(ERROR + "Username tidak boleh kosong!" + RESET)
                elif newUser in Users:
                    print(WARNING + "Username sudah digunakan!" + RESET)
                else:
                    newPass = input("Password : ").strip()
                    if newPass == "":
                        print(ERROR + "Password tidak boleh kosong!" + RESET)
                    else:
                        Users[newUser] = {"password": newPass, "role": "user"}
                        print(SUCCESS + "Registrasi Berhasil!" + RESET)
                input("Tekan Enter...")

            elif pilih == "3":
                programBerjalan = False
                print(WARNING + "Keluar dari program..." + RESET)

            else:
                raise ValueError("Pilihan tidak valid!")

        except ValueError as e:
            print(ERROR + "Error: " + str(e))
            input("Tekan Enter...")

    else:
        os.system("cls || clear")
        print(TITLE + f"=== Login sebagai {username} ({role}) ===" + RESET)
        print(INFO + "1. Lihat Stok Alat" + RESET)
        if role == "Admin":
            print("2. Tambah Alat")
            print("3. Update Status Alat")
            print("4. Hapus Alat")
            print("5. Lihat Daftar User")
        print("6. Hitung Total Jumlah Alat (rekursif)")
        print("7. Logout")

        try:
            pilih = input("Pilih Menu : ").strip()

            if pilih == "1":
                tampilkan_stok_alat()
                tanya = input("\nIngin cek jumlah alat tertentu? (y/n): ").lower().strip()
                if tanya == "y":
                    nama_cek = input("Masukkan nama alat: ").strip()
                    jumlah = cek_jumlah_alat(nama_cek)
                    if jumlah is not None:
                        print(SUCCESS + f"Jumlah alat '{nama_cek}' adalah: {jumlah}" + RESET)
                input("Tekan Enter...")

            elif pilih == "2" and role == "Admin":
                os.system("cls || clear")
                print(TITLE + "=== TAMBAH ALAT ===" + RESET)
                nama = input("Nama Alat : ").strip()
                if nama == "":
                    print(ERROR + "Nama alat tidak boleh kosong!" + RESET)
                elif nama in labGear:
                    print(WARNING + "Alat sudah ada!" + RESET)
                else:
                    tambah_alat(nama)
                input("Tekan Enter...")

            elif pilih == "3" and role == "Admin":
                os.system("cls || clear")
                print(TITLE + "=== UPDATE STATUS ===" + RESET)
                if not labGear:
                    print(WARNING + "Tidak ada alat yang bisa diupdate." + RESET)
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
                                    print(SUCCESS + "Status alat diperbarui menjadi Dipinjam." + RESET)
                                else:
                                    print(ERROR + "Nama peminjam tidak boleh kosong." + RESET)
                            elif aksi == "2":
                                labGear[namaAlat]["status"] = "rusak"
                                labGear[namaAlat]["peminjam"] = "-"
                                print(WARNING + "Status alat diperbarui menjadi Rusak." + RESET)
                            elif aksi == "3":
                                labGear[namaAlat]["status"] = "tersedia"
                                labGear[namaAlat]["peminjam"] = "-"
                                print(SUCCESS + "Status alat diperbarui menjadi Tersedia." + RESET)
                            else:
                                print(ERROR + "Pilihan tidak valid." + RESET)
                        else:
                            print(ERROR + "Nomor alat tidak valid!" + RESET)
                    else:
                        print(ERROR + "Masukkan angka!" + RESET)
                input("Tekan Enter...")

            elif pilih == "4" and role == "Admin":
                os.system("cls || clear")
                print(TITLE + "=== HAPUS ALAT ===" + RESET)
                if not labGear:
                    print(WARNING + "Tidak ada alat yang bisa dihapus." + RESET)
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
                                print(SUCCESS + "Alat berhasil dihapus." + RESET)
                            else:
                                print(WARNING + "Dibatalkan." + RESET)
                        else:
                            print(ERROR + "Nomor alat tidak valid." + RESET)
                    else:
                        print(ERROR + "Masukkan angka!" + RESET)
                input("Tekan Enter...")

            elif pilih == "5" and role == "Admin":
                tampilkan_daftar_user()

            elif pilih == "6":
                total = hitung_total_alat()
                print(SUCCESS + f"Total semua alat di lab: {total}" + RESET)
                input("Tekan Enter...")

            elif pilih == "7":
                sedangLogin = False
                username = ""
                role = ""
                print(WARNING + "Logout berhasil!" + RESET)
                input("Tekan Enter...")

            else:
                raise ValueError("Pilihan tidak valid atau akses ditolak!")

        except ValueError as e:
            print(ERROR + "Error: " + str(e))
            input("Tekan Enter...")