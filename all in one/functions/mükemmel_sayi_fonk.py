def mukemmel_sayi_bulma(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if sayi == toplam:
        return True
    else:
        return False


while True:
    sayi = input("Sayıyı Giriniz: ")
    if sayi == "q":
        print("Hoşça Kalın..")
        break
    else:
        sayi = int(sayi)
        if mukemmel_sayi_bulma(sayi):
            print("Mükemmel Sayı!!!", sayi)
        else:
            print("Normal Sayı", sayi)
