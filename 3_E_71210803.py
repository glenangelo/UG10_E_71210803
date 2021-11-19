if __name__ == '__main__':
    names = input("Masukkan daftar siswa : ").title().split(', ')
    print("Daftar Siswa :", names)
    newName = input("Masukkan siswa yang ingin ditambahkan : ").title()

    if newName in names:
        print("Siswa atas nama {} sudah berada dalam daftar siswa".format(newName.upper()))
    else:
        names.append(newName.upper())
        print("Hasil penambahan pada daftar siswa : ", names)