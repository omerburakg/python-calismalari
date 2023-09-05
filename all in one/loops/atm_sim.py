from turtle import goto

print(
    """
***********************************
                ATM
IŞLEMLER
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Çıkmak İçin 'q' basınız.
***********************************
"""
)
bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz: ")
    if islem == "q":
        print("Hoşça Kalın...")
        break
    elif islem == "1":
        print("Bakiyeniz {} Türk Lirasıdır.".format(bakiye))
    elif islem == "2":
        miktar = int(input("Yatırmak İstediğiniz Tutar: "))
        bakiye += miktar
        print("Bakiyeniz: {}".format(bakiye))
    elif islem == "3":
        miktar = int(input("Çekmek İstediğiniz Tutar: "))
        if (bakiye - miktar) < 0:
            print("Bakiyeniz Yetersiz.")
            continue
        bakiye -= miktar
        print("Bakiyeniz: {}".format(bakiye))
    else:
        print("Geçersiz İşlem!")
        continue
