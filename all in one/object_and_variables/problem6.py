# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
# Hipotenüs Formülü: a^2 + b^2 = c^2

print("Hipotenüs Hesaplama Programı\n")

a = float(input("Birinci Kenarı Giriniz: "))
b = float(input("İkinci Kenarı Giriniz: "))
c = (a**2 + b**2) ** 0.5
print("{} ile {} kenarlarının hipotenüsü {} ".format(a, b, c))
