# Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

#         [(3,4),(10,3),(5,6),(1,9)]

# Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

#         [12, 30, 30, 9]

# *Not : map() fonksiyonunu kullanmaya çalışın.*

liste = [(3, 4), (10, 3), (5, 6), (1, 9)]


def alan(tuple):
    return tuple[0] * tuple[1]


print(list(map(alan, liste)))
