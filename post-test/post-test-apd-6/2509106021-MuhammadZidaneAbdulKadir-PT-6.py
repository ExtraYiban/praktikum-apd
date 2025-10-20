import os
from data import Users, labGear
from status import *

while programBerjalan:
    os.system("cls || clear")

    if not sedangLogin:
        print("=== Selamat Datang di Lab GEAR ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
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
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

    else:
        os.system("cls || clear")
        print(f"=== Login sebagai {username} ({role}) ===")
        print("1. Lihat Stok Alat")
        if role == "Admin":
            print("2. Tambah Alat")
            print("3. Update Status Alat")
            print("4. Hapus Alat")
        print("5. Logout")

        pilih = input("Pilih Menu : ").strip()

        if pilih == "1":
            os.system("cls || clear")
            print("=== STOK ALAT ===")
            if not labGear:
                print("Belum ada alat.")
            else:
                for nama, info in labGear.items():
                    print(f"- {nama} | Jumlah: {info['jumlah']} | Status: {info['status']} | Peminjam: {info['peminjam']}")
            input("Tekan Enter...")

        elif pilih == "2" and role == "Admin":
            os.system("cls || clear")
            print("=== TAMBAH ALAT ===")
            nama = input("Nama Alat : ").strip()
            if nama == "":
                print("Nama alat tidak boleh kosong!")
            elif nama in labGear:
                print("Alat sudah ada!")
            else:
                jumlah = input("Jumlah : ").strip()
                if jumlah.isdigit() and int(jumlah) > 0:
                    labGear[nama] = {"jumlah": int(jumlah), "status": "tersedia", "peminjam": "-"}
                    print("Alat berhasil ditambahkan!")
                else:
                    print("Jumlah harus berupa angka lebih dari 0.")
            input("Tekan Enter...")

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

        elif pilih == "5":
            sedangLogin = False
            username = ""
            role = ""
            print("Logout berhasil!")
            input("Tekan Enter...")

        else:
            print("Pilihan tidak valid atau akses ditolak!")
            input("Tekan Enter...")
