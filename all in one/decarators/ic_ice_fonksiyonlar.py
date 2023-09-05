def selamla(isim):
    print("Selam", isim)


selamla("Ata")

merhaba = selamla

del selamla  # selamla fonksiyonu silindi fakat merhaba fonksiyonu hala bellekte yer almakta.

merhaba("Kemal")


print(
    "------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------"
)
# İÇ İÇE FONKSİYONLAR


def fonksiyon():
    def fonksiyon2():
        print("Küçük fonksiyondan herkese merhaba!")

    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")


fonksiyon()  # fonksiyonu çağırdı. fonksiyon tanımlı fakat fonksiyon2'yi çağırsaydık tanımlı olmadığı için hata verecekti.

# print(fonksiyon2()) NameError: name 'fonksiyon2' is not defined. Did you mean: 'fonksiyon'?


def fonksiyon(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    print(toplama(args))


fonksiyon(1, 2, 3, 4, 5, 6, 7)
