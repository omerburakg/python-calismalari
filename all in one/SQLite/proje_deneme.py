from udemy_kütüphane import *

print(
    """*******************************
Kütüphane Programına Hoş geldiniz.

İşlemler:

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt

Çıkmak için 'q' basınız.

*******************************"""
)

kütüphane = Kütüphane()
while True:
    islem = input("İşlemi seçiniz: ")
    if islem == "q":
        print("Program sonlandırılıyor...")
        break
    elif islem == "1":
        kütüphane.kitapları_göster()
    elif islem == "2":
        isim = input("Kitabın Adı: ")
        kütüphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))

        yeni_kitap = Kitap(isim, yazar, yayınevi, tür, baskı)
        print("Kitap Ekleniyor....")
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")
    elif islem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        kütüphane.kitap_sil(isim)
        print("Kitap Silindi.")
    elif islem == "5":
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz: ")
        kütüphane.baskı_yukselt(isim)
        print("Baskı Yükseltildi.")
    else:
        print("Geçersiz İşlem!")
