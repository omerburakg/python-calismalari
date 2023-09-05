import math

# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.


def ekok_bulma(sayi1, sayi2):
    ebob = math.gcd(sayi1, sayi2)
    ekok = (sayi1 * sayi2) / ebob
    return ekok


while True:
    sayi1 = int(input("1. Sayıyı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz: "))
    print(
        "{} ile {} En küçük ortak katı: {}".format(
            sayi1, sayi2, (ekok_bulma(sayi1, sayi2))
        )
    )
