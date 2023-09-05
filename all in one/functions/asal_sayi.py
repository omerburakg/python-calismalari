def asal_mi(sayi):
    if sayi == 1:
        return False
    if sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True


while True:
    sayi = input("Sayıyı Giriniz:")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        if asal_mi(sayi):
            print("{} asal bir sayıdır.".format(sayi))
        else:
            print("Asal bir sayı değildir.")
