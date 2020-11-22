import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0

    while (id != int(atm.cekPin()) and trial < 3):
        id = int(input("Pin anda salah. Silakan Masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()  
    break

while True:
    print('Selamat Datang :D')
    print('\n 1 - Cek Saldo \n 2 - Tarik \n 3 - Simpan \n 4 - Ganti Pin \n 5 - Keluar ')
    selectmenu = int(input('\nSasukan pilihan anda :'))

    if selectmenu == 1:
        print("\nSaldo anda sekarang: Rp. " + str(round(atm.cekSaldo())) + "\n" )
    elif selectmenu == 2:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(round(nominal)) + " ")

        if verify_withdraw == "y":
            print("Saldo awal anda adalah: Rp. " + str(round(atm.cekSaldo())) + "")
        else:
            break
        
        if nominal <= atm.cekSaldo():
            atm.withdrawBalance(nominal)
            print("Transaksi debet berhasil!")
            print("Saldo sisa sekarang: Rp. " + str(round(atm.cekSaldo())) + "")
        else:
            print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
            print("Silakan lakukan penambahan nominal saldo")

    elif selectmenu == 3:
        nominal = float(input("Masukkan nominal saldo: "))
        verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(round(nominal)) + " ")

        if verify_deposit == "y":
            atm.depositBalance(nominal)
            print("Saldo anda sekarang adalah: Rp." +
            str(round(atm.cekSaldo())) + "\n" )
        else:
            break
    elif selectmenu == 4:
        verify_pin = int(input("masukkan pin anda: "))
        while verify_pin != int(atm.cekPin()):
            print("pin anda salah, silakan masukkan pin: ")
        updated_pin = int(input("silakan masukkan pin baru: "))
        print("pin anda berhasil diganti!")

        verify_newpin = int(input("coba masukkan pin baru: "))

        if verify_newpin == updated_pin:
            print("pin baru anda sukses!")
        else:
            print("maaf, pin anda salah! ")
    elif selectmenu == 5:
        print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
        print("No. Rekord: ", random.randint(100000, 1000000))
        print("Tanggal: ", datetime.datetime.now())
        print("Saldo akhir: ", str(round(atm.cekSaldo())))
        print("Terima kasih telah menggunakan ATM Progate!")
        exit()
    else:
        print("Error. Maaf, menu tidak tersedia")
        