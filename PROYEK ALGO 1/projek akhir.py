import pandas as pd
import csv
import os 
import datetime as dt

list_jenisproduk = {
   1:"Alat persiapan lahan",
   2:"Alat penanaman",
   3:"Alat pemeliharaan tanaman",
   4:"Alat panen",
   5:"Alat pascapanen",
   6:"Bahan pertanian",
   7:"Pencarian"
}

list_jenisproduk1 = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e"
}
list_jenisproduk2 = {
    1:"a",
    2:"e",
    3:"b",
    4:"c",
    5:"d"
}
list_jenisproduk3 = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e"
}
list_jenisproduk4 = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e"
}
list_jenisproduk5 = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e"
}
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
        return None

    with open('RegTRIJAYA.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                print(f"Selamat datang, {username}!")
                jenis_produk(username)
                return username
        print("Login gagal! Username atau password salah.")
        return None


def jenis_produk(username):
    os.system('cls')
    print(f"Selamat datang, silahkan pilih jenis produk : ")
    for i in list_jenisproduk:
        print(i,".",list_jenisproduk[i])
    jenis = input("Pilihlah jenis produk (1/2/3/4/5/6): ")
    if jenis == '1':
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Persiapan Lahan  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            for i in list_jenisproduk1:
                print(i,".",list_jenisproduk1[i])

            pilih_produk1 = input("pilih produk: ")
            produk = ""
        
            if pilih_produk1 == "1":
                produk = "produk 1"
            elif pilih_produk1 == "2":
                produk = "produk 2"
            elif pilih_produk1 == "3":
                produk = "produk 3"
            elif pilih_produk1 == "4":
                produk = "produk 4"
            elif pilih_produk1 == "5":
                produk = "produk 5"
            else:
                print ("pilihan tidak tersedia!")
            print(f"{produk} adalah produk yang dipilih {username}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("pilih menu :").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk)
            elif keranjang_beli == "B":
                print(f"{produk} telah dibeli oleh {username}. Terima kasih!")
            else:
                print("pilihan tidak tersedia")
                
    elif jenis == '2':
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Penanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            print(list_jenisproduk2)
            pilih_produk2 = input("pilih produk: ")
            produk = ""
        
            if pilih_produk2 == "1":
                produk = "produk 1"
            elif pilih_produk2 == "2":
                produk = "produk 2"
            elif pilih_produk2 == "3":
                produk = "produk 3"
            elif pilih_produk2 == "4":
                produk = "produk 4"
            elif pilih_produk2 == "5":
                produk = "produk 5"
            else:
                print ("pilihan tidak tersedia!")
            print(f"{produk} adalah produk yang dipilih {username}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("pilih menu :").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk)
            elif keranjang_beli == "B":
                print(f"{produk} telah dibeli oleh {username}. Terima kasih!")
            else:
                print("pilihan tidak tersedia")
    elif jenis == '3':
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Pemeliharaan Tanaman  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            print(list_jenisproduk3) 
            pilih_produk3 = input("pilih produk: ")
            produk = ""
        
            if pilih_produk3 == "1":
                produk = "produk 1"
            elif pilih_produk3 == "2":
                produk = "produk 2"
            elif pilih_produk3 == "3":
                produk = "produk 3"
            elif pilih_produk3 == "4":
                produk = "produk 4"
            elif pilih_produk3 == "5":
                produk = "produk 5"
            else:
                print ("pilihan tidak tersedia!")
            print(f"{produk} adalah produk yang dipilih {username}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("pilih menu :").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk)
            elif keranjang_beli == "B":
                print(f"{produk} telah dibeli oleh {username}. Terima kasih!")
            else:
                print("pilihan tidak tersedia")
           
    elif jenis == '4':
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Panen  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            print(list_jenisproduk4)
            pilih_produk4 = input("pilih produk: ")
            produk = ""
        
            if pilih_produk4 == "1":
                produk = "produk 1"
            elif pilih_produk4 == "2":
                produk = "produk 2"
            elif pilih_produk4 == "3":
                produk = "produk 3"
            elif pilih_produk4 == "4":
                produk = "produk 4"
            elif pilih_produk4 == "5":
                produk = "produk 5"
            else:
                print ("pilihan tidak tersedia!")
            print(f"{produk} adalah produk yang dipilih {username}")
            print('''
            A. Masukkan keranjang
            B. Beli dan bayar
            ''')
            keranjang_beli = input("pilih menu :").strip().upper()
            if keranjang_beli == "A":
                keranjang(username, produk)
            elif keranjang_beli == "B":
                print(f"{produk} telah dibeli oleh {username}. Terima kasih!")
            else:
                print("pilihan tidak tersedia")

            # keranjang(username, produk)
        
    elif jenis == '5':
            print('''
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            $$$$$$$$$^^^^^  Alat Pascapanen  ^^^^^$$$$$$$$
            __________________ SELAMAT BERBELANJA ___________________
            ''')
            print(list_jenisproduk5)
    print(input("pilih produk: "))
    produk= ""
    if pilih_produk4 == "1":
                produk = "produk 1"
    elif pilih_produk4 == "2":
                produk = "produk 2"
    elif pilih_produk4 == "3":
                produk = "produk 3"
    elif pilih_produk4 == "4":
                produk = "produk 4"
    elif pilih_produk4 == "5":
                produk = "produk 5"
    else:
        print ("pilihan tidak tersedia!")
        print(f"{produk} adalah produk yang dipilih {username}")
        print('''
        A. Masukkan keranjang
        B. Beli dan bayar
        ''')
        keranjang_beli = input("pilih menu :").strip().upper()
        if keranjang_beli == "A":
                keranjang(username, produk)
        elif keranjang_beli == "B":
                print(f"{produk} telah dibeli oleh {username}. Terima kasih!")
        else:
            print("pilihan tidak tersedia")

    if jenis == '5':
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
with open('RegTRIJAYA.csv', 'r') as file:
        writer = csv.writer(file)
username = writer
            
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
def main():
    home()
main()

# def deskripsi_produk():
#     pass

# def data_pengiriman():
#     pass
    
# def pencarian():
#     pass

# def voucher():
#     pass

# def pembayaran():
    
