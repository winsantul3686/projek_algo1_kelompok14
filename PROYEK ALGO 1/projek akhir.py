import pandas as pd
import csv
import os 
import datetime as dt


def register():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("______________________  REGISTER  ______________________")
    username = input("Masukkan username anda: ").strip()
    password = input("Masukkan password anda: ").strip()
    
    file_exists = os.path.isfile('RegTRIJAYA.csv')

    with open('RegTRIJAYA.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:  
            writer.writerow(["username","password"])
        writer.writerow([username,password])
        print("________________________")
        print("Akun telah didaftarkan!!")
        print("________________________")
        print("1.Login")
        print("2.Selesai")
        otw_login = input ("pilihlah angka untuk selanjutnya (1/2) :")
        if otw_login == '2':
            print("=-=-=-=-=-=- Pendaftaran selesai! -=-=-=-=-=-=")
            input("klik enter untuk login")
        elif otw_login== '1':
            login()
        else:
            print("input tidak tersedia")



def login():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print("________________________ LOGIN _________________________")

    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not os.path.isfile('RegTRIJAYA.csv'): 
        print("Belum ada akun yang terdaftar. Silakan daftar terlebih dahulu.")
        return

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                print(f"Selamat datang, {username}!")
                return

    print("Login gagal! Username atau password salah.")
register()
login()

# def jenis_produk():
#     pass

# def daftar_produk():
#     pass

# def keranjang():
#     pass

# def deskripsi_produk():
#     pass

# def data_pengiriman():
#     pass
    
# def pencarian():
#     pass

# def voucher():
#     pass

# def pembayaran():
#     pass