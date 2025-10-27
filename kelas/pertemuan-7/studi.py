try:
    nama = input("Berikan nama: ")
    if nama.strip() == "":
        raise ValueError("Nama Tidak Boleh kosong atau hanya berisi spasi saja")

except ValueError as e:
    print(e)
