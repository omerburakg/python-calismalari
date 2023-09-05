import os
import time


def anafonksiyon(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplama
    elif islem_adi == "carpim":
        return carpim


fonk = anafonksiyon(
    "toplama"
)  # <function anafonksiyon.<locals>.toplama at 0x0000023DDD86E2A0>
print(fonk(1, 2, 3, 4, 5, 6, 7, 8))


fonk2 = anafonksiyon(
    "carpim"
)  # <function anafonksiyon.<locals>.carpim at 0x00000174C4CBE3E0>
print(fonk2(1, 2, 3, 4, 5, 6))

time.sleep(5)
os.system("cls")


def toplama(a, b):
    return a + b


def çıkarma(a, b):
    return a - b


def çarpma(a, b):
    return a * b


def bölme(a, b):
    return a / b


def anafonksiyon(func1, func2, func3, func4, işlem_adı):
    if işlem_adı == "toplama":
        print(func1(3, 4))
    elif işlem_adı == "çıkarma":
        print(func2(10, 3))
    elif işlem_adı == "çarpma":
        print(func3(3, 5))
    elif işlem_adı == "bölme":
        print(func4(10, 4))
    else:
        print("Geçersiz işlem.")


anafonksiyon(toplama, çıkarma, çarpma, bölme, "toplama")
time.sleep(1)
anafonksiyon(toplama, çıkarma, çarpma, bölme, "çıkarma")
time.sleep(1)
anafonksiyon(toplama, çıkarma, çarpma, bölme, "çarpma")
time.sleep(1)
anafonksiyon(toplama, çıkarma, çarpma, bölme, "bölme")
