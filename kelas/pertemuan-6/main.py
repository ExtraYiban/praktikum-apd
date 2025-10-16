buah = {"apel","jeruk","mangge","apel"}
for i in buah:
    print(i)
    print(i,end=" ")

angka= [1,1,2,3,4,5,6,7]
print(set(angka))

daftar_buku = {
    "Novel": "Bumi Manusia",
    "Buku2" : "Laut Bercerita"
}
print(daftar_buku)

Biodata = {
    "Nama" : "Ananda Daffa Harahap",
    "NIM" : 2409106050,
    "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" : True,
    "Social Media" : {
    "Instagram" : "daffahrhap"
    }
}

for i,j in Biodata.items():
    print(i)
    print(j)

print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Social Media']['Instagram']}")
print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get('Nama'))

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Sebelum Ditambah
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print(Film)

del Film["The Conjuring"]
print(Film)

Musik = {
    "The Chainsmoker": ["All we Know", "The Paris"],
    "Alan Walker": ["Alone", "Lily"],
    "Neffex": ["Best of Me",['tes','halo'], "Memories"],
    'Paramore' : ["Misery Business", "Ain't It Fun", 
                ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
}

print(Musik['Paramore'][2][1][1])

angka = {}
print(type(angka))

print()
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}

#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)