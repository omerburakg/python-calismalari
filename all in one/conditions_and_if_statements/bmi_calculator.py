kilo = float(input("Kilonuzu kg cinsinden giriniz."))
boy = float(input("Boyunuzu metre cinsinden giriniz."))

bmi = kilo / (boy * boy)

if bmi < 18.5:
    print("Beden Kitle İndeksi {}. ZAYIF!".format(bmi))
elif 18.5 <= bmi < 25:
    print("Beden Kitle İndeksi {}. NORMAL!".format(bmi))
elif 25 <= bmi < 30:
    print("Beden Kitle İndeksi {}. FAZLA KİLOLU!".format(bmi))
elif 30 <= bmi:
    print("Beden Kitle İndeksi {}. OBEZİTE!".format(bmi))
else:
    print("Değerleri Hatalı Girdiniz.")
