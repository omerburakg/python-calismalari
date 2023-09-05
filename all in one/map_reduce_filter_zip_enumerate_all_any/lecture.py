from functools import reduce

# iterasyon yapılanlar


# reduce fonk çağrıldı
def double(x):
    return x**2


print(map(double, [1, 2, 3, 4, 5, 6]))
print(list(map(double, [1, 2, 3, 4, 5, 6])))
# Map kısaca bir fonku çoklu işleme uygulamak içindir.
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
liste3 = [9, 10, 11, 12, 13]
# Burada x= 1 y = 5 z =9 x = 2 y = 6 z = 10 şeklinde devam edecektir. Z 5 adet x ve y 4 adet olduğu için 13 hesaplanmayacaktır.
print(list(map(lambda x, y, z: x * y * z, liste1, liste2, liste3)))


def toplama(x, y):
    return x + y


print(reduce(toplama, [12, 18, 20, 10]))

# reduce ilk iki değeri alır ve işleme sokar. Sonucu 3. ile işleme sokar, çıkan sonucu sonraki değerler ile sıra sıra işleme sokar.

print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))


def maksimum(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "equal"


print(reduce(maksimum, [-2, 3, 1, 4]))

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# filter() fonk. birinci parametre olarak mutlaka bool dönen fonk alır ve liste gibi veritiplerinin her bir elemanına bu fonku uygular. filter sadece true
# sonuç çıkaran değerleri alarak bir tane filter objesi döndürür.


def asal_mi(x):
    i = 2
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        while i < x:
            if x % i == 0:
                return False
            i += 1
        return True


print(list(filter(asal_mi, range(1, 100))))


liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10, 11]

print(list(zip(liste1, liste2)))
# zip fonk. listelerin elemanlarını sırasıyla demet şeklinde gruplayarak bir tane liste oluşturur.
liste3 = ["Python", "PHP", "Java", "Javascript"]
print(list(zip(liste1, liste2, liste3)))

liste1 = [1, 2, 3, 4]
liste2 = ["Python", "PHP", "Java", "Javascript"]

for i, j in zip(liste1, liste2):
    print("i:", i, "j:", j)
# Aynı anda iki liste üzerinde gezinmek

sözlük1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
sözlük2 = {"Sıfır": 0, "Bir": 1, "İki": 2}
# sözlükleri zipleyelim
print(list(zip(sözlük1, sözlük2)))  # anahtarlar eşleşti.
print(list(zip(sözlük1.values(), sözlük2.values())))  # Değerler eşleşti


liste = ["Elma", "Armut", "Muz", "Kiraz"]
print(list(enumerate(liste)))
# enumerate her elemanı indexler ve demet çifti oluşturur.

liste = ["a", "b", "c", "d", "e", "f", "g"]
for i, e in enumerate(liste):  # index,eleman
    if (i % 2) == 0:
        print(e, i)


liste.clear()
### ---------------------------------------- ALL ve ANY -----------------------------------------------------


def hepsi(liste):
    for i in liste:
        if not i:  # i false ise
            return False
    return True


liste = [True, False, True, False, True]
print(
    hepsi(liste)
)  # Her şeyde görmek için print yazdık.. çünkü ben anaconda tarzı şeyler kullanmayan bi malım..
liste = [1, 2, 3, 4, 5]
print(hepsi(liste))


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False


print(herhangi([True, False, True, False, True]))
liste = [0, 0, 0, 0, 0]
print(herhangi(liste))
print("\n***************************************\n")
# İşte all() ve any() fonksiyonları bu işlemleri bizim için kolaylaştırmaktadır.

# all() fonksiyonu bütün değerlerimiz true ise true, en az bir değer False ile False değer döndürmektedir.
print("all")
liste.clear()
liste = [True, False, True, False, True]
print(all(liste))
print(all([True, True, True]))

# any() fonksiyonu ise bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
print("\nany")
liste = [True, False, True, False, True]
print(any(liste))
liste = [0, 0, 0, 0, 0]
print(any(liste))
