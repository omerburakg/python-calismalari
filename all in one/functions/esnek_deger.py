def toplama(*a):
    toplam = 0
    for i in a:
        toplam += i
    return toplam


print(toplama(3, 4, 5, 6, 11, 15))


def çarp(*a):
    carpma = 1
    for i in a:
        carpma *= i
    return carpma


print(çarp(10, 10, 10, 2))

çifttek = lambda sayi: sayi % 2 == 0  # LAMBDA İFADESİ
print(çifttek(123))
