import os
from data import Users,labGear
from status import *

while programBerjalan:
    os.system("cls")

    if not sedangLogin:
        print("Selamat Datang Di Lab GEAR")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Pilihan : ").strip()

        if pilih == "1":
            # Login
            os.system("cls || clear")
            print("===LOGIN====")
            inpUsername = input("Username : ")
            inpPassword = input("Password : ")

            loginSukses = False
            for u in Users:
                if u[0] == inpUsername and u[1] == inpPassword:
                    sedangLogin = True
                    role = u[2]
                    username = inpUsername
                    loginSukses = True
                    print("Login Berhasil!")
                    input("Tekan Enter... ")
                    break
            
            if not loginSukses:
                print("Gagal Login!")
                input("Tekan Enter ...")
        
        elif pilih == "2":
            # Register
            os.system("cls || clear")
            print("===REGISTER===")
            newUser = input("Username Baru : ").strip()
            if newUser == "":
                print("Username tidak boleh kosong")
            else:
                usernameAda = False
                for u in Users:
                    if u[0] == newUser:
                        usernameAda = True
                if usernameAda:
                    print("Username sudah dipakai!")
                else:
                    newPass= input("Password : ").strip()
                    if newPass == "":
                        print("Password tidak boleh kosong")
                    else:
                        Users.append([newUser,newPass,"user"])
                        print("Registrasi Berhasil")
                input("tekan enter... ")
        
        elif pilih == "3":
            programBerjalan = False

        else:
            input("Pilihan Tidak Valid!, Tekan Enter... ")
    else:
        # Menu Setelah Login
        os.system("cls || clear")
        print(f"====Masuk Sebagai: {username} ({role})====")
        print("1. Lihat Stok")
        if role == "Admin":
            print("2. Tambah Alat")
            print("3. Update Status")
            print("4. Hapus Alat")
        print("5. Logout")
        pilih = input("Pilih : ").strip()

        if pilih == "1":
            # Read
            os.system("cls || clear")
            print("=== Stok Alat ===")
            if len(labGear) == 0:
                print("Belum Ada Alat!")
            else:
                for i in range(len(labGear)):
                    g = labGear[i]
                    print(f"{i+1}. {g[0]} | Jumlah : {g[1]} | Kondisi : {g[2]} | Peminjam : {g[3]} ")
            input("Tekan Enter... ")

        elif pilih == "2" and role == "Admin":
            # Create
            os.system("cls || clear")
            nama = input("Nama Alat : ").strip()
            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                duplikat = False
                for g in labGear:
                    if g[0].lower() == nama.lower():
                        duplikat = True
                    if duplikat:
                        print("Alat sudah ada!")
                    else:
                        jumlahStr = input("Jumlah : ").strip()
                        if jumlahStr.isdigit() and int(jumlahStr) > 0:
                            labGear.append([nama,int(jumlahStr),"tersedia","-"])
                            print("Alat Ditambahkan!")
                            break
                        else:
                            print("Jumlah harus angka > 0!")
            input("Tekan Enter... ")

        elif pilih == "3" and role == "Admin":
            # Update
            if len(labGear) == 0:
                print("Tidak ada alat untuk di update!")
                input("Tekan Enter...")
                continue
            
            os.system("cls || clear")
            for i in range(len(labGear)):
                g = labGear[i]
                print(f"{i+1}. {g[0]} - {g[2]}")
            noStr = input("Pilih nomor alat: ").strip()
            if noStr.isdigit():
                idx = int(noStr) - 1
                if 0 <= idx < len(labGear):
                    print("1.Dipinjam\n2. Rusak\n3. Tersedia")
                    aksi = input("Pilih Status : ").strip()
                    if aksi == "1":
                        peminjam = input("Nama Peminjam : ").strip()
                        if peminjam != "":
                            labGear[idx][2] = "dipinjam"
                            labGear[idx][3] = peminjam
                            print("Status : Dipinjam")
                        else:
                            print("Nama Peminjam Wajib diisi!")
                    elif aksi == "2":
                        labGear[idx][2] = "Rusak"
                        labGear[idx][3] = "-"
                        print("Status Rusak")
                    elif aksi == "3":
                        labGear[idx][2] = "tersedia"
                        labGear[idx][3] = "-"
                        print("Status : tersedia")
                    else:
                        print("Pilihan Tidak valid!")
                else:
                    print("Nomor Alat Tidak Valid!")
            else:
                print("Masukkan angka!")
            input("Tekan Enter...")
        elif pilih == "4" and role == "Admin":
            # Delete
            if len(labGear) == 0:
                print("Tidak ada alat untuk dihapus!")
                print("Tekan Enter... ")
                continue
            os.system("cls")
            for i in range(len(labGear)):
                print(f"{i+1}. {labGear[i][0]}")
            noStr = input("Pilih nomor alat yang dihapus: ").strip()
            if noStr.isdigit():
                idx = int(noStr) - 1
                if 0 <= idx < len(labGear):
                    konfirm = input(f"Hapus {labGear[idx][0]}? (y/n): ").strip().lower()
                    if konfirm == "y":
                        del labGear[idx]
                        print("Alat dihapus!")
                    else:
                        print("dibatalkan.")
                else:
                    print("Nomor tidak valid!")
            else:
                print("Masukkan Angka!")
            input("Tekan Enter...")
        elif pilih == "5":
            #Logout
            sedangLogin = False
            role = ""
            username = ""
            print("Berhasil logout.")
            input("Tekan Enter... ")
        else:
            input("Pilihan tidak valid atau akses ditolak. Tekan Enter....")
print("Terima Kasih!, Program Selesai.")