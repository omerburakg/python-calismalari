# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
liste1 = []
liste2 = []


def ebob_bulma(sayi1, sayi2):
    for i in range(1, sayi1):
        if sayi1 % i == 0:
            liste1.append(i)
    for i in range(1, sayi2):
        if sayi2 % i == 0:
            liste2.append(i)


a = int(input("1.Sayıyı Giriniz: "))
b = int(input("2.Sayıyı Giriniz: "))

(ebob_bulma(a, b))
print(max(list(set(liste1).intersection(liste2))))
