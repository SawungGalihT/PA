import csv
import pwinput
from prettytable import PrettyTable
import sys

daftar_pc=[]
akun_admin=[]
akun_pelanggan=[]
data_pengguna=[]
data_admin=[]
data_transaksi=[]

def simpan_daftar_pc():
    with open("datapc.csv", "w", newline="") as new_file:
        fieldNames = ["nama", "harga/jam", "status"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=",", fieldnames=fieldNames)
        csv_writer.writeheader()
        for i in daftar_pc:
            csv_writer.writerow(i)

def simpan_daftar_pelanggan():
    with open("datapelanggan.csv", "w", newline="") as new_file:
        fieldNames = ["nama", "sandi" ,"saldo", "pin"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=",", fieldnames=fieldNames)
        csv_writer.writeheader()
        for i in akun_pelanggan:
            csv_writer.writerow(i)

def simpan_daftar_admin():
    with open("dataadmin.csv", "w", newline="") as new_file:
        fieldNames = ["nama", "sandi"]
        csv_writer = csv.DictWriter(
            new_file, delimiter=",", fieldnames=fieldNames)
        csv_writer.writeheader()
        for i in akun_admin:
            csv_writer.writerow(i)

def ambil_data_pc_csv():
    with open('datapc.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        daftar_pc.clear()
        for row in reader:
            daftar_pc.append(dict(row))

def ambil_data_pelanggan_csv():
    with open('datapelanggan.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        akun_pelanggan.clear()
        for row in reader:
            akun_pelanggan.append(dict(row))

def ambil_data_admin_csv():
    with open('dataadmin.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        akun_admin.clear()
        for row in reader:
            akun_admin.append(dict(row))

def tampil_data_pc():
    table = PrettyTable()
    table.title = "Daftar PC"
    table.field_names = ["Nomor","Nama PC", "Harga/Jam","Status"]
    for i in range(len(daftar_pc)):
        table.add_row([i+1,daftar_pc[i]["nama"], "Rp "+ str(daftar_pc[i]["harga/jam"]),daftar_pc[i]["status"]])
    print(table)

def tampil_data_pelanggan():
    table = PrettyTable()
    table.title = "Daftar Pelanggan"
    table.field_names = ["Nomor", "Nama","Sandi"]
    for i in range(len(akun_pelanggan)):
        table.add_row([i+1, akun_pelanggan[i]["nama"],akun_pelanggan[i]["sandi"]])
    print(table)

def tampil_data_admin():
    table = PrettyTable()
    table.title = "Daftar Admin"
    table.field_names = ["Nomor","Nama","Sandi"]
    for i in range(len(akun_admin)):
        table.add_row([i+1, akun_admin[i]["nama"],akun_admin[i]["sandi"]])
    print(table)

def tambah_data_pc():
    while True:
        tampil_data_pc()
        try:
            baru = {}
            nama = str(input("masukkan nama : "))
            harga = int(input("masukkan harga : "))
            status = "kosong"
            if " " in nama:
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            elif nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                baru.update({
                    "nama" : nama,
                    "harga/jam" : harga,
                    "status" : status
                            })
                daftar_pc.append(baru)
                simpan_daftar_pc()
                input("Data Berhasil Ditambahkan. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Harga Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")
        
def tambah_data_admin():
    while True:
        tampil_data_admin()
        try:
            baru = {}
            nama = str(input("Masukkan Nama Baru : "))
            sandi = int(input("Masukkan Sandi Baru : "))
            if " " in nama :
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            elif nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                baru.update({
                    "nama" : nama,
                    "sandi": sandi
                            })
                akun_admin.append(baru)
                simpan_daftar_admin()
                input("Data Berhasil Ditambahkan. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Sandi Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def hapus_data_pc():
    while True:
        tampil_data_pc()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Dihapus : "))
            if pil < 1 or pil > len(daftar_pc):
                input("Pilihan PC tidak valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali")
            else:
                daftar_pc.pop(pil-1)
                simpan_daftar_pc()
                input("Data Berhasil Dihapus. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Pilihan Data Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def hapus_data_pelanggan():
    while True:
        tampil_data_pelanggan()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Dihapus : "))
            if pil < 1 or pil > len(akun_pelanggan):
                input("Pilihan Pelanggan Tidak Valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali.")
            else:
                akun_pelanggan.pop(pil-1)
                simpan_daftar_pelanggan()
                input("Data Berhasil Dihapus. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Pilihan Data Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def hapus_data_admin():
    while True:
        tampil_data_admin()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Dihapus : "))
            if pil < 1 or pil > len(akun_admin):
                input("Pilihan Admin Tidak Valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali")
            else:
                akun_admin.pop(pil-1)
                simpan_daftar_admin()
                input("Data Berhasil Dihapus. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Pilihan Data Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def ubah_data_pc():
    while True:
        tampil_data_pc()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Diubah : "))
            if pil < 1 or pil > len(daftar_pc):
                input("Pilihan PC Tidak Valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali.")
                continue
            baru = {}
            nama = str(input("Masukkan Nama : "))
            harga = int(input("Masukkan Harga : "))
            status = daftar_pc[pil-1]["status"]
            if " " in nama:
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            elif nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                baru.update({
                    "nama" : nama,
                    "harga/jam" : harga,
                    "status" : status
                            })
                daftar_pc[pil-1] = baru
                simpan_daftar_pc()
                input("Data Berhasil Diubah. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Pilihan Data Dan Harga Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def ubah_data_pelanggan():
    while True:
        tampil_data_pelanggan()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Diubah : "))
            if pil < 1 or pil > len(akun_pelanggan):
                print("Pilihan Pelanggan Tidak Valid. Silakan Pilih Nomor Yang Sesuai.")
                continue
            baru = {}
            nama = str(input("Masukkan Nama : "))
            sandi = int(input("Masukkan Sandi : "))
            if " " in nama:
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            elif nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                saldo = akun_pelanggan[pil-1]["saldo"]
                pin = akun_pelanggan[pil-1]["pin"]
                baru.update({
                    "nama" : nama,
                    "sandi" : sandi,
                    "saldo" : saldo,
                    "pin" : pin,
                            })
                akun_pelanggan[pil-1] = baru
                simpan_daftar_pelanggan()
                input("Data Berhasil Diubah. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
                input("Masukkan Data Dengan Benar!! (Pilihan Data Dan Sandi Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def ubah_data_admin():
    while True:
        tampil_data_admin()
        try:
            pil = int(input("Data Ke Berapa Yang Ingin Diubah : "))
            if pil < 1 or pil > len(akun_admin):
                input("Pilihan Admin Tidak Valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali.")
                continue
            baru = {}
            nama = str(input("Masukkan Nama : "))
            sandi = int(input("Masukkan Sandi : "))
            if " " in nama:
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            elif nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                baru.update({
                    "nama" : nama,
                    "sandi" : sandi,
                            })
                akun_admin[pil-1] = baru
                simpan_daftar_admin()
                input("Data Berhasil Diubah. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
                input("Masukkan Data Dengan Benar!! (Pilihan Data Dan Sandi Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")

def menu_pc(akun):
    while True:
        tampil_data_pc()
        try:
            pilih_pc = int(input("Silahkan Pilih PC (nomor) : "))
            durasi = int(input("Silahkan Masukkan Durasi Pemakaian (jam): "))
            if pilih_pc < 1 or pilih_pc > len(daftar_pc):
                input("Nomor PC Tidak Valid. Silakan Pilih Nomor Yang Sesuai.\nTekan ENTER Untuk Kembali.")
                continue
            nama_user = str(akun["nama"])
            harga_pc = int(daftar_pc[pilih_pc - 1]["harga/jam"])
            saldo = int(akun["saldo"])
            total = harga_pc * durasi
            saldo_baru =str(saldo- total)
            if saldo >= total:
                daftar_pc[pilih_pc - 1]["status"] = "Sedang Digunakan "+akun["nama"]
                akun["saldo"] = saldo_baru
                checkout(saldo,pilih_pc - 1,durasi,total,nama_user)
                data_transaksi.append(total)
                simpan_daftar_pelanggan()
            else:
                input("\nSaldo Anda Tidak Mencukupi Untuk Menggunakan PC Ini. Tekan Enter Untuk Kembali")
            simpan_daftar_pc()
        except ValueError:
            input("Masukkan Angka Dalam Bentuk Angka !!!!\nTekan ENTER Untuk Kembali. ")
            return
        input("Tekan ENTER Untuk Kembali.")
        break

def checkout(jumlah, pc, durasi, total,akun):
    print("")
    cekot = PrettyTable()
    cekot.title = "Transaksi Berhasil"
    cekot.field_names = ["Nama PC", "Harga/Jam", "Durasi (jam)", "Saldo"]
    cekot.add_row([str(daftar_pc[pc]["nama"]), f"Rp {daftar_pc[pc]['harga/jam']}", durasi, f"Rp {jumlah}"])
    kembalian = jumlah - total
    cekot.add_row(["=============", "=============", "=============", "============="])
    cekot.add_row([ "Nama User", "Total", "Kembalian",""])
    cekot.add_row(["-------------", "-------------", "-------------", "-------------"])
    cekot.add_row([ akun,  f"Rp. {total}", f"Rp. {kembalian}",""])
    print(cekot)
    
def menu_admin(data_admin):
    while True:
        print("")
        print("="*10, "Selamat Datang, " + data_admin["nama"], "="*10)
        print("\nMenu Admin.")
        print("1. Lihat PC \t\t\t8. Lihat Admin.")
        print("2. Tambah PC \t\t\t9. Tambahkan Admin.")
        print("3. Hapus PC \t\t\t10. Hapus Admin")
        print("4. Edit Daftar PC \t\t11. Edit Admin.")
        print("5. Lihat Daftar Pelanggan \t12. Kembali.")
        print("6. Hapus Daftar Pelanggan")
        print("7. Edit Daftar Pelanggan")
        pil = str(input("Masukkan pilihan : "))

        if (pil == "1"):
            tampil_data_pc()
            input("Tekan Enter Untuk Kembali. ")
        elif (pil == "2"):
            tambah_data_pc()
        elif (pil == "3"):
            hapus_data_pc()
        elif (pil == "4"):
            ubah_data_pc()
        elif (pil == "5"):
            tampil_data_pelanggan()
            input("Tekan Enter Untuk Kembali. ")
        elif (pil == "6"):
            hapus_data_pelanggan()
        elif (pil == "7"):
            ubah_data_pelanggan()
        elif (pil == "8"):
            tampil_data_admin()
            input("Tekan Enter Untuk Kembali. ")
        elif (pil == "9"):
            tambah_data_admin()
        elif (pil == "10"):
            hapus_data_admin()
        elif (pil == "11"):
            ubah_data_admin()
        elif (pil == "12"):
            break
        else:
            input("Masukkan Pilihan Dengan Benar!!!! Tekan ENTER Untuk Kembali.")

def menu_pelanggan(data_pengguna,i):
    while True:
        ambil_data_pelanggan_csv()
        print("")
        print("="*10, "Selamat Datang, " + data_pengguna["nama"], "="*10)
        print("\nMenu Pelanggan.")
        print("1. Lihat Saldo EH-PAY")
        print("2. Tambah Saldo EH-PAY")
        print("3. Pilih PC Yang Ingin Digunakan")
        print("4. Kembali")
        pil=str(input("Masukkan Pilihan : "))
        if (pil=="1"):
            pin  = pwinput.pwinput("\nMasukkan PIN Anda : ",mask="*")
            print("")
            if pin == akun_pelanggan[i]["pin"]:
                print("Saldo Anda: Rp " + str(akun_pelanggan[i]["saldo"]))
                input("\nTekan ENTER untuk Kembali Ke Menu.")
            else:
                input("PIN Yang Anda Masukkan Salah!! Tekan ENTER untuk Kembali Ke Menu")
            print("")
        elif (pil=="2"):
            print("")
            pin  = pwinput.pwinput("Masukkan PIN Anda : ",mask="*")
            if pin == akun_pelanggan[i]["pin"]:
                try:
                    jumlah = int(input("Masukkan Jumlah Saldo Yang Ingin Ditambahkan : "))
                    if jumlah > 0:
                        saldo_awal = akun_pelanggan[i]["saldo"]
                        saldo_akhir = int(saldo_awal) + jumlah
                        akun_pelanggan[i]["saldo"] = saldo_akhir
                        input("Saldo Berhasil Ditambahkan. Tekan ENTER Untuk Kembali.")
                        simpan_daftar_pelanggan()
                    else:
                        input("Jumlah Saldo Harus Positif. Tekan ENTER Untuk Kembali Ke Menu.")
                except ValueError:
                    input("Masukkan Jumlah Saldo Dalam Bentuk Angka. Tekan ENTER Untuk Masukkan Ulang.")
            else:
                input("PIN Yang Anda Masukkan Salah!! Tekan ENTER untuk Kembali Ke Menu")
            print("")
        elif (pil=="3"):
            menu_pc(akun_pelanggan[i])
        elif (pil=="4"):
            print("")
            break
        else:
            input("Masukkan Pilihan Dengan Benar!!!! Tekan ENTER Untuk Kembali.")

def login_admin():
    username = str(input("Masukkan Username : "))
    password = str(pwinput.pwinput("Masukkan Sandi : ",mask="*"))
    for i in range(len(akun_admin)):
        if (username == akun_admin[i].get("nama") and password == akun_admin[i].get("sandi")) :
            data_admin = {"nama":akun_admin[i]["nama"]}
            menu_admin(data_admin)
            return
        else:
            continue
    input("Username Atau Password Yang Anda masukkan Salah !! Tekan ENTER Untuk Kembali.")
    print("")

def login_user():
    username = input("Masukkan Username : ")
    password = pwinput.pwinput("Masukkan Sandi : ",mask="*")

    for i in range(len(akun_pelanggan)):
        if username == akun_pelanggan[i].get("nama") and password == akun_pelanggan[i].get("sandi"):

            data_pengguna = {
                'nama': akun_pelanggan[i]['nama'],
                'saldo': akun_pelanggan[i]['saldo'],
            }
        
            index_penunjuk_akun = i

            menu_pelanggan(data_pengguna,index_penunjuk_akun)
            return
        else:
            continue
    input("Username Atau Password Yang Anda Masukkan Salah !! Tekan ENTER Untuk Kembali.")
    print("")

def tambah_user():
    while True:
        try:
            baru = {}
            nama = str(input("masukkan nama : "))
            sandi = int(input("masukkan sandi : "))
            saldo = 0
            pin = int(input("masukkan pin : "))
            if " " in nama:
                input("Masukkan Data Tanpa Spasi!!! Tekan ENTER Untuk Kembali.")
            if nama == "":
                input("Masukkan Data Dengan Benar!!! Tekan ENTER Untuk Kembali.")
            else:
                baru.update({
                    "nama" : nama,
                    "sandi" : sandi,
                    "saldo" : saldo,
                    "pin" : pin,
                            })
                akun_pelanggan.append(baru)
                simpan_daftar_pelanggan()
                input("Pendaftaran Berhasil. Tekan Enter Untuk Kembali. ")
                return
        except ValueError:
            input("Masukkan Data Dengan Benar!! (Sandi Dan Pin Harus Berupa Angka).\nTekan ENTER Untuk Kembali.")
            return
while True:
    ambil_data_pc_csv()
    ambil_data_pelanggan_csv()
    ambil_data_admin_csv()
    print("="*10,"SELAMAT DATANG", "="*10, "\n\tDI WARNET (SAUDARA)","\n")
    print("Menu.")
    print("1. Login Admin")
    print("2. Login Pengguna")
    print("3. Daftar Sebagai Pengguna Baru")
    print("4. Keluar")
    pilihan = str(input("Masukkan Pilihan : "))
    print("")
    if (pilihan=="1"):
        login_admin()
    elif (pilihan=="2"):
        login_user()
    elif (pilihan=="3"):
        tambah_user()
    elif (pilihan=="4"):
        sys.exit()

