# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.


a = float(input("Aracınız 100 kilometrede kaç litre yakıyor?"))
b = float(input("Kaç kilometre yaptınız?"))
c = float(input("Yakıtın Litre Ücreti:"))

a = a / 100
odeme = a * b * c
print("Toplam Ödenen Yakıt Tutarı: {}".format(odeme))
