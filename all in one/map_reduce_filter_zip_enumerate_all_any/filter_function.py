# Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

#     [(3,4,5),(6,8,10),(3,10,7)]

# Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

#     [(3, 4, 5), (6, 8, 10)]

# *** Not: filter() fonksiyonunu kullanmaya çalışın. ***


def ucgen_mi(tuple):
    if (
        abs(tuple[0] + tuple[1]) > tuple[2]
        and abs(tuple[2] + tuple[1]) > tuple[0]
        and abs(tuple[0] + tuple[2]) > tuple[1]
    ):
        return True
    else:
        return False


liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]

print(list(filter(ucgen_mi, liste)))
