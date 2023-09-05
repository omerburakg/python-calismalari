import time

# def kareleri_hesapla(sayilar):
#     sonuc = list()
#     baslama = time.time()
#     for i in sayilar:
#         sonuc.append(i**2)
#     bitis = time.time()
#
#     print("Bu fonksiyon "+str(bitis-baslama)+" saniye sürdü.")
#     return sonuc
#
# def kupleri_hesapla(sayilar):
#     sonuc = list()
#     baslama = time.time()
#     for i in sayilar:
#         sonuc.append(i**3)
#     bitis = time.time()
#     print("Bu fonksiyon "+str(bitis-baslama)+" saniye sürdü.")
#     return sonuc
#
# kareleri_hesapla(range(100000))
# kupleri_hesapla(range(100000))


# Bu fonksiyonlar işlevsizdir ve kod tekrarı barındırmaktadır. Kod tekrarından kaçınmak için decorator kullanırız. Şimdi bu zaman farkını tekrarlamadan decorator ile yazalım.


def zaman_hesapla(func):  # dec
    def wrapper(sayılar):  # wrapper
        baslama = time.time()
        sonuc = func(sayılar)
        bitis = time.time()
        print(func.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuc

    return wrapper


@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc


@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc


kareleri_hesapla(range(100000))
kupleri_hesapla(range(100000))
