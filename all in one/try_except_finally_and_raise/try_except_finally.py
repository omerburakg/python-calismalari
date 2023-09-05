try:  # Hata oluşursa devamındaki kodları okumaz ve ilgili except'e gider.
    sayi1 = float(input("Sayı1: "))
    sayi2 = float(input("Sayı2: "))
    print(sayi1 / sayi2)
except ZeroDivisionError:  # Herhangi bir hata belirtilmezse tüm hatalar bu bloğa gelir.
    print("Bir Sayiyi Sifira Bolmeye Calistiniz!")
except ValueError:
    print("Lütfen Girdiginiz Sayilari Kontrol Edin")
finally:
    print("'Finally' Çalıştı.")  # Hata olsa da olmasa da finally çalışır.

# Farklı hataları aynı except bloğuna yazabiliriz.

try:
    sayi1 = float(input("Sayı1: "))
    sayi2 = float(input("Sayı2: "))
    print(sayi1 / sayi2)
except (ZeroDivisionError, ValueError):
    print("ZeroDivisionError ya da ValueError hatası")
