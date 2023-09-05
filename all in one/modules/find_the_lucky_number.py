import random
import time

print(
    """
*********************************
        SAYI TAHMİN OYUNU
*********************************
"""
)

rastgele_sayi = random.randint(1, 40)
tahmin_hakki = 5
while True:
    tahmin = int(input(("Tahmin Ettiğiniz Sayı(40'a kadar): ")))
    if tahmin < rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Büyük Bir Sayı Girmelisin :)")
        tahmin_hakki -= 1
    elif tahmin > rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Küçük Bir Sayıya Ne Dersin?")
        tahmin_hakki -= 1
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler!!! Tam İsabet!")
        break
    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Bitti...")
        print("Sayımız:", rastgele_sayi)
        break
