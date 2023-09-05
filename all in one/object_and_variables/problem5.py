# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = float(input("İlk Sayıyı Giriniz: "))
b = float(input("İkinci Sayıyı Giriniz: "))

print("Girilen değerler: {} , {}".format(a, b))

a, b = b, a
print("Değişmiş Halleri: {} , {}".format(a, b))
