import pandas as pd
import csv
import os 
import datetime as dt

def home():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("$$$$$$$$$^^^^^  SELAMAT DATANG di TRIJAYA  ^^^^^$$$$$$$$")
    print('''
          1. Register
          2. Login
           ''')
    home = input("Pilih fitur : ")
    if home == "1":
        register()
    elif home == "2":
        login()



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
        elif otw_login == '1':
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
        print("Akun tidak terdaftar. Silakan daftar terlebih dahulu!.")
        return

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for i in reader:
            if i['username'] == username and i['password'] == password:
                print(f"Selamat datang, {username}!")
                return

    print("Login gagal! Username atau password salah.")
home()    


def jenis_produk(username):
    os.system('cls')
    print(f"Selamat datang, silahkan pilih jenis produk : ")
    print('''
    1. Alat persiapan lahan
    2. Alat penanaman
    3. Alat pemeliharaan tanaman
    4. Alat panen
    5. Alat pascapanen
    6. Bahan pertanian
    7. Pencarian
    ''')
    jenis = input("Pilihlah jenis produk (1/2/3/4/5/6): ")
    if jenis == '1':
        print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})

        ''')
# df = pd.read_csv("data_produk.csv", sep="\s+", header = None, names=['Name', 'Age', 'Height'])
# print(df)
        print(input("pilih produk: "))
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        
    elif jenis == '2':
        print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Penanaman  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})
        ''')
        print(input("pilih produk: "))
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
    elif jenis == '3':
        print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})
        ''')
        print(input("pilih produk: "))
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
    elif jenis == '4':
        print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Panen  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})
        ''')
        print(input("pilih produk: "))
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
    elif jenis == '5':
       print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})
        ''')
       print(input("pilih produk: "))
       print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
    elif jenis == '6':
        print('''
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
          $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
        __________________ SELAMAT BERBELANJA ___________________
        1. nama_produk ({stok})
        2. nama_produk ({stok})
        3. nama_produk ({stok})
        4. nama_produk ({stok})
        5. nama_produk ({stok})
        6. nama_produk ({stok})
        7. nama_produk ({stok})
        8. nama_produk ({stok})
        ''')
        print(input("pilih produk: "))
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
#     elif jenis == '7':
#         pass
with open('RegTRIJAYA.csv', 'r') as file:
        writer = csv.writer(file)
username = writer
jenis_produk(username)
    
def keranjang(username, produk):
    file_exists = os.path.isfile('KeranjangTRIJAYA.csv')
    with open('KeranjangTRIJAYA.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "produk"])
        writer.writerow([username, produk])
        print(f"{produk} berhasil ditambahkan ke keranjang!")
        input("Tekan enter untuk kembali.")
        jenis_produk(username)

# def deskripsi_produk():
#     pass

# def data_pengiriman():
#     pass
    
# def pencarian():
#     pass

# def voucher():
#     pass

# def pembayaran():
    