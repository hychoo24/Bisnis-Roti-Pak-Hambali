roti = 2000

while True:
    print("Pilih Menu")       
    print("1. Beli Roti")
    print("2. Jual Roti")
    print("3. Lihat Stock Roti")
    print("4. Keluar")
    
    pilihan = input("Pilih 1/2/3/4: ")
    if pilihan != '1' '2' '3' '4':
        print("Menu tidak ditemukan coba lagi")
        break
    
    if pilihan == '4':
        print("Anda Telah Keluar")
        break

    if pilihan == '1':
        print("Stock Roti Saat ini:", roti)
        tambah = int(input("Stock Roti yang akan dibeli: "))
        hasil = roti + tambah
        print("Stock Roti Sekarang =", hasil)


    elif pilihan == '2':
        print("Stock Roti Saat ini:", roti)
        jual = int(input("Stock Roti yang akan dijual: "))
        hasil = roti - jual
        print("Stock Roti Sekarang =", hasil)


    elif pilihan == '3':
        print("Stock Roti Saat ini:", roti)