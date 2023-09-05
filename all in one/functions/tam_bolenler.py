def tam_bolenleri_bulma(sayi):
    tam_bolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    sayi = input("Sayıyı Giriniz")

    if sayi == "q":
        print("Hoşça kalın.")
        break
    else:
        sayi = int(sayi)
        print(tam_bolenleri_bulma(sayi))
