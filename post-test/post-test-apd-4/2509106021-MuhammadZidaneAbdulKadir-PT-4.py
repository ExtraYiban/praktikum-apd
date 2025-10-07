import os

username_db = "zidan"
password_db = "021"

while True:
    print("=== Selamat Datang di Toko ===")
    status = input("Apakah Anda member? (y/n): ")
    login = False
    if status == "y":
        kesempatan = 3
        while kesempatan > 0:
            print("\n=== Login Member ===")
            user = input("Masukkan Username: ")
            pw = input("Masukkan Password: ")

            if user == "" or pw == "":
                print("Input tidak boleh kosong!")
                continue

            if user == username_db and pw == password_db:
                login = True
                print("Login berhasil, silakan belanja!\n")
                break
            else:
                kesempatan -= 1
                if kesempatan > 0:
                    print(f"Login gagal! Sisa percobaan: {kesempatan}")
                else:
                    print("Login gagal 3 kali! Anda dianggap Non-Member.\n")
                    login = False
                    break
    else:
        print("\nAnda berbelanja sebagai Non-Member.\n")

    total = 0
    keranjang = ""

    while True:
        print("=== Menu Produk ===")
        print("1. Pensil    - Rp5.000")
        print("2. Buku      - Rp12.000")
        print("3. Penghapus - Rp3.000")
        print("4. Checkout")

        pilih = input("\nPilih menu (1-4): ")

        if pilih == "1":
            os.system("cls")
            total += 5000
            keranjang += "Pensil - Rp5.000\n"
            print("Pensil berhasil ditambahkan ke keranjang.")
            print(f"Total sementara: Rp{total:,}\n")

        elif pilih == "2":
            os.system("cls")
            total += 12000
            keranjang += "Buku - Rp12.000\n"
            print("Buku berhasil ditambahkan ke keranjang.")
            print(f"Total sementara: Rp{total:,}\n")

        elif pilih == "3":
            os.system("cls")
            total += 3000
            keranjang += "Penghapus - Rp3.000\n"
            print("Penghapus berhasil ditambahkan ke keranjang.")
            print(f"Total sementara: Rp{total:,}\n")

        elif pilih == "4":
            print("\n=== Struk Belanja ===")
            print(keranjang if keranjang != "" else "Tidak ada barang dibeli.")
            if login:
                diskon = total * 0.15
                harga_akhir = total - diskon
                print(f"Harga sebelum diskon : Rp{total:,}")
                print(f"Diskon (15%)         : Rp{diskon:,}")
                print(f"Total bayar          : Rp{harga_akhir:,}")
            else:
                print(f"Total bayar          : Rp{total:,}")
            print("\nTerima kasih sudah berbelanja!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

    ulang = input("Apakah ingin memulai transaksi baru? (y/n): ")
    if ulang != "y":
        print("Program selesai. Sampai jumpa!")
        break



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣤⠒⠒⠒⠚⣭⡟⠻⠍⠉⠉⠄⠀⠀⠀⠀⠌⢳⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢸⠘⡌⡀⠀⠴⠁⢻⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⡟⠠⠀⡇⢰⢛⡶⡝⠀⠀⢠⠀⠸⠀⠀⠀⢀⠀⠈⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⡇⠀⣀⡆⠏⣻⣃⠁⠀⠀⠀⠀⠀⠆⠀⠐⠀⠐⠀⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢰⡗⠁⣠⣤⡤⡀⠀⠑⣄⠀⠀⠀⠀⣀⣨⣤⣤⣀⠀⢸⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢹⣴⣻⣧⣤⣼⣤⣀⢀⠀⠁⠀⣰⣾⣋⣽⣿⢿⣤⢕⡘⡆⠀⠀
# ⠀⠀⠀⠀⠀⠀⣾⣿⢟⡭⠓⠒⠩⣟⣿⡇⠀⢰⣿⢟⠍⠂⠀⠈⠙⣷⣸⠃⠀⠀
# ⠀⠀⠀⠀⠀⠀⡿⡟⠁⢰⣿⣯⡦⠈⣿⣿⠀⣾⣇⠃⢀⣾⣥⣬⡄⠘⣿⡀⠀⠀
# ⠀⠀⠀⠀⠀⢨⡇⡷⣤⡈⠻⠿⠃⢀⣿⣿⠀⣿⣏⣇⠈⠻⠛⠗⢁⣼⠋⢷⠀⠀
# ⠀⠀⠀⠀⠀⢹⠁⠸⢾⣷⣦⣤⣴⡾⠁⢡⠀⠠⠉⠫⣳⠦⡤⣾⡿⠋⠀⢸⠀⠀
# ⠀⠀⠀⠀⠀⢸⣀⠀⠀⠈⠉⠉⠀⠀⢀⠏⠀⠀⠡⡀⠀⠉⠉⠉⠁⠀⠀⢸⠄⠀
# ⠀⠀⠀⠀⠀⠈⢻⡷⣖⣶⣤⣤⣶⡀⠘⡈⠀⠀⠄⠑⣶⣤⣀⣀⣤⣶⣾⠟⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢳⣶⣴⣿⡿⠋⣤⠀⠀⡀⠀⠀⢀⠘⢯⣽⣿⣿⣾⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢸⡆⣹⣿⢤⡀⣿⣿⣿⣭⣽⡿⠟⢀⣠⠬⢛⢹⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⡏⢸⢸⠳⣝⢶⣬⣉⣉⣠⣤⡶⢛⠕⠀⡄⡎⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⠘⡌⠛⢯⠒⠋⠭⣭⠵⠖⠉⠀⡰⡃⡠⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢸⢿⢠⡇⡀⢤⠀⠉⠉⠿⠟⠁⠀⢀⡴⡇⠀⠀⢇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣼⡞⠸⡇⠀⠐⠈⠒⠤⠤⣤⣤⣖⠷⠁⠀⠀⣠⠋⠇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢰⣿⣷⠀⣇⠇⠠⠤⡀⠅⠘⠛⢻⠁⠀⠀⠀⠀⣿⡁⢰⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣸⣿⣿⡀⡗⡬⢀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠸⠀⣿⠀⠈⡆⠀⠀
# ⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⡗⣌⢘⠀⠀⠀⠀⠀⠐⠀⠀⠀⠈⠀⣻⣧⠀⢱⡄⠀
# ⠀⠀⠀⠀⠀⢸⣿⣿⡟⣧⣣⡇⠈⠄⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⡿⣿⣷⣼⠁⠀
# ⠀⠀⠀⠀⠀⢸⣿⣿⡇⣿⡇⡇⠀⡇⠀⠀⠂⠀⢠⠀⠀⠀⠀⠀⡇⡹⠁⢸⡇⠀
# ⠀⠀⠀⠀⠀⢸⡟⢻⡇⣸⢧⡇⠀⡇⠀⠀⠀⠀⢘⠀⠀⠀⠀⠀⡇⡇⠀⢸⠁⠀
# ⠀⠀⠀⠀⠀⠀⣯⡎⣿⣿⡏⠀⠀⡇⠀⠐⠀⠀⢸⠀⠀⠀⠀⠐⠀⠇⠠⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⣹⡆⢺⣿⣇⢀⠀⡇⠀⠈⠀⠀⠸⠘⠄⠀⠀⠀⢸⠀⣸⠁⠀⠀
# ⠀⠀⠀⠀⠀⠀⢿⢰⣜⣿⣿⡗⣠⡇⠀⠀⠀⠀⢸⢢⠀⠀⠀⢸⢀⣠⢳⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠘⢧⡻⣿⠀⢹⠲⡇⠄⠠⠀⠀⢼⠸⠀⠀⠀⡽⣸⡗⣼⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⢳⠾⠘⣿⡅⣿⠐⠀⢀⠀⣸⡃⠀⢀⣼⣷⣋⠜⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢨⠃⢐⣿⠙⣿⡟⠒⠚⠚⠛⡷⠖⣿⡿⠛⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⡘⡏⠀⣿⠁⠀⠀⠀⠀⡏⠃⢹⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⡟⣗⡃⢾⡇⠀⠀⠀⠀⡇⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢰⠃⠸⣧⠿⠧⢸⡇⠀⠀⠀⢰⡇⠠⠤⣻⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣼⠀⣼⢈⣗⠀⢘⣿⠀⠀⠀⢸⣷⢀⣲⡏⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢠⡏⠀⢹⢸⣿⣿⠞⢹⠀⠀⠀⢸⡛⠿⠟⡧⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣼⠀⠀⡌⢸⣏⡆⠀⢸⠀⠀⠀⢸⣹⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢰⠏⠀⠀⡅⠀⣿⣮⠀⢸⠀⠀⠀⢸⣯⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⡾⠁⠀⠀⡇⠀⣿⣯⠀⢸⠀⠀⠀⢸⣯⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢸⠇⢠⠁⠀⡇⠀⣿⡧⠀⢸⠀⠀⠀⢸⢻⡇⠈⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⡺⠀⠒⠀⢠⠃⣰⣿⣧⠀⢺⠀⠀⠀⡼⠽⠘⡰⢳⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢠⠇⠀⡄⠀⢸⣤⣿⠃⠀⠃⠘⡇⡀⢰⡇⠀⠀⠱⠘⢧⡀⠀⠀⠀⠀⠀
# ⠀⠀⠂⡼⠀⢠⣀⠀⢸⡟⠁⠀⠀⠀⡀⣯⠄⢸⣷⠀⠀⠀⠀⠪⡳⣄⠀⠀⠀⠀
# ⠀⠀⢸⠇⠀⠈⠍⠀⡈⠀⠀⠀⠀⠀⢹⡿⠒⢿⣿⠆⠀⠀⠀⢢⠀⠈⢳⡀⠀⠀
# ⠀⠀⡾⠀⠆⠃⡆⠀⠃⡠⠀⣀⠀⠀⣼⣏⠀⠌⣿⣧⠀⠀⢠⣠⣧⣀⡄⠙⢧⡀
# ⠀⢸⠃⠀⠨⠸⠁⠀⣀⠗⣼⣗⠶⢤⣿⡇⠀⠀⢸⣿⣄⠤⠿⣷⡬⠿⣆⠐⢢⣽
# ⠀⣾⡆⠀⠈⢰⠀⢀⡇⢠⣿⠃⠀⢰⣿⠁⠀⠀⠀⢻⣧⠀⠀⠘⣷⣀⣨⣷⣬⡯
# ⢀⣇⠀⠀⢣⠊⠀⠀⣿⣿⣇⠠⠄⣾⠂⠀⠀⠀⠀⠀⠻⣷⣲⣞⡿⠞⠛⠉⠁⠀
# ⣾⡇⠄⠠⠸⡀⠀⢸⣿⠹⢻⣿⣟⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀
