if __name__ == '__main__':
    a = int(input("Masukkan bilangan 1 : "))
    b = int(input("Masukkan bilangan 2 : "))
    c = int(input("Masukkan bilangan 3 : "))

    if a <= b <= c:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (a, b, c))
    elif a <= c <= b:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (a, c, b))
    elif b <= a <= c:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (b, a, c))
    elif b <= c <= a:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (b, c, a))
    elif c <= a <= b:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (c, a, b))
    else:
        print("Urutan bilangan dari yang terkecil adalah %d %d %d" % (c, b, a))