import os
from prettytable import PrettyTable
from data import Users
from utils.warna import TITLE, RESET

def tampilkan_header():
    print(TITLE + "=== SISTEM LAB GEAR UNIVERSITAS ===" + RESET)
    print("Selamat datang di sistem manajemen alat laboratorium\n")

def tampilkan_daftar_user():
    os.system("cls || clear")
    print(TITLE + "=== DAFTAR USER TERDAFTAR ===" + RESET)

    table = PrettyTable()
    table.field_names = ["Username", "Role"]

    for user, info in Users.items():
        table.add_row([user, info["role"]])

    print(table)
    input("\nTekan Enter untuk kembali...")
