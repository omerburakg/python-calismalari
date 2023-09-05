print(
    """******************************************
             Hesap Makinesi
İşlemler:
1) Toplama
2) Çıkartma
3) Çarpma
4) Bölme
******************************************
"""
)


a = int(input("1. Sayi:"))
b = int(input("2. Sayi:"))
c = int(input("İşlem:"))

if c == 1:
    print("{} ile {} toplamı {}".format(a, b, a + b))
elif c == 2:
    print("{} ile {} farkı {}".format(a, b, a - b))
elif c == 3:
    print("{} ile {} çarpımı {}".format(a, b, a * b))
elif c == 4:
    print("{} ile {} bölümü {}".format(a, b, a / b))
else:
    print("Geçersiz bir işlem girdiniz.")
