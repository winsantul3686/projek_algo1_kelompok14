import csv
import os

def register():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("______________________  REGISTER  ______________________")
    username = input("Masukkan username barumu: ").strip()
    password = input("Masukkan password barumu: ").strip()
    
    file_exists = os.path.isfile('RegTRIJAYA.csv')

    with open('RegTRIJAYA.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Password"])  # Tambahkan header jika file baru
        writer.writerow([username, password])
        print("Akun telah didaftarkan!!")

def login():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("________________________ LOGIN _________________________")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('RegTRIJAYA.csv'):  # Cek apakah file ada
        print("Belum ada akun yang terdaftar. Silakan daftar terlebih dahulu.")
        return

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username and row['Password'] == password:
                print(f"Selamat datang, {username}!")
                return

    print("Login gagal! Username atau password salah.")
register()