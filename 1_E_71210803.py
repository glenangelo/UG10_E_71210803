if __name__ == '__main__':
    print("""
    ===== Kalkulator Akar dan Pangkat =====
    Pilihan menu :
    1. Pangkat 2
    2. Pangkat 3
    3. Akar Kuadrat
    """)

    pilihan = int(input("Masukkan menu yang anda pilih : "))
    if pilihan == 1:
        n = int(input("Masukkan bilang yang ingin di pangkatkan : "))
        hasil = n * n
        print("Hasil dari pemangkatan bilangan {} dengan 2 (Kuadrat) adalah ".format(n), hasil)
    elif pilihan == 2:
        n = int(input("Masukkan bilang yang ingin di pangkatkan : "))
        hasil = n ** 3
        print("Hasil dari pemangkatan bilangan {} dengan 3 (Kubik) adalah ".format(n), hasil)
    elif pilihan == 3:
        n = int(input("Masukkan bilang yang ingin di akarkan : "))
        hasil = n ** (1/2)
        print("Hasil akar kuadrat dari bilangan {} adalah ".format(n), hasil)
    else:
        print("Pilihan menu yang di masukkan tidak sesuai")
