x = 5*5

def perkalian():
    x = 5 * 3
    print(x)

perkalian()

def perkenalan(nama):
    print(f"Halo {nama} selamat Berbelanja")

          
perkenalan("yoga")

def luasPersegiPanjang(panjang,lebar):
    luas = panjang * lebar
    print(f"Luas dari persegi panjang {luas}")

luasPersegiPanjang(5,3)

def luasPersegi(sisi):
    luas = sisi * sisi
    return luas


print(f" Luas Persegi {luasPersegi(8)}")

def volumePersegi(sisi):
    volume = luasPersegi(sisi) * sisi
    print(f"Volume persegi : {volume}")


luasPersegi(9)
volumePersegi(6)

def faktorial(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * faktorial(n - 1)

hasil = faktorial(7)
print(f"hasil dari 7! adalah: {hasil}")

# fungsi untuk menampilkan menu
def show_menu():
        print ("\n")
        print ("----------- MENU---------- ")
        print ("[1] Show Data")
        print ("[2] Insert Data")
        print ("[3] Edit Data")
        print ("[4] Delete Data")
        print ("[5] Exit")
        menu = input("PILIH MENU> ")
        print ("\n")
        if menu == "1":
                show_data()
        elif menu == "2":
            insert_data()
        elif menu == "3":
            edit_data()
        elif menu == "4":
            delete_data()
        elif menu == "5":
            exit()
        else:
            print ("Salah pilih!")

# Fungsi untuk menampilkan semua data
film = []
def show_data():
        if len(film) <= 0:
                print("Belum Ada data")
        else:
            print("ID | Judul Film")
        for indeks in range(len(film)):
            print(indeks, "|", film[indeks])

        # Fungsi untuk menambah data
def insert_data():
        film_baru = input("Judul Film: ")
        film.append(film_baru)
        print("Film berhasil ditambahkan!")

    # Fungsi untuk mengedit data
def edit_data():
        show_data()
        indeks = int(input("Inputkan ID film: "))
        if indeks >= len(film) or indeks < 0:
                print("ID salah")

        else:
            judul_baru = input("Judul baru: ")
            film[indeks] = judul_baru
            print("Film berhasil diupdate!")

        # Fungsi untuk menghapus data
def delete_data():
        show_data()
        indeks = int(input("Inputkan ID film: "))
        if indeks >= len(film) or indeks < 0:
                print("ID salah")
        else:
            film.remove(film[indeks])
            print("Film berhasil dihapus!")

        # fungsi untuk menampilkan menu
def show_menu():
        print ("\n")
        print ("----------- MENU---------- ")
        print ("[1] Show Data")
        print ("[2] Insert Data")
        print ("[3] Edit Data")
        print ("[4] Delete Data")
        print ("[5] Exit")
        menu = input("PILIH MENU :  ")
        print ("\n")

        if menu == "1":
                show_data()
        elif menu == "2":
            insert_data()
        elif menu == "3":
            edit_data()
        elif menu == "4":
            delete_data()
        else:
            print('Tidak ada di menu')


while True:
    show_menu()
