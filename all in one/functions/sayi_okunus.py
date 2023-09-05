# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = [
    "",
    "On",
    "Yirmi",
    "Otuz",
    "Kırk",
    "Elli",
    "Altmış",
    "Yetmiş",
    "Seksen",
    "Doksan",
]


def sayi_okut(sayi):
    birler_bas = sayi % 10
    onlar_bas = sayi // 10
    return (onlar[onlar_bas], birler[birler_bas])


print(
    """İki Haneli Sayı Okutma
Çıkmak İçin 'q'"""
)

while True:
    sayi = input("Sayıyı Giriniz: ")
    if sayi == "q":
        print("Hoşça Kalın..")
        break
    else:
        sayi = int(sayi)
        print(sayi_okut(sayi))
