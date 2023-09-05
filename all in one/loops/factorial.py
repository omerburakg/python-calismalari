# Faktoriyel Hesaplama
print(
    """
************************************
        Faktoriyel Hesaplama
Çıkmak için 'q' Basınız.
************************************
"""
)
while True:
    sayi = input("Sayiyi Giriniz:")
    if sayi == "q":
        print("Program Sonlandırılıyor...")
        break
    sayi = int(sayi)
    if sayi >= 0:
        faktoriyel = 1
        for i in range(2, sayi + 1):
            faktoriyel *= i
        print("Girdiğiniz {} sayısının faktöriyeli: {}".format(sayi, faktoriyel))
