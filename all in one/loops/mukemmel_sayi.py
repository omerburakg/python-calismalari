# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
print(
    """
************************************
        MÜKEMMEL SAYI BULMA
************************************
Çıkmak İçin "q" basınız.
"""
)
while True:
    degisken = input("Sayıyı Giriniz: ")
    if degisken == "q":
        print("Hoşça Kalın")
        break
    degisken = int(degisken)
    toplam = 0
    liste = []
    for i in range(1, degisken):
        if (degisken % i) == 0:
            liste.append(i)
    for i in liste:
        toplam += i
    if toplam == degisken:
        print("MÜKEMMEL SAYI!!")
    elif toplam != degisken:
        print("Mükemmel Sayı Değil.")
