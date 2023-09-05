a = input(
    """*******************************************
        Ucgen-Dortgen Hesaplama
Lütfen İşlemı Yazınız.
Ucgen
Dortgen
*******************************************
"""
)
if a == "Ucgen" or a == "Ücgen" or a == "Üçgen":
    x = int(input("1. Kenar: "))
    y = int(input("2. Kenar: "))
    z = int(input("3. Kenar: "))
    if abs(x + y) > z and abs(y + z) > x and abs(x + z) > y:
        if x == y and x == z:
            print("Eşkenar Üçgen")
        elif (
            (x != y and x == z)
            or (x == y and x != z)
            or (z == y and z != x)
            or (y == z and y != x)
        ):
            print("İkizkener Üçgen")
        else:
            print("Sıradan Üçgen")
    else:
        print("Üçgen Belirtmiyor.")
elif a == "Dortgen" or a == "Dörtgen":
    x = int(input("1.Kenar: "))
    y = int(input("2.Kenar: "))
    z = int(input("3.Kenar: "))
    d = int(input("4.Kenar: "))
    if (a == x) and (x == y) and (x == z) and (x == d):
        print("Kare ")
    elif (x == z) and (y == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen Belirtmiyor.")
else:
    print("Bir Hata İle Karşılaşıldı.")
