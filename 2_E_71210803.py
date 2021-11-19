if __name__ == '__main__':
    n = float(input("Masukkan suhu tubuh Anda : "))

    if n < 32:
        print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
    elif 32 <= n <= 37.5:
        print("Suhu Anda normal!")
    elif 37.5 < n <= 50:
        print("Anda demam! Jangan bepergian ke tempat fasilitas umum")
    else:
        print("Anda bukan Manusia :)")
