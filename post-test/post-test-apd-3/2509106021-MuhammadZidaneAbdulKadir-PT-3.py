#                                __________
#                       ________|          |________
#                      |       /   ||||||   \       |
#                      |     ,'              `.     |
#                      |   ,'                  `.   |
#                      | ,'   ||||||||||||||||   `. |
#                      ,'  /____________________\  `.
#                     /______________________________\
#                    |                                |
#                    |                                |
#                    |                                |
#                    |________________________________|
#                      |____________________------__|
#
#          ,----------------------------------------------------,
#          | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
#          |                                                    |
#          |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
#          |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
#          | [][_][][][][][][][][][][][][]||     []    [][][][] |
#          | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
#          |   [__][________________][__]              [__][]|| |
#          `----------------------------------------------------'
# ______         _        _____         _     _____ 
# | ___ \       | |      |_   _|       | |   |____ |
# | |_/ /__  ___| |_ ______| | ___  ___| |_      / /
# |  __/ _ \/ __| __|______| |/ _ \/ __| __|     \ \
# | | | (_) \__ \ |_       | |  __/\__ \ |_  .___/ /
# \_|  \___/|___/\__|      \_/\___||___/\__| \____/ 


# Data login
username_db = "zidan"
password_db = "021"

print("=== Selamat Datang di Toko ===")
status = input("Apakah Anda member? (y/n): ")

# Proses login jika member
if status == "y":
    print("\n=== Login Member ===")
    user = input("Masukkan Username: ")
    pw = input("Masukkan Password: ")

    # Autentikasi dengan ternary operator
    login = True if (user == username_db and pw == password_db) else False

    if not login:
        print("Login gagal! Program selesai.")
        exit()
    else:
        print("Login berhasil, silakan belanja!\n")
else:
    login = False
    print("\nAnda berbelanja sebagai Non-Member.\n")

# Menu produk
print("=== Menu Produk ===")
print("1. Pensil    - Rp5.000")
print("2. Buku      - Rp12.000")
print("3. Penghapus - Rp3.000")

# Input jumlah (tanpa looping)
jml_pensil = int(input("\nMasukkan jumlah Pensil    : "))
jml_buku = int(input("Masukkan jumlah Buku      : "))
jml_penghapus = int(input("Masukkan jumlah Penghapus : "))

# Hitung total
total = (jml_pensil * 5000) + (jml_buku * 12000) + (jml_penghapus * 3000)

# Output struk
print("\n=== Struk Belanja ===")
if status == "y" and login:
    diskon = total * 0.15
    harga_akhir = total - diskon
    print(f"Harga sebelum diskon : Rp{total:,}")
    print(f"Diskon (15%)         : Rp{diskon:,}")
    print(f"Total bayar          : Rp{harga_akhir:,}")
else:
    print(f"Total bayar          : Rp{total:,}")

print("\nTerima kasih sudah berbelanja!")