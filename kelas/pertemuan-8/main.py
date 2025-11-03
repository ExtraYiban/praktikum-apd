import random
print(random.randint(1,5))
acak = "apcd"
pilih_acak = ["pisang","rambutan","manggis"]
print(random.choice(pilih_acak))
print(random.choice(acak))
kumpulan_angka = "123456789"
hasil = ""
for i in range(4):
    hasil += random.choice(kumpulan_angka)
print(hasil)
acak_kartu = ["1 wajik","5 wajik","5 wajik"]
random.shuffle(acak_kartu)
print(acak_kartu)
