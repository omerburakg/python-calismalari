def mukemmel_sayi(sayi):
    liste = []
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            liste.append(i)
    for i in liste:
        toplam += i
    if toplam == sayi:
        return "Mükemmel Sayı"
    else:
        return "Normal Sayı"


while True:
    print("Çıkmak için 'q'")
    sayi = int(input("Sayi"))
    print(mukemmel_sayi(sayi))

    if sayi == "q":
        print("Hoşçakalın")
        break
