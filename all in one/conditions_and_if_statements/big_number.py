a = int(input("1.Sayı:"))
b = int(input("2.Sayı:"))
c = int(input("3.Sayı:"))

if a > b and a > c:
    print("En Büyük Sayı", a)
elif b > a and b > c:
    print("En Büyük Sayı", b)
elif c > a and c > b:
    print("En Büyük Sayı", c)
else:
    print("Aynı Değerler Girildi.")
