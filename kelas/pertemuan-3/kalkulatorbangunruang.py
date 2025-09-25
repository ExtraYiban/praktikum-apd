print("""
      KALKULATOR BANGUN RUANG
      1. Hitung Volume Kubus
      2. Hitung Volume Balok
      2. Hitung Volume Prisma
      """)

pilihan = int(input("Pilihan : "))

if pilihan == 1:
    sisi = int(input("Berapa Panjang sisi: "))
    sisi = sisi * sisi * sisi
    print(f"Volume Kubus Adalah {sisi}")
elif pilihan == 2:
    panjang = int(input("Berapa Panjang : "))
    lebar = int(input("Berapa Lebar : "))
    tinggi = int(input("Berapa tinggi : "))
    print(f"Volume Balok Adalah {panjang * lebar * tinggi}")
else:
    luasAlas = int(input("Berapa Luas Alas : "))
    tinggi = int(input("Berapa tinggi : "))
    print(f"Volume Prisma Adalah {luasAlas * tinggi}")