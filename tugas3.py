while True :
    angka_1 = float(input("Masukkan angka pertama :"))
    angka_2 = float(input("Masukkan angka kedua: "))
    print("KALKULATOR SEDERHANA")
    print("Pilih operasi yang kamu inginkan")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Keluar")

    operasi = input("Ketik pilihanmu(1/2/3/4/5) :")

    if operasi =="1":
        hasil = angka_1 + angka_2
        print(f"hasil penjumlahan = {hasil}")
    elif operasi =="2":
        hasil = angka_1 - angka_2
        print(f"hasil pengurangan = {hasil}")
    elif operasi =="3":
        hasil = angka_1 * angka_2
        print(f"hasil perkalian = {hasil}")
    elif operasi == "4":
        if angka_2 == 0:
            print("Error :bilangkan kedua tidak bisa sama dengan 0")
        else:
            hasil = angka_1 / angka_2
            print(f"hasil pembagian = {hasil}")
    else:
        print("Terimakasih telah menggunakan kalkulator ini")
        break

    