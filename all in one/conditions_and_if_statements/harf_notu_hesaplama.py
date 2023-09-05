from typing import final

vize1 = int(input("1. Vize Notu:"))
vize2 = int(input("2. Vize Notu:"))
final_notu = int(input("Final Notu:"))

harf_notu = (vize1 * (30 / 100)) + (vize2 * (30 / 100)) + (final_notu * (40 / 100))

if harf_notu >= 90:
    print("Not: {} AA".format(harf_notu))
elif harf_notu >= 85:
    print("Not: {} BA".format(harf_notu))
elif harf_notu >= 80:
    print("Not: {} BB".format(harf_notu))
elif harf_notu >= 75:
    print("Not: {} CB".format(harf_notu))
elif harf_notu >= 70:
    print("Not: {} CC".format(harf_notu))
elif harf_notu >= 65:
    print("Not: {} DC".format(harf_notu))
elif harf_notu >= 60:
    print("Not: {} DD".format(harf_notu))
elif harf_notu >= 55:
    print("Not: {} FD".format(harf_notu))
elif harf_notu < 55:
    print("Not: {} FF".format(harf_notu))
else:
    print("Hatalı Değer Yazıldı.")
