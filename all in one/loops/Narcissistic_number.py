# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse
# bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4


print(
    """
**************************************
        ARMSTRONG SAYISI BULMA
çıkmak için "q" basınız.
**************************************
"""
)

while True:
    toplam = 0
    sayi = input("Sayıyı Giriniz: ")
    if sayi == "q":
        print("Hoşça Kalın...")
        break
    elif sayi != "q":
        liste = []
        for i in sayi:
            liste.append(int(i))
        for i in liste:
            toplam += i ** len(liste)
            if toplam == int(sayi) and (toplam >= 100 or toplam == 1 or toplam == 0):
                print("Armstrong Sayısı!!!")
        if toplam != int(sayi) or (1 < toplam < 100):
            print("Normal Sayı")
